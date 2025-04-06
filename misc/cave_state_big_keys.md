When reading or writing Big Key data, the game looks up a bitmask based on your dungeon ID. When trying to open a big door or big chest, this bitmask is compared against your existing Big Keys to see if you can open it. When obtaining a Big Key, this bitmask is used to determine which Big Key(s) to give you.

In cave state, or xor cave state, the bitmask that is loaded is a piece of ROM that was not intended to be a bitmask, giving different results.

The rest of this document gets into the gory technical details. See [the wiki page](https://alttp-wiki.foxlisk.com/index.php/Cave_state) for the info that's useful to gameplay.


# Facts

There are 2 bytes of SRAM containing all Big Key data, at `$7EF366`. This is a bitfield where each bit represents the Big Key of a particular dungeon, with the following layout (stolen entirely from [kan's disassembly](https://github.com/spannerisms/jpdasm/blob/master/symbols_sram.asm#L717)):

```
; xced aspm    wihb tg..
;   c - Hyrule Castle
;   x - Sewers
;   a - Agahnim's Tower
;
;   e - Eastern Palace
;   d - Desert Palace
;   h - Tower of Hera
;
;   p - Palace of Darkness
;   s - Swamp Palace
;   w - Skull Woods
;   b - Thieves' Town
;   i - Ice Palace
;   m - Misery Mire
;   t - Turtle Rock
;   g - Ganon's Tower
```

`$040C` is the memory address that holds current dungeon ID.

In cave state, your dungeon ID is `$FF`. In xor cave, your dungeon ID is `$FD`.


# Reading Big Key Data

When you try to open a big door/big chest, the data at `$7EF366` is checked. This is done in a few different places in the code, sometimes with a special [bitmask](#bitmask) and sometimes by directly using your [dungeon ID](#dungeon-id). I'm not sure why the difference.

## Bitmask

There are several chunks of code that check for a big key (`#_01CF22`, `#_01EB8A`, `#_01EC17`), with the code looking like this (sometimes using the Y accumulator instead):

```
#_01EC14: LDX.w $040C                   ; load current dungeon ID
#_01EC17: LDA.l $7EF366                 ; load Big Key flags
#_01EC1B: AND.l DungeonMask,X
#_01EC1F: BEQ .no_big_key_for_big_chest
```

This loads your current Big Key data, then `AND`s it against a bitmask, and if the result is nonzero, you're allowed to open the big chest. Normally, this bitmask is going to have a single bit set, corresponding to the dungeon you're in, and that will be compared against the Big Keys you have, which are (supposed to be!) set in the same way.

However, in cave (or xor cave) state, the data that gets loaded is way outside of what was intended, so we get a different bitmask. In cave state, the bitmask is `$CA17` (or `0b1100101000010111`). In xor cave, the bitmask is `$C40F` or `0b1100010000001111`. This means several different Big Keys will work.

[Much more detail here](#bitmasks-for-reading) if you want it.

## Dungeon ID

There is one place that does this differently: drawing the menu. This uses your dungeon ID directly instead of using a bitmask. This code is trying to use the dungeon ID as an index into the Big Key bitflags. It does this by dividing the dungeon ID by 2 and then left shifting the Big Key value that many times + 1. If the last bit shifted off is a 1, you have the big key. Normally this works because the Big Key flags are in fact stored this way, but of course in Cave State this is not correct.

```
ItemMenu_DrawMapAndBigKey:
#_0DEE57: REP #$30

#_0DEE59: LDA.w $040C        ; load dungeon ID
#_0DEE5C: AND.w #$00FF
#_0DEE5F: CMP.w #$00FF       ; in cave state, just skip ahead
#_0DEE62: BEQ .no_big_key

#_0DEE64: LSR A              ; A >> 1
#_0DEE65: TAX                ; X = A
#_0DEE66: LDA.l $7EF366      ; A = Big Key data

.shift_for_key
#_0DEE6A: ASL A              ; A << 1

#_0DEE6B: DEX                ; x -= 1
#_0DEE6C: BPL .shift_for_key ; if X >= 0, GOTO .shift_for_key

#_0DEE6E: BCC .no_big_key    ; if the last bit shifted off of A was a 0, we have no big key
```

This short circuits if you're in cave state. If you're in xor cave, though, it will shift `$3F` bits off of your accumulator, so the `BCC` will branch and not draw the Big Key.


# Writing Big Key Data

The place that writes Big Key data is in `bank_09.asm`. The exciting part looks like this:

```
#_0986A5: LDX.w $040C            ; X = dungeon ID

#_0986A8: REP #$20

#_0986AA: LDA.w .dungeon_masks,X ; load the flags to write
#_0986AD: ORA.b [$00]            ; OR them with existing data (do not erase Big Keys)
#_0986AF: STA.b [$00]            ; store the updated Big Key flags
```

Here, the value in `$00` is `$7EF366` ([see why](#item-receipt-context)), which is the same location from above, where our Big Key data lives. The `.dungeon_masks` table is supposed to give you a bitmask with one bit set based on your dungeon ID, but of course we are reading way out of bounds. The data we load up is `$D020` (`0b1101000000100000`) in cave state, and `$C003` (`0b1100000000000011`) in xor cave. [See how we find these values](#bitmasks-for-writing)


The code then `OR`s this with the existing Big Key data, to make sure we don't wipe out any already claimed keys, and saves the result, giving us the indicated Big Keys.

# Appendices

## Bitmasks For Reading

There's a sequence of bitmasks stored starting at [`#_0098C0`](https://github.com/spannerisms/jpdasm/blob/master/bank_00.asm#L4327). It's 16 elements long, with one for each dungeon.

It looks like this:

```
DungeonMask:
#_0098C0: dw $8000 ; Sewers
#_0098C2: dw $4000 ; Hyrule Castle
...
```

In cave state, we read way past the intended 16 elements.

For regular cave state, we're looking at `DungeonMask,$FF`. This works out to be the value at `#_0099BF`. The relevant ROM looks like this:

```
#_0099BE: dw $17C4
#_0099C0: dw $07CA
```

The [Asar manual](https://rpghacker.github.io/asar/asar_19/manual/) tells us that

> [w]hen using dw, dl or dd, each number is converted to little-endian

which means that the actual ROM data looks like this:

```
#_0099BE: $C4
#_0099BF: $17
#_0099C0: $CA
#_0099C1: $07
```

So the two bytes in ROM are `$17CA`. When this is loaded as a little-endian word, we get `$CA17`.

For xor cave (`$FD`), we get the values from `$99BD`, which are 

```
#_0099BC: dw $0FC4
#_0099BE: dw $17C4
```

meaning we get back the value `$C40F` or `0b1100010000001111`

## Item Receipt Context

This is the code that sets up the memory at `$00`-`$02` before the code that saves our Big Keys [above](#writing-big-key-data).

The relevant code is in `AncillaAdd_ItemReceipt` and goes something like this (**heavily** edited for brevity):

```
#_09860A: LDY.w $02D8 ; Y = the ID of the item we're getting
#_098624: TYA         ; A = Y
#_098625: ASL A       ; A << 1
#_098626: TAX         ; X = A
```

The Big Key item get ID is (`$32`). We left shift it once (`$64`), and set X to that value. We then load some data from that table:

```
#_098627: LDA.w .sram_write+0,X
#_09862A: STA.b $00

#_09862C: LDA.w .sram_write+1,X
#_09862F: STA.b $01

#_098631: LDA.b #$7E
#_098633: STA.b $02
```

This is taking the data from the indicated element of `.sram_write` and writing it to `$00`, which is used as the address of where to write data.

```
.sram_write
#_0984E2: dw $7EF359 ; FIGHTER SWORD
...
#_098546: dw $7EF366 ; BIG KEY
```

As expected, this is giving us the address `$7EF366`, which is the same memory we were looking at when *reading* Big Keys. That's reassuring.

## Bitmasks For Writing

Similarly to the [bitmasks for reading](#bitmasks-for-reading), there is a block of bitmasks in ROM used for writing Big Keys. This one is only 14 elements long, though (they didn't include the two unused masks).

```
.dungeon_masks
#_0985C6: dw $8000 ; Sewers
...
```

The ROM address we actually read is `$0986C3` for xor cave and `$986C5` for cave state. The disassembly tells us the relevant lines of code are:

```
#_0986C1: STA.w $0309

.not_heart_container
#_0986C4: CPY.b #$20                 ; ITEMGET 20
#_0986C6: BNE .not_crystal_or_caping
```

Rather than working out the exact bytes myself, I inspected the ROM. In the ROM, these bytes are at `$486C3-$486C6` because of LoROM mapping stuff.

```
0986C3: 03
0986C4: C0
0986C5: 20
0986C6: D0
```

Adjusting for endianness, these values are `$D020` (or `0b1101000000100000`) in cave state, and `$C003` (or `0b1100000000000011`) in xor cave.