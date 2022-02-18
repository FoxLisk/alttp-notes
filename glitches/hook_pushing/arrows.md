# Setting Directions With Arrows

## What gets set

Arrows set movement patterns according to the below table (note that movement is positive to the right and down, and negative to the left and up). This data is [stolen from Tojso](https://docs.google.com/spreadsheets/d/1s6qyLF2d3EzZotUeTg0lUzND0qYK49JZJzBJ13nQasc/edit#gid=914173735).

| Arrow direction | X movement pattern                     | Y movement pattern |
| --------------- | ------------------                     | ------------------ |
| Left            | 0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1  | -4,-4,-4,-4        |
| Up              | -6,-6,-6,-7                            | 0                  |
| Right           | 6,6,6,7                                | 4,4,4,4            |
| Down            | 7,7,7,7,8                              | 0                  |

## How to set it

This is going to cover only slot 0 arrows for use with slot 9 blocks, simply because that seems to be the only way to make this useful.

Since we're using a slot 9 block, the hookshot will be reading from slot 0. First we have to get an arrow in slot 0. This is a bit tricky because a slot 4 arrow will kill a slot 9 block (reasons unknown). A slot 4 block will *also* kill a slot 9 block (reasons unknown). So we have to avoid either of those going in slot 4. Here are some setups:

### Somaria only

You can place a slot 3 block & break it for 4 projectiles. This is enough to set a slot 0 arrow, but the timing is a little tight between the cane & bow animations; i.e. you need enough space for all 4 beams to travel pretty far.

### Blue boom

You can use the blue boom to fill slot 4. With a slot 3 block and a slot 4 boom, you can use either 3 arrows or 1 bomb + 2 arrows to get a slot 0 arrow. The extra bomb makes timing significantly more lenient on the arrow shots.

### Red Boom

Red boom fills up a lot of slots: 1 for itself + 6 sparkles. With the slot 9 block, that's 8 slots filled, so red boom + 2 arrows should work... but you run into sparkle despawn timing nonsense.

Red boom + spam arrows is the best play here. Placing a slot 3 block makes this fail a lot.

# How to use this

Once you have the desired direction set in slot 0, you can do a couple things.

The easiest thing to do is simply hookpush with this value, e.g. by using a select buffer or filling the slots or whatever. Arrows only get you 9 frames of movement but that is enough for some things, and they set high speed.

Another thing is to [set duration with a spin](spin_duration.md). This allows you to get huge hookpushes without the usual long-duration-setting items (beams, fire rod), and is the main way to take advantage of diagonal hookpushing.

## Cardinal arrow hookpushes

Here are some specific setups for cardinal movement. Some of these assume you understand how to set duration with a spin.

### West

Just shoot an arrow up and then do the rest. An arrow by itself gets you 56 pixels (c.f. bomb getting you 44), or you can do the spin stuff for tons.

### North

For a long north hookpush you can probably simply use a left arrow. The X speed is negligible. If it's somehow not negligible you just set your X stopping coord where you want it and you'll always trivially hit it.

If you aren't altering the duration, these will be shorter than setting distance/duration with a bomb.

### East

You can use a south arrow and do the rest normally since there is no Y velocity.

A south arrow by itself is actually already pretty good. You get 64 pixels of east movement; a bomb only gets you 44 pixels.

### South

This is a bit more complicated. We need to set stopping coordinates carefully if we don't want much diagonal movement.


A simple setup is to do a west spin on the same X coordinate that you hook from; this will stop you 19 pixels to the east of where you start because of the beautiful synchronicity of `0x6+0x6+0x6+0x7 = 0x19`. Make sure to start this high enough (~1.5 tiles) above where you are going to push from. You can activate hook from 1px left or right of your starting X position and still hit the wall.

You can also do a south spin 3 pixels left of where you hook from. This also has +/- 1 pixel of leeway.

