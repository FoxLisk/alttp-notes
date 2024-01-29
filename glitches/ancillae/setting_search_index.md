# Setting the Search Index

## Slot 2 Items

Certain ancillae, when spawned into slot 2, will directly write values to the search index.

### Ice Rod

A slot 2 ice rod sets search index to 0.

### Lamp

A slot 2 lamp sets the search index to a different value depending on what direction Link is facing:

| Facing | Search index |
| ------ | ------------ |
| Left   | `$10`        |
| Up     | `$0D`        |
| Right  | `$07`        |
| Down   | `$0A`        |

### Powder

Powder behaves as follows. Starting from the frame that the chime plays (which is one frame before the powder sprinkle animation starts displaying):

```
Frame  1: Set the search index based on the direction Link is facing, to the same value as the lamp would.
Frame  2: Increment search index
Frame  3:
Frame  4: Increment search index
Frame  5:
Frame  6: Set search index to 0
Frame  7:
Frame  8: Increment search index
Frame  9:
Frame 10: Increment search index
Frame 11:
Frame 12: Increment search index
Frame 13:
Frame 14: Increment search index
Frame 15:
Frame 16: Increment search index
Frame 17:
Frame 18: Increment search index
```

Thus ending up with a value of 6, regardless of facing direction. It's worth noting here that you can interrupt this animation with a S&Q or, in the case of fake powder, a screen transition, to end up on values other than 6.


Since Powder sets the search index, fake powder can be very useful. Since you can move during fake powder, you can find setups to activate fake powder next to a screen transition and have the transition stop the powder animation at a point with a high index set.

See [Fake Items](/glitches/fake_items.md) for more info, including ledgepog setups.

## Misslotted Bombs

Misslotting a bomb (i.e. putting it in any slot besides 0 and 1) leaves you with the following search indices:

| Slot | Index |
| ---- | ----- |
| 2    | 0     |
| 3    | 3     |
| 4    | 7     |

Note that a slot 3 bomb leaving you with search index 3 is normal and expected by the rules of misslotting; bombs in slot 2 and 4 are the odd ones because they set specific values.

Bombs in back slots (and slot 3!) have the normal behaviour of leaving the search index at the slot they went into.

## Bombable Wall Debris

Bombs that blow up walls become bombable wall debris in the same slot after they're done exploding. This bombable wall debris has the following effects if misslotted:

### Slot 2 Bombable Wall Debris

This increments the search index slowly up to 4. If your search index is >= 4 when this process starts, it will increment until it wraps around and gets to 4, which means it will set some very high indices. You can achieve this easily by doing an arrow replacement.

The way it updates is that it does an 8-frame loop where first it updates the search index (the first time through this step is skipped), then 2 frames later it updates the debris animation.

```
00 Ancilla set to $08 OR search index incremented (on subsequent loops)
01
02 Debris animation updated
03
04
05
06 
07
```

The last debris update is after the last index increment.

This process continues while the game is paused.

**NOTE**: Since you can get extremely high search indices with this, it is possible to do ACE and other misslotting of questionable legality. I don't know exactly how high of an index is safe. `$10` is obviously safe (lamp sets it and that never causes trouble). If you're attempting to use this to set index I would recommend trying to stop by around `$10`.

### Slot 4 Bombable Wall Debris

This sets the search index to 7, then counts down to 0 repeatedly, and ends on 7 again.

In particular, the timer that is being used to govern the 8-frame loop described above is affecting the search index directly with slot 4 debris. This loop normally occurs 4 times, but specifically it occurs until `$7E03C6` is set to `$04`; I don't know exactly what else affects that value at present.

### Slot 5 Bombable Wall Debris

This sets your search index to a value based on the direction the *door* is facing.

| Facing | Value |
| ------ | ----- |
| North  | `0x20`|
| South  | `0xD0`|
| Left   | `0x78`|
| Right  | `0x78`|

## Fairy Revival

Any fairy revival, including from a deathhole, sets the search index to 6.
