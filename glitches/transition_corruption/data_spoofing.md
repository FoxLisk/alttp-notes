Semantics note: "room" and "supertile" are interchangeable in this context. I have tried to mostly say "supertile" for explicitness reasons, but they mean the same thing.

# Data Spoofing

Room data lives in two places: there's some locations in RAM that get modified as you take actions in game such as opening chests and unlocking doors, which I will call the `active data` here. There's also data in SRAM, which is more canonical but updated only at specific times.

Transitioning between supertiles is one of those times. Supposing you transition from supertile A to B:

1. your room ID changes to B
2. Your current active room data is written to SRAM for room A
3. The room data for B is read from SRAM into active RAM
4. Room B is loaded (and you move into it)

When you do an STC, only the first 2 effects occur, which allows us to hang out in supertile A with our room ID set to that of supertile B. Then, when we transition (or s&q), our current active data will be written to the SRAM for supertile B. 

We can use this to our advantage for both purposes; that is to say, interacting with room A while having room B's ID set can be useful; and writing room state from A to room B can separately be useful. 

When it comes to chests, this is mostly useful for opening the wrong ones, and sometimes for re-closing chests.

When it comes to doors, this is mostly useful for opening doors in other rooms.

## An example

For simplicity, assume we start in supertile A and data spoof B, and that A and B each have 1 chest.

1. You are in supertile A, with a chest unopened
2. Spoof towards B
   1. First, this writes down our active room data to SRAM for A
   2. Now the chest is still closed (regardless of the chest's state in B)
   3. And our Room ID is now B
3. Open the chest. This looks up the contents of the chest in room B and gives us that. The chest is now open
4. Leave the room
   1. Now, our room state is written to supertile B. This will (perhaps among other things) open the chest in B.
   2. This will *not* open the chest in A; you can, for example, mirror out and redo the STC to get the chest again (thus duplicating, or "duping", its contents)

This has done two things for us: we got the contents of a chest in room B without having to go there, and also we opened a chest in room B without having to go there.

Opening chests in the wrong room isn't really useful, but opening *doors* in the wrong room can be. For example, if you bomb the exit in laser bridge and then spoof data northward and mirror out, you will end up writing the "door open" data from laser bridge down to the "room above laser bridge" room ID, thus unlocking the door without a key.

As kan puts it:

> if you had no chests opened in room A and spoof to room B then leave immediately, room B will have the exact same flags as room A


# How To

I think basically this happens when a supertile transition gets interrupted. I know of two ways to do this:

## STC

Non-west Somaria Transition Corruptions cause data spoofing. This has something to do with them sort of triggering a sub & a supertile transition at the same time, meaning we always get the effects of a supertile transition, and it gets interrupted.

I don't know what's going on with west STCs yet.

## YBA

Supertile YBAs also cause data spoofing. Subtile YBAs don't.

# Further reading


* https://alttp-wiki.net/index.php/Data_spoofing
* http://alttp.mymm1.com/wiki/Yuzuhara%27s_Bottle_Adventure#Supertile_YBA


