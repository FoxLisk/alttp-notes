this is probably not a good way to do this

$02D8[0x01] -   The index of the item you receive when you open a chest or pick up an item off the ground,                               or otherwise obtain the item (like Link getting the sword from his Uncle

blue boom 0C
bow 0B
gloves 1B
mearl 1F
hammer 09
mitts 1C
fire rod 07
hook 0A
somaria 15
ice rod 08
book 1D

-- quake 11 probably but this doesn't have 0x2e9 set to 01. it *does* have 0x5d set to 15 though...
-- flippers 1E same as quake

$02E9[0x01]   -   Item Receipt Method
                0 - Receiving item from an NPC or message
                1 - Receiving item from a chest
                2 - Receiving item that was spawned in the game by a  sprite
                3 - Receiving item that was spawned by a special object

$036C[0x01] -   Action index when interacting with tiles, like pots, rocks, or chests.
                0 - ???
                1 - Picks up a  pot or bush.                2
 - Starts dashing
                3 - Grabs a wall
                4 - Reads a sign.
                5 - Opens a chest.
                6 - ???
                7 - ???

$02DA[0x01] -   Flag indicating whether Link is in the pose used to hold an item or not.
                0 - no extra pose
		2 - holding up item with two hands pose (e.g. triforce)
		everything else - holding up item with one hand pose


I use this to check for getting ether:

$5D[0x01] - Link Handler or "State"
            0x0 - ground state
            0x1 - falling into a hole
            0x2 - recoil from hitting wall / enemies 
            0x3 - spin attacking
            0x4 - swimming
            0x5 - Turtle Rock platforms
            0x6 recoil again (other movement)
            0x7 - hit by Agahnim’s bug zapper
            0x8 - using ether medallion
            0x9 - using bombos medallion
            0xA - using quake medallion
            0xB - ???
            0xC - ???
            0xD - ???
            0xE - ???
            0xF - ??? 
            0x10 - ???
            0x11 - falling off a ledge
            0x12 - used when coming out of a dash by pressing a direction other than the dash direction
            0x13 - hookshot
            0x14 - magic mirror
            0x15 - holding up an item
            0x16 - asleep in his bed
            0x17 - permabunny
            0x18 - stuck under a heavy rock
            0x19 - Receiving Ether Medallion
            0x1A - Receiving Bombos Medallion
            0x1B - Opening Desert Palace
            0x1C - temporary bunny
            0x1D - Rolling back from Gargoyle gate or PullForRupees object
            0x1E - The actual spin attack motion.
