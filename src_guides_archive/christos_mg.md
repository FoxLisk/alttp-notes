Thanks to SuperSkuj for this work.

================================================================================================
Major Glitches
================================================================================================

These are ordered from most severe to least severe.

1. Exploration Glitch (EG)
Placing the player sprite on the incorrect layer of the game, or otherwise bypassing
obstacles through layer manipulation. Can be activated with normal OOB glitches or
underworld YBAs. EG is only possible in the underworld.

2. Door Glitches (DG)
Three subsets of glitches which are accomplished by bypassing or corrupting a door
transition on the underworld. This can be accomplished with a YBA or through use of the
Cane of Somaria, bombs, pixelporting (in a TAS), and probably more ways.

2a. Superskuj Door Juke (SDJ) AKA Data Swapping
A glitch which swaps data between two rooms, or overwrites completion flags in
a room. This can: cause chest contents to change, refill chests, regenerate
keys, and toggle the "holes hurt players" flag which allows some Wrong Warps.

2b. Door Warp
A glitch which corrupts a door transition, causing it to transport the
player multiple rooms instead of just one, or to transport the player in the
wrong direction.

2c. Underworld Fake Flute
See: 6. Fake Flute

3. Wrong Warp (WW)
Using a hole in a room to transfer the player to a room which is not intended to be
accessed from the former. Some holes can accomplish this by default, such as Ganonpot
or the Turtle Rock lava dive, others require an SDJ to change the behavior of the
hole. As of now Door Glitches are required to perform any Wrong Warps, but they aren't
considered a subset of Door Glitches, instead they have their own classification.

4. Out of Bounds (OOB)
Specific manipulation of the game engine's collision detection to bypass an obstacle,
including clipping, teleports and mirror jumps. This applies to glitches on the overworld
and underworld, and while there is a distinction between EG and OOB, some applications may
lead to EG. OOB doesn't give you freedom of movement in the underworld, that is EG.

5. Screen Transition Gitches (Overworld)
Two subsets of glitches which corrupt the function of a screen transition on the
overworld.

5a. Mirror Warping
Activating the mirror on the same frame as a screen transition to warp across
a screen.

5b. YBA
A blue potion YBA activates a fake flute (see: Fake Flute).
Using a green or red potion to activate a YBA on the overworld corrupts the
screen's data, allowing the player to bypass some obstacles.

6. Fake Flute
The flute menu can be accessed with a YBA on the overworld or underworld, and are
classified separately:

6a. Overworld Fake Flute
Achieved by performing a blue potion YBA on the overworld. Calls a functioning
flute menu, with the exception that transportation from the Dark World
will result in the player landing in the Fake Light World.

6b. Underworld Fake Flute
Achieved with a green YBA in an inter-tile door or a blue YBA in an intra-tile
door. This calls a flute menu which does not function properly. This is not
considered EG unless the player moves far enough from the landing zone to
reload underworld tiles.

================================================================================================
Appendix:
================================================================================================

Yuzuhara's Bottle Adventure (YBA) - Useage of a potion on the same frame as a screen or door
transition. This has a wide variety of effects, and thus is not considered a classification of
glitches on its own but rather a technique to accomplish these glitches.

Camera Offset Glitch - This is an illusion where the player appears to bypass obstacles on the
overworld because the camera is displaying an incorrect location. This can be caused by
teleporting/jumping through a screen transition, or with the Fake Flippers "softlock" condition.
In this state the player usually won't interact with sprites, but will interact with tiles.
