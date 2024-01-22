| Item  | Duration |
| ----  | -------- |
| Arrow           | FF if it doesn't hit anything, otherwise runs up to 08 after hitting a wall |
| Boomerang       | 00 while going out, 01 on the return, 04 if it doesnt spawn due to instantly tinking[0] |
| Hookshot        | Depends on distance, but not really usable afaik |
| Hookshot tink   | The tink from hitting a wall sets 04 in the slot below the hookshot without changing direction |
| Bomb            | 00 when placed, then during the explosion builds up to 0B |
| Powder          | Builds up to 09 |
| Fire rod        | Builds up 1 per frame as long as it's moving (it moves 4px/f) |
| Ice rod         | Oscillates 00-07 but seems to land at 06 if it goes a decent distance |
| Bombos          | 00 |
| Quake           | 37[1] |
| Lamp            | 00 |
| Hammer          | 01 |
| Shovel          | 01 |
| Flute           | 00[2] |
| Net             | N/A [3] |
| Book            | N/A |
| Bottle          | N/A |
| Somaria         | The block sets to 00. The beams also set 00. Breaking the block sets 01 very shortly then back to 00. |
| Byrna           | 04 |
| Mirror          | N/A |
| =====           | ===== |
| Slash - Fighter | N/A |
| Slash - Master+ | 04 |
| Beam            | 4C[4] |
| Spin            | 00 builds up to 04, then the ancilla gets replaced (2A becomes 2B) and the duration is set to 49, which drops ultimately to 03 |
| Splash          | 01 |
| Dust            | 06 | 
| Bonk            | FF |
| Item grab       | 1D |
| Fairy revival   | 00 in slot 0 (???) |


[0] Red boom spawns enough sparkles to go into front slots, and they oscillate 00-03  
[1] I don't know how to put this in slot 0  
[2] Does nothing in underworld (TODO: it probably doesn't do anything in dark world or when inactive, either)  
[3] The net is not and does not spawn an ancilla (?!)  
[4] When you slash with beams, the beam spawns first and thus occupies the higher slot
