Most (all?) ancillae set values when they're used that I call their "stopping coordinates." When you're hookpushing, your position is checked against these stopping coordinates every frame to decide if your movement should be stopped.

The relevant ancillae set these basically where they end up; e.g. bombs set their stopping coordinates where you place them, beams and fire rods where they terminate. [Spins are weird](spin_duration.md).

If you're ever +/- 1 pixel in the direction you're moving from your stopping coordinate, your hookpush stops. E.g. if you shoot an eastward beam in slot 0 to set hookpushing values, your stopping coordinate in the X direction is going to be where that wall is. If you pass over that wall and you hit either the exact X coordinate or are +/- 1 pixel from it, your hookpush will stop.

This is why when you're using beams to set up a hookpush, you want to beam something that will be behind you once you start the hookpush. That is, if you're pushing right past a vertical wall, you want your beam that sets up the slot to terminate to the left of you.


Anyway. The main points here are: 

1. Don't set your stopping coordinates in your path unless you specifically want to be stopped, and
2. If you set your stopping coordinate and then move (2+4n) px away from it, you won't get stopped; i.e. if you are on the grid, use a 4px/f ancilla (such as beams) to set up your hookpush, and then move 2px off the grid, you will fly past your stopping coordinate.


TODO: 

I haven't finished looking into this, but it seems like the stopping coordinate given in the practice hack hud extras for "X Coord" is actually somewhat offset from the effective stopping coord. Unclear how exactly this affects things. Same probably true of Y Coord.
