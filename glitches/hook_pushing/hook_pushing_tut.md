
====

1. What and why

  1. Hookpushes allow you to move with absolutely no collision detection for potentially long distances, which is useful for e.g. skipping doors that you can't open, or moving around the EG map within the rules of No Logic

1. Two ways to hookpush:

  1. Somaria hookpushes
  1. Stuckpushes

1. Prereq: Ancilla

  1. Ancilla are stuff link makes, with his items/sword/boots
  1. There are 10 slots for ancilla.

    1. The first 5 (0-4) are where most ancilla want to go, starting from 4.

      1. Bombs are special and want to go in 1 and 0
    1. The back 5 (5-9) are where sparkles (from sword charges, silver arrows, etc) want to go
  1. Under some circumstances, ancilla that want to go in slots 0-4 can be convinced to go in slots 5-9 instead. This is called "misslotting."
    1. This happens when an ancilla tries to spawn but: slots 0-4 are full, there is a sparkle in slots 5-9, and the search index is at least as high as the sparkle's slot number

1. Somaria hookpushes
  1. Easier to do powerful stuff with, but requires somaria.
  1. Overview: If you have a slot 9 somaria block, the hookshot will read data from the wrong place. In particular it will start at its own slot and then look down 1 slot each frame until reaching slot 0.
  1. Slot nine blocks
    1. Search index setting
      1. Lamp 3x
      1. Powder / fake powder
  1. Hookpush:
    1. Get a high value with correct direction in slot 0: beam or firerod or bomb
      1. Placing 2 bombs will put the 2nd in slot 0. This will get you up to 44 pixels of movement.
      1. Breaking a block and beaming will get you 4C in slot 0 which is a billion miles of movement.
      1. Breaking a block and firerrodding will get you a value corresponding to how long the fire travels before hitting, which can be quite high.
      1. Don't run afoul of stopping coords!
        1. Start your hookpush somewhere farther in the direction you want to go than the thing your slot 0 ancilla hit
    1. Use that data:
      1. Pause setup: Hook and pause/select buffer (skip intermediate slots)
      1. Fill slots: You need to fill all the slots between where the hookshot goes and slot 0 with stuff that won't stop it. Some setups:
       1. Slot 3 block (dust-block), dust-beam (slots 1 and 2 with dust and beam), then dust-hook (this puts beams in slots 0 and 1 and a hookshot in slot 2, obviating the need to skip any slots with 0s in them)
       1. Let a bomb blow up in slot 1, then dust-beam and you can hookshot. This feels more finicky, I haven't fully understood it yet.

1. Stuckpushes
  1. Less versatile than somaria hookpushes, but, of course, don't require somaria.
  1. Overview: If you get misslot a hook and then immediately regular-slot a hook, you can read hookpush by reading "wrong" data
  1. Stuck a push
    1. Set search index
    1. Shoot 3 arrows in a wall
    1. Slash and hold sword
    1. Place 2 bombs
    1. Hook, drop sword, hook again
  1. Unleash the push
    1. Place 2 bombs, then fill 2 more slots with things that aren't arrows. 2 lamps is the easiest way to do this
      1. you can try firerod + dust
      1. You can try south blue boom + dust, but if you somehow got a non-slot-4 stuck push this will fail and/or do something weird
  1. You can pick a different slot to read duration/direction information from by throwing the boomerang.
    1. The easy thing to do is throw boom east to pick slot 1, and then use a bomb, which can get you up to 44px of movement: just throw the boom east and then do the same setup from above, *but* make sure you unleash the hook towards the end of the bomb explosion
    1. This does make using the boom to fill a slot much more consistent, since you need to throw it anyway.
