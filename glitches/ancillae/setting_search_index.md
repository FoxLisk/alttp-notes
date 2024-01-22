# Setting the Search Index

## Slot 2 Items

Certain ancillae, when spawned into slot 2, will directly write values to the search index.

### Ice Rod

A slot 2 ice rod sets search index to 0.

### Lamp

A slot 2 lamp sets the search index to a different value depending on what direction Link is facing:

| Facing | Search index |
| ------ | ------------ |
| Left   | `$10`        |
| Up     | `$0D`        |
| Right  | `$07`        |
| Down   | `$0A`        |

### Powder

Powder behaves as follows. Starting from the frame that the chime plays (which is one frame before the powder sprinkle animation starts displaying):

```
Frame  1: Set the search index based on the direction Link is facing, to the same value as the lamp would.
Frame  2: Increment search index
Frame  3: Increment search index
Frame  4:
Frame  5: Set search index to 0
Frame  6: Increment
Frame  7: Increment
Frame  8: Increment
Frame  9: Increment
Frame 10: Increment
Frame 11: Increment
```

Thus ending up with a value of 6, regardless of facing direction. It's worth noting here that you can interrupt this animation with a S&Q or, in the case of fake powder, a screen transition, to end up on values other than 6.

## Fairy Revival

Any fairy revival, including from a deathhole, sets the search index to 6.

## See also

Since Powder sets the search index, fake powder can be very useful. Since you can move during fake powder, you can find setups to activate fake powder next to a screen transition and have the transition stop the powder animation at a point with a high index set.

See [/glitches/fake_items.md](Fake Items) for more info, including ledgepog setups.
