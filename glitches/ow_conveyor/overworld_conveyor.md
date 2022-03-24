# What

You can get the conveyor state on the overworld by using misslotting.

If you walk into a diagonal wall while in conveyor state on the overworld you can clip through *everything* and go lots of cool places.

# Explanation

Firstly: the memory location `$3F3` indicates whether Link is currently under the influence of a conveyor:

* if it's `0x00`, Link is not on a conveyor
* if it's `0x01`, Link is on a north conveyor
* if it's `0x02`, Link is on a south conveyor


Secondly, When you are holding an ancilla and take damage, that ancilla becomes responsible for the following process:

1. set a value in memory to `0x01`
2. 15 frames later, set that value to `0x02`
3. 23 frames later (38 total), set that value to `0x00`

The address that it writes to is based on its slot; in particular, if it's in slot 9 it writes to the magic conveyor address.

This is all well and good, but we have to do something to interrupt the part where the value gets set back to `0x00` if we want to do anything useful. As it turns out, an exploding bomb abdicates its duty and stops updating this memory address! Thus, we can pick up a slot 9 bomb and then get hit the appropriate number of frames before it explodes, we can get the conveyor state permanently.

The easy way to do this is, basically

1. place a front-slot bomb
2. wait if you want a down conveyor
3. place a slot 9 bomb
4. pick up that bomb

This turns out to be quite manageable to execute. Some specific setups are listed below, but the general pattern is:

* for upward conveyor, fill up 4 slots then lay 2 bombs back to back
* for downward conveyor, place a bomb before filling up all the slots, then use the time it takes to fill the last slot(s) to introduce the necessary delay before placing the slot 9

e.g. for upward conveyor with Somaria, you can break a block (4 slots) and then double-tap `Y`, but for downward conveyor you'd want to place the first bomb before breaking the block.

You'll always pick up the first bomb you placed, so if you place them both in the same spot, pick up and throw the first one and then pick up the second one.


See [more words from Tojso](#notes) for some more technical details.

# setups

These assume that you can get a high index & a sparkle in slot 9 and that you will be careful to pick up the slot 9 bomb. Hopefully you can extrapolate from these examples as necessary.

## Somaria

### Upward

1. block
2. break block
3. bomb 1
4. bomb 2

### Downward

1. block
2. bomb 1
3. break block
4. bomb 2

[clip](conveyor_downward_somaria.mp4)

## Bow

### Upward

1. 3 arrows in wall
2. Dust
3. Bomb 1
4. Bomb 2 *before the dust is gone*

This is a very tight window. Some people like to do an itemdash for the first bomb, but I find that much harder than a quick sequence of `A Y Y` taps.

### Downward

1. 3 arrows in wall
2. Bomb 1
3. Dust
4. Bomb 2

This is a lot more lenient than the upward setup.

---

## notes

From Tojso. [Much more here](https://discord.com/channels/307860211333595146/741638618090569738/956387095851708417):

    I started messing with a forgotten application of misslotting: OW Conveyor. it revolves around the address $3F3. when this is 0x00, no additional movement is applied to Link. when it is nonzero, a constant movement is applied Link. 0x01 for normal north conveyor, 0x02 for south, 0x03 for west, 0x04 for east. 
    to get a nonzero $3F3 with misslotting, you simply need to take damage while holding a slot 9 ancilla (somaria block or bomb). this starts a 0x01 on the first frame of damage, then increments to 0x02 15 frames later, then 10 frames later you regain control of link, then 13 frames later it goes back to 0x00. if we can interrupt this count up to 0x02, then we keep the conveyor state beyond the 37 frames that it lasts.
    while you are holding an ancilla, if you take damage you then drop said ancilla. this causes the address $3EA,x to update (this means $3EA is for slot 0, then you just add x to that to get the address for slot x. for slot 9, this would be $3F3). I think it helps with the bounces that the ancilla does as it drops to the ground. however, this only applies to taking damage while holding it, not while throwing it.
