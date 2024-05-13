# How to stuckpush:

## Get a "stuck hook" in slot 0-4

Technically, this rquires changing Link's state while the hookshot is extending towards a hookable object. In practice, this means the following:

1. Fill slots 0-4 (2 bombs and 3 arrows is an easy way to do this, but there are plenty of others)
1. Put a replaceable ancilla in slots 5-9. An easy way to do this is have your sword held out (hookshots like eating sparkles)
1. Make sure your search index is >= 5
   [Search index info from Glan](/glitches/ancillae/setting_search_index.md)
1. Use the hook in range of a hookable
   * This hook will go in slots 5-9, eating the above ancilla. This is probably search-index dependent in a way I don't yet grok
1. _Before that hook connects_, use the hook again, but in a way that gets it to spawn in slots 0-4. An easy way to do this is to have an arrow in a 0-4 slot and release your sword after the first hook, which will allow the second hook to replace the arrow.

If this works, there will be a hookshot sprite on screen extending from where you were towards whatever you were hooking. It's pretty obvious.

## Pick and setup the slot you'd like to read for stuckpushing

I'm a little fuzzy on the technical details at this point. But we have a couple things now:

1. A "stuck" hookshot somewhere in slots 0-4 that's ready to pounce. Let's call this $STUCK_SLOT
1. A value in $039D (the "hookslot") that tells the game what slot to read data from when unleashing the above hookshot. This will start by pointing at the hookshot we just got stuck; i.e. the value at $039D = $STUCK_SLOT

Our next step is going to be [unleashing that hookshot](#unleash-the-stuck-hookshot). If we don't do any further manipulations, what will happen is that we get the direction and duration that the stuck hookshot was supposed to give us. This can be quite useful; for example you can stuckpush easily from Hope Room to Tile Room in GT by getting a hook to the topright pot stuck and then unleashing it.

You can, however, read different data for the direction/duration instead, which can also be quite useful! Throwing a boomerang sets the slot that we're going to read data from according to [this table](boomerang_slot.md) i.e. it sets $039D (the hookslot) to the given value. So if you throw a boomerang west, you set the slot to 2; if you got, say, a sword beam in there, you'd get a very long hookpush.

This is tricky to do in general; or, anyway, I'm not good at it. It runs into some constraints: first of all, it's hard to know exactly which slot your stuckshot is in, which can make selecting a slot difficult. I think normally it will go in slot 4 (since that's the highest-slotted arrow it should get replaced) but I have seen it in other slots. Secondly, you need good data in the slot *and* the slot to be filled at the same time; a lot of the use of hookpushing is to go, say, left through a wall, which makes it hard to create an ancilla that has the left direction and lasts long enough to still prevent the next hookshot from spawning.

### Using Bombs

However, there is one very easy and very useful thing we can use to take advantage of this: bombs go in slots 1 and 0 automatically, set direction & duration, and don't hit walls and despawn. They only set 0x0B for duration, which is 11 frames or 44 pixels of movement, which isn't enough for everything but can be quite useful.

The way we do this is, once we have a stuck hookpush, we throw a boomerang to the east to set our hookslot to 1. Then we place a bomb facing the direction we would like to push in. Then we [unleash](#unleash-the-stuck-hookshot) while the bomb animation is near its end (watch the "extension" field in the practice hack to get a feel for the timing).

The easiest method (IMO) is:

1. throw boom east
2. place 2 bombs
3. when the explosion is midway, lamp 2x and then use hookshot

You can also time the boom throw to fill a slot if you prefer (and if the relevant walls cooperate).

## Unleash the stuck hookshot

This requires using the hookshot while it can't spawn in *any* slot. An easy way to do this is fill slots 0-4 with non-replaceable ancilla (things that aren't arrows, generally; bombs, boomerang, and lamp are all easy and useful) and not having any sparkles in higher slots. You can also set the search index low and get away with arrows and bombs (with a search index of 2 or lower the hookpush will give up before noticing it can replace a slot 2-4 arrow).

This will push you in the direction and for the duration chosen above.


(all info credit to Tojso, vZakat, and Glan)


# More Setups

## Using 0A Hookslot

Throwing the boom NW sets the hookslot to 0A. 0A is a greater slot than we can put ancilla into, but, per Tojso:

    having a bomb in slot 0 constantly sets the extension for slot A to 2 (then is decremented to 1 by the hookshot via pushing), so you basically move until the bomb explodes or you hit a supertile transition.
    seems like direction of slot A is determined by the layer of the ancilla in slot 0. so pushing with slot 0 on the lower layer will go south, pushing with slot 0 on the upper layer will go north (edited)
    so, for most purposes, slot A direction will be north

This is pretty easy. Just get a push stuck, then throw the boom NW and unleash it.

# Double-Misslotted Stuckpushes

Disclaimer - I understand this even less than the above. See [Tojso's explanation](#tojso-on-double-misslots).

In brief: If you misslot 2 hookshots in a particular way, you can get the activation effect of the second one easily.

The easiest setup I know requires silver arrows (because it continuously generates sparkles):

- 2 bombs
- 2 arrows in wall
- 1 *silver* arrow on screen

[Here is a video of this](double_misslot_silvers.mp4)

Hookshot a hookable object twice quickly. The first one will go in slot 9, and the second one will go in slot 8. If you succeeded, your hookslot will be 9. If you failed, it's usually (IME - YMMV) because the hookshots were too far apart; you can tell this happened when your hookslot is 8 and your stuck push is already touching the object you targeted.

That's the hard part - the benefit is that unleashing the hookpush is much easier. Just use another hookshot and make sure it doesn't "complete" (i.e. hit a hookable object or hit a non-hookable and return to you) too quickly. This will get you the movement from the stuck push.

A tricker setup that uses ice rod instead of silvers:

- 2 arrows in wall
= Sword out
- 2 bombs
- Ice rod

now you have to pause briefly, something to do with get the sparkles to line up, and then hook twice.

[Here is a video of this](double_misslot_icerod.mp4)

N.B. I can misslot hooks in a way that looks like this but fails to work by using red boom for sparkles. Have yet to diagnose why that one fails.

## Stucking the activating push

If the last hook use with a double-misslot hits a hookable object (but still gets you the hookpush; i.e. it doesn't hit until the stuck push has reached its target and is pushing you), it too will get stuck. This can be used like a normal stuckpush; i.e. you can fill slots and unleash it.



-----

## Some discord logs for posterity

Tojso: Somaria-less Hookpushing is really just 2 things:

1) Get a stuck hook in slots 0-4
2) Ancilla overload a hook

To get a stuck hook, you simply need to change link's state while the hookshot is extending toward a hookable object. There are a few ways to do this.

Easiest is known as hookshopping, where you purchase a shop item while the hook is extending. This is limited to shops, so not very useful in rando, but useful for getting other variations down. https://twitter.com/linus0505/status/1419156698367856643

Most commonly, you'll use a misslotted hook (any slot 5-9), then a regular hook (any slot 0-4) immediately after at the same object. The misslotted hook will hit the hookable object first, which changes Link's state before the regular hook reaches its target. There is some fuzzyness here as sometimes the regular hook will also retract and I'm not 100% sure what causes it.

Lastly, there is potential to use Lonk with a regular hook as you can move a little while using items with Lonk.

[4:53 PM] Tojso: The most important variable from here is $39D (view this in prachack using the Hookslot for one of the Sentries in the HUD extras). When a hookshot is thrown or hits a hookable object, the slot of the hookshot will be written to $39D. 

To activate the hookpush, we need to use the hookshot, but a newly spawned hookshot will just overwrite $39D with whatever slot it's occupying. To get around this, we use ancilla overload (think splash-delete). We use the hookshot while slots 0-4 are filled, thus a new one doesn't actually spawn, so the game just uses whatever was left over from $39D and the associated variables from that slot.

You do need to be a bit careful, though. If your index is 0 before throwing the last hook, it can replace particles in slots 1-3, just like shooting arrows does.

Ultimately, this version of hookpushing is more a like a translation of an existing hook you could do in the supertile.

[4:53 PM] Tojso: However, we can use different distances and directions by modifying $39D before throwing the last hook. $39D is also used by the boomerang, depending on the direction you throw it: (8 for N, 9 for NE, 1 for E, 5 for SE, 4 for S, 6 for SW, 2 for W, and A for NW).


---

 Tojso: using the boomerang allows you to use stuff from a slot other than the one for your stuck hook. so in the powder-pushing example, I misslotted a beam to slot 5 while throwing the boomerang to set $39D to 5. so, when I ancilla overload the hook, the game looks at stuff only from slot 5.  
[5:14 PM] FoxLisk: yeah  
[5:14 PM] Tojso: it can be tricky to get the timings down when using boomerang to change $39D to something within 0-4  
[5:14 PM] FoxLisk: so when we shoot the hookshot that doesn't actually spawn  
[5:15 PM] FoxLisk: it looks at whatever the ancilla index indicated by $39D is  
[5:15 PM] FoxLisk: and looks at what the prachack calls the "extension" value  
[5:15 PM] FoxLisk: and hookpushes us for that many frames  
[5:15 PM] FoxLisk: right? (direction is still a mystery to me)  
[5:15 PM] Tojso: correct, direction is also taken from the same slot from $39D  

---

[11:00 PM] FoxLisk: okay back on stuckpushing (is that what we're calling it?)

for the last hook usage, the one that's supposed to activate the stuck hookshot, is it correct to say: that hook needs to not spawn, which means you need to avoid having sparkles that it can replace? (modulo some search index stuff that i dont understand well)

i.e. using arrows and bombs to fill up slots 0-4 is fine for the first step, because you can stick a sparkle in 5-9 and it will eat that sparkle (and then something else about your setup causes the 2nd use to spawn in 0-4 normally)

but using arrows and bombs to fill up slots 0-4 for the last hook won't work, because either it will replace an arrow and spawn in 0-4, or if you try to avoid that by sticking a sparkle in 5-9 it will replace that sparkle and still spawn and in neither case do you get the stuckpush effect
[11:10 PM] Glan: Yes that is correct, it must not be able to replace anything in any slot
[11:11 PM] Glan: You can use bombs and arrows, but you have to manip the index to 2
[11:12 PM] Glan: However you only have to fill 2 slots in addition to the bombs, so boots dust + something else works easily if you can do that
[11:13 PM] Glan: (because the hookshot is still taking up one)
[11:13 PM] Glan: Even bombs + 2 lamp flames should work although you might need to buffer it or something
[11:20 PM] FoxLisk: yeah i did bombs + 2 lamp flames for one of the no EG routes lol
[11:21 PM] FoxLisk: okay great
[11:21 PM] FoxLisk: so if you do bombs + arrows [+hookshot] and set the index to 2, would you need the hookshot in slot 2?
[11:21 PM] FoxLisk: also how do you set index to 2? i only know how to set it high w/ lamp
[11:22 PM] FoxLisk: also, if the search index is very low, you still need the higher slots filled? like, it checks slots 0-4 and if all of them are full, then the search index comes into play to find something it can replace?
[11:24 PM] FoxLisk: toj said the other day 

You do need to be a bit careful, though. If your index is 0 before throwing the last hook, it can replace particles in slots 1-3, just like shooting arrows does.

so that seems relevant... my search index understanding is abysmal twinmo1Sad
[11:26 PM] Glan: Yea the search index only matters when the slots are full

#### Tojso on double misslots

I hadn't really messed with multiple misslotted hooks before, but now that I've seen an easy repeatable setup, I understand how it works. misslotted hooks do not move link at all. movement from misslotted hooks only occurs because a non-misslotted hook exists. from my earlier text wall about stuck hooks:

When a hookshot is thrown or hits a hookable object, the slot of [that] hookshot will be written to $39D. 


the push happens solely because of the 2nd misslotted hook. when you throw 2 misslotted hooks, the first hits a hookable object before the 2nd, which stops the 2nd before it hits the hookable object. when you throw a normal hook after that, the other hooks re-activate.

if the normal hook hits a hookable object first or fully retracts first, the push won't happen, and you'd have to start the setup from the beginning again.

however, if the 2nd misslotted hook hits a hookable object first, then $39D is set to the slot of that hook. additionally, because the normal hook exists, the game assumes that the normal hook is responsible for hitting the hookable object, so the push activates and link moves. however, because $39D is equal to the slot of the 2nd hook, the game uses those variables instead of the ones from the normal hook. it's not possible to use variables other than those from the slot of the 2nd misslotted hook here.

if the normal hook would hit a hookable object after this, it gets stuck, allowing another push, one that can be modified using boomerangs.
