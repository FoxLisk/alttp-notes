Most (all?) ancillae set values when they're used called their "terminator"s (i used to use the term "stopping coordinates.") When you're hookpushing, your position is checked against these terminators every frame to decide if your movement should be stopped.

The relevant ancillae set these basically where they end up; e.g. bombs set their terminators where you place them, beams and fire rods where they terminate. [Spins are weird](spin_duration.md).

If you're ever +/- 1 pixel in the direction you're moving from a terminator, your hookpush stops. E.g. if you shoot an eastward beam in slot 0 to set hookpushing values, your terminator in the X direction is going to be where that wall is. If you pass over that wall and you hit either the exact X coordinate or are +/- 1 pixel from it, your hookpush will stop.

This is why when you're using beams to set up a hookpush, you want to beam something that will be behind you once you start the hookpush. That is, if you're pushing rightward past a vertical wall, you want your beam that sets up the slot to terminate to the left of you.


Anyway. The main points here are: 

1. Don't set your terminators in your path unless you specifically want to be stopped, and
2. If you set your terminator and then move (2+4n) px away from it, you won't get stopped; i.e. if you are on the grid, use a 4px/f ancilla (such as beams) to set up your hookpush, and then move 2px off the grid, you will fly past your terminator.


# Directionality

Because Link is not a point mass, the actual place link gets stopped is based on an offset from the terminator.

This is mostly exactly what you'd expect: Link stops at the point where his body hits the thing, like he does when you're hooking a pot. It's a little less obvious when putting these together in game, though.

## Left

Link will stop no farther left than 0x3 pixels to the right of the terminator

## Up

Link will stop no higher than 0x7 pixels below the terminator

## Right

Link will stop no farther right than 0xB pixels to the left of the terminator


## Down

Link will stop no lower than 0xF pixels above the terminator


# Terminator Offsets

Here are how some items set terminators.

## Sword Beams

Sword beams travel at 4 px/f and start on Link, so generally they set terminators of whatever they hit, on the grid centered at where you shot them.

Where they actually set Link to stop isn't necessarily visually exactly where you'd expect, but it's pretty close.

## Fire Rod

Same as sword beams, but goes 4px farther in whatever direction you shoot it.

## Bombs

| Link facing | Stopping X | Stopping Y |
| ----------- | ---------- | ---------- | 
| Left        | X - 0x06   | Y + 0x0C   |
| Up          | X + 0x08   | Y + 0x04   |
| Right       | X + 0x16   | Y + 0x0C   |
| Down        | X + 0x08   | Y + 0x18   |

so to the left and right you can get full distance by staying "on-grid" with the bomb, if for some reason you can't get otherwise good terminators

## Arrows

Arrows unfortunately move at 3px/f which makes this kind of a mess. Fortunately, [arrow velocity](arrows.md) is so weird that you need to make totally different assumptions than just "am I on grid?" so this doesn't seem to matter a lot? Maybe I'll find a reason to think it matters later.
