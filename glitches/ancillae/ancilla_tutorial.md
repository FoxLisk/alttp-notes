# Ancilla Manipulation Tutorial

This is an attempt to take you through ancilla manipulation in a somewhat breezy way, with worked examples and applications.

# Slots

Ancilla spawn into ten "slots", which we number 0-9. The first 5 slots (0-4) are called "front slots," and the rest are called "back slots."

# Prachack Settings

Note that these are for v14 only. v13 is different and much less full-featured.

In the prachack "HUD Extras" menu, set the following:

Set one of the Sentries to `Anc index` (this is the search index, we'll get to that soon)

* Line 1: Ancilla 0-4
* Line 2: Ancilla 5-9
* Ancilla prop 1: ID
* Ancilla prop 2: ID

Once we get to hookpushing, you should also add 

* Line 3: Ancilla 0-4
* Ancilla prop 3: Extension

But I find 3 lines quite noisy if I don't need them.

# Spawning Ancillae

When you do something that generates an ancilla, the process for spawning it goes like this:

1. If we already have enough of this kind of ancilla (i.e. we try to throw a second boom), do nothing
1. Look for an open ancilla slot, starting from slot 4; spawn into one if found
    1. Bombs start looking at slot 1
    1. Sparkles start looking at slot 9
1. Look for a replaceable ancilla, and spawn into its slot if we find one.

How many is "enough" of a particular kind of ancilla? Depends on the ancilla - you can only spawn 1 boomerang, but you can spawn 2 fire rods, for example. [You can see all the quotas here](ancilla_quotas.md).

## Easy cases

First let's look at some trivial examples: if you shoot an arrow with nothing else going on, you'll see it go into slot 4. You can tell this from the prachack HUD because the last slot on row 1 will light up with `09`, which is the ID of the arrow ancilla. When it hits a wall, it will change to `0A`, which is the ID for the "arrow in wall" ancilla.

If you shoot another arrow while that one's in the wall, the 2nd arrow will go into slot 3. If you shoot a 3rd, it will go into slot 2. If you shoot more, things get complicated, so let's wait on that for a moment.

If you were to start fresh and first lay a somaria block, that would go in slot 4. Since somaria blocks persist, when you go to shoot an arrow, it will have to spawn in slot 3, and subsequent arrows will go into slots 2 and 1.

---

Some ancillae behave slightly differently. If you lay bombs, they want to go into slot 1. So if you start fresh and lay a bomb, it goes into slot 1, and the next bomb will go into slot 2.

Some things generate sparkles. These sparkles want to go into slot 9. If you hold your sword out, you'll see it generate a series of sparkles starting in slot 9. These sword sparkles die out at a rate that causes them to generally fill slots 9, 8, and 7. If you throw a red boomerang, you'll see up to 6 sparkles spawn, filling slots 9, 8, 7, 6, 5 and 3 (the boomerang itself goes in slot 4).

## Slots are full

If there's no empty slots, the ancilla that's trying to spawn begins a **replacement** process, where it tries to find a "replaceable" ancilla and take its slot. I'm not going into extreme detail here; for any details you find this document to be light on, see [the codex](ancilla_spawning.md).

The replacement process looks basically this:

1. First, we pick a slot to start looking at
1. Then, we look at that slot. If it's a replaceable ancilla, we replace it. Otherwise we move down a slot and try again
1. If we run out of slots to check, we don't spawn the ancilla at all.
1. At the end of this process, the search index is the slot of the replaced ancilla, or 0 if nothing was found to replace.

The way we pick a slot to start with is related to what we call the **search index**. If the search index is already set, we decrement it and use that value; otherwise we use the value of the ancilla's quota.

### NOTE

Arrow replacement only occurs if there are **exactly** 3 arrows in walls when the arrow is shot, only replaces arrows in walls, and if the search index is lower than the slot of the lowest arrow in wall, it will loop back around to slot 4 and find the highest slot one. Luckily, knowing this rarely actually comes up.

# Examples

## Example: Fake Flippers

Let's look at everyone's favourite example, splashless fake flippers. The way this trick works is that if you enter the water without spawning the splash ancilla, you get to swim as if you had flippers.

I'm going to explain this so that you actually understand what's going on, and you know when it does and doesn't work properly.

How can we get this to happen? Let's load up the `Ice Palace -> Zora's Domain` preset and go to the prachack menu `Game State -> Remove Sprites` to get everything out of our way.

First up, let's make sure our search index is 0. Yours may already be (you should be able to see the sentry for this). If it's not, an easy way to set it to 0 is to place a bomb on land, and then walk to deep water and spam bombs (you may need to give yourself extra bombs).

Next we'll need all 5 slots filled. The classic way to do this is with 2 bombs and 3 arrows, which will lead to these slots:

    bomb bomb arrow arrow arrow

When we try to jump into the water with this setup, the game tries to spawn a splash ancilla. The way this process goes is as follows:

1. Are there too many splashes already?
    * No, go ahead and try to spawn
1. Is there an open slot available?
    * No, try to do a replacement
1. Is the search index 0?
    * Yes. The splash's quota is 1, so we set the search index to 2
1. Is there a replaceable ancilla in a slot lower than the search index?
    * No; slots 0 and 1 have bombs in them, which are not replaceable.

So we give up and don't spawn the splash, and are able to swim without flippers.

What would happen if our search index were higher? If the search index is at least 3, the splash will find a replaceable ancilla (in slot 2), and we will not be able to swim.

We can easily test this by spamming lamp and repeating the setup - spamming lamp sets your search index quite high. If you do this, you'll see the splash go into slot 4 instead, and you will be kicked out of the water.

[See this demonstrated here](fake_flippers_demo.mp4)

## Example: Repeated arrow firing

Many people, when they do the 2 bombs + 3 arrows fake flipper setup and it fails, get confused and end up hearing the following foolproof steps:

1. Spam lamp
1. Fire six arrows into the wall
1. Place 2 bombs
1. Now the splashless setup will succeed

Why does this work? Well let's go through it.

First, spamming lamp sets our search index high. (We'll get to the details in a moment, but it always sets it to be >5).

Then we fire six arrows into the wall. Note that arrows behave somewhat differently than other ancillae when trying to do a replacement, although the search index behaviour is pretty similar. So what happens here?

1. The first three arrows get fired as normal, filling slots 4, 3, and 2.
1. The fourth arrow wants to do a replacement. This is because when you try to shoot your bow and there's already 3 arrows already present, it tries to do a replacement rather than either giving up or picking an empty slot (arrows are weird)
    1. Because the search index is >5, the first replaceable ancilla it finds is the arrow in slot 4
        1. It replaces this arrow and leaves the search index set to 4
1. The fifth arrow wants to do a replacement
    1. Because the search index is 4, the first replaceable ancilla it finds is in slot 3.
        1. It replaces this arrow and leaves the search index set to 3
1. The sixth arrow wants to do a replacement, yada yada, search index set to 2

So now we have 2 bombs and 3 arrows in our front slots, with search index 2. Now when we jump in the water, our splash will only look at slots <2 for replaceable ancillae, and won't find any (bombs aren't replaceable), and we get to keep swimming.

# Misslotting

Okay, the half of you who weren't here because you wanted to know how fake flippers works were waiting for this section - this is the background knowledge for getting to understand hookpushing.

We just went over how to exploit the ancilla spawning process by _preventing_ an ancilla (the splash) from spawning. Another way of exploiting it - a much more powerful way! - is by spawning ancillae into slots they're not supposed to be in.

Let's look at some ways to spawn a slot 9 Somaria block, which is one of the most powerful uses of this tech (although I'm not covering applications - [some of that is written up in the hookpushing section, though](/glitches/hook_pushing).)

We already have the knowledge required to do this! If we have full front slots, a high search index (anything >5 counts, although in practice we usually want >9), and a replaceable ancilla, we can spawn an ancilla into a back slot.

How do we set a high index? The easiest way is by spamming lamp while facing a direction other than right - [more details here](setting_search_index.md#lamp).

So, with our high index set, we need to accomplish the following:

1. Slots 0-4 occupied
1. a replaceable ancilla in a high slot

## Example: Bombs + Silvers

It turns out that a good way to do this is using silver arrows, which generate a large number of sparkles. So let's do this:

1. Lay 2 bombs (they go in slots 1 and 0)
1. Shoot 2 silvers into the wall (slots 4 and 3)
1. Shoot a silver arrow into open space
    * the arrow goes into slot 2, filling the front slots
    * the sparkles should fill all of the back slots

Then we can place, for example, a Somaria block, which will replace the sparkle in slot 9.

[Here is a video of me misslotting some ancillae with this method](misslotting_bomb_silvers.mp4).

## Example: Bombs, Arrows, Sword sparkles

Another good way of doing this is holding our sword out to generate sparkles. This has some inconsistency to it because of the way sparkles work - they are constantly spawning, dying, leaving an empty slot for a couple frames, and respawning. However with some practice you should be able to get a rhythm down for it.

This time we're going to hold our sword out, and then place 2 bombs and shoot 3 arrows in the wall. Shooting the bow interrupts sparkle generation, so if you have a consistent timing between the last arrow input and the Y press for the somaria block, you should be able to get consistent slot 9 blocks.

[Here is a video example](misslotting_bomb_arrow_sword.mp4).

# Outro

There's a staggering number of ways to combine items to cause various misslots or stop items from spawning. We only talked about a couple examples here, but hopefully this is enough information to understand other setups and maybe start thinking about your own!
