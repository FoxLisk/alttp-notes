# Setting high values with spins

Link's spin animation is actually 2 different ancillae. The first one (`2A`) only lasts a few frames and counts duration up from 0 to 4, which isn't very useful. However, it then replaces itself with the second sprite (`2B`), which sets the duration to 49 (this is almost as high as beams, which set 4C).

Crucially, _neither spin sprite sets the direction value_! This means we can set direction with something else - for example, we can [use arrows](arrows.md) to set a diagonal direction and use a spin to get a long hookpush. We can also use this to get more distance than we normally can with other ways of setting direction, including some [low item setups](#low-item-setups).

In order to get a long duration out of this, we need to start a spin and then interrupt it almost immediately, in whatever slot we've set our desired direction in. In practice this is slot 0, because this stuff only really works with slot 9 block pushes afaict.

# Stopping Coordinates

Be careful - the spin **does** set [stopping coordinates](stopping_coordinates.md). These coordinates are dependent on both Link's coordinates when you spin, and the direction Link is facing. I have included the direction set by `2A` for completeness; it shouldn't matter in real setups, which depend on the `2B` ancilla.

| Link's direction | `2A` X | `2A` Y | `2B` X | `2B` Y | Summary        |
| ---------------- | ------ | ------ | ------ | ------ | -------------- |
| Left             | X+1C   | Y+0A   | X+19   | Y+18   | 1.5 tiles `v>` |
| Up               | X+0A   | Y+20   | X-03   | Y+1C   | ~2 tiles `v`   |
| Right            | X-0A   | Y+14   | X-08   | Y+06   | 0.5 tiles `<v` |
| Down             | X+07   | Y-08   | X+15   | Y-02   | 1.5 tiles `>`  |

I'm pretty sure this is the starting coordinate of the little swirly sparkly thingy that spins around, if that helps.

I think the easiest takeaway here is that with a successful spin setup facing right, your stopping coordinates will be approximately half a tile SW from where you start; so make sure to position yourself not to hookpush past that line.

If you're moving at 4px/f in a direction and you start (2+4n)px off of your stopping coord in that direction, you'll never get stopped in that direction. This is super convenient because this means using a right spin and then hookpushing from that same Y coordinate always gets you past your stopping coord (because `6 = 2 + 4 * 1`).

# Setups

The rest of this document is various setups for getting slots and timing to work out.


Here are some setups for setting high duration values in slot 0.

## Blue Boom/Fire Rod

1. Place a slot 3 block
2. Place bomb
3. Slash sword 4 times, holding on the 4th one
4. Right before sword is charged, throw boom/fire rod
5. Dash dust
6. Release spin

This is harder with the fire rod, because the casting animation kills your sword sparkles. You have to delay between the shot and the spin release, and you have to spin before the firerod despawns, and you have to time it all against the bomb. It's manageable but blue boom is much more forgiving.

## Ice Rod

This assumes nothing except the slot 9 block is down (i.e. free front slots)

1. Place bomb
2. Slash sword 3 times, holding on the 3rd
3. When the spin is charged, ice rod
4. After the ice rod projectile has traveled about 2 tiles, release spin

This is a little finicky because of how many sparkles are de- and re-spawning all the time.

This unfortunately doesn't work with red boom - with sword sparkles out, the red boom sparkles go ape shit and fill up all your slots and your spin doesn't reliably go into slot 0. I haven't found a workable red boom setup yet.

# Low Item Setups

You can use the cane beams and some timing to get a high duration value in slot 0 - **BUT** it will involve setting the direction value at the same time. We can use these to get long north/west/south hookpushes with minimal extra items.

Somaria beams spawn from the highest available front slot downwards (i.e. they want to go in slot 4, then 3, then 2, then 1, then 0), and they spawn in this order:

1. Right
2. Left
3. Down
4. Up

We can use this to get long hookpushes by combining with our spin stuff if we are careful about where the beams go, but horizontal ones require another item (afaict).

If we have a bomb down when we break the somaria block, the up beam goes in slot 0. If it then immediately hits something and despawns, and then we spin, and then we get hit, we have our direction set to north and our duration very high.

If we fill another slot and then make sure the down beam despawns first, we can get a long down hookpush. 

If we fill one more slot and then make sure the west beam despawns first, we can get a long west hookpush.

If we fill *yet another* slot, the block won't break at all, unfortunately, so east hookpushes are out of our reach.

In practice, the way this works is you start like so:

1. Slot 9 block
2. Slot 3 block against a wall in the appropriate direction
3. Bomb

followed by some slight variation on:

1. 3 slashes, hold charge on the 3rd
2. When the charge is full, break the block
3. After the first beam despawns, release the spin

This setup, unaltered, will get you a long up hookpush (if your block is against something to the north, ofc)

For a down push, use blue boom or ice rod or kick up dust (if you kick up dust you'll have to do it twice; once for the break and again for the spin). 

For a left push, do two of the above (boom + ice rod, boom + double dust, ice rod + double dust)

## Even lower item stuff

  We can use a slot 0 bomb to set direction and then do a spin to set duration. This allows us to get long hookpushes with nothing but boots, fighter sword, cane, hook, and a high search index. 
  You can use this to get a long cardinal push in any direction, including east. This might just be more useful than the whole prior section, maybe including that stuff is a mistake. We'll see.

The problem we're up against here is that we are trying to set direction with a slot 0 bomb; but we also need to get hit by a bomb while we have a spin in slot 0. So we need to set distance with a slot 0 bomb, then place another bomb in a different slot, and then place a spin in slot 0 such that we get hit by the second bomb.

We can do this by timing bombs to get a slot 0 bomb:

1. Slot 9 block
2. Slot 3 block
3. Slot 1 bomb
4. As it's exploding, slot 0 bomb
5. New slot 1 bomb pretty shortly after the slot 0
6. As the slot 0 bomb is exploding, break the block
7. After the slot 0 bomb goes away, spin and get hit by the slot 1 block.


We can also use somaria beams to get a slot 0 bomb:

1. slot 9 block
2. slot 3 block
3. Break block, place bomb (in slot 0)
4. After a brief pause, place another bomb (in slot 1)
   * I use 4 slashes for timing here but it's not perfect
5. Place another slot 3 block
6. As the slot 0 bomb is finishing its explosion, break the block
7. After the slot 0 bomb is gone, release spin and get hit.

You could, instead, wait for the slot 0 bomb to disappear before breaking the block, and then spin after the up beam disappears. This requires more careful positioning of the block and does not seem, to me, to make the timing any easier.

And, for fun, here is a setup using a misslotted bomb.

[Here is a setup with a misslotted bomb](bomb_misslot_east.mp4).
