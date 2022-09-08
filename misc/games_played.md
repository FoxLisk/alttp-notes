When you beat the game, the end of the credits sequence displays a "Games Played" screen. What is this counting, and how exactly does it get counted?

# Very Short Overview

When you beat a dungeon (or obtain/rescue zelda), the total of (deaths + save&quits) since the last time you beat a dungeon (or obtained/rescued zelda) is saved as the number of "games played" in the dungeon you beat. There are some wrinkles to this.

---

# Relevant memory

* There is a counter at `$7E:F3FF` that I am going to call `GPNOW` (for Games Played Now). This tracks your running count of "Games Played".
* There is an array from `$7E:F3E3` to `$7E:F3FE` of games played per segment. Let's call this `GPSEGMENTS`.

# Counting Up

During the course of the game, whenever you save and quit from the select menu, or choose _any_ option from the death menu, `GPNOW` is incremented.

# Storing The Counter

There are several events that cause this number to be transferred elsewhere in memory. There are 3 slightly different versions of this.

## Normal Storing

The normal storage process goes like:

1. Write the value at `GPNOW` to the `GPSEGMENTS` array at the index corresponding to your dungeon ID
2. Set `GPNOW` to zero *unless* your dungeon ID is that of Agahnim's Tower, in which case leave `GPNOW` as is.

This process is triggered when any of the following events occur:

* Obtaining Zelda in her cell
* Delivering Zelda to the priest
* Collecting a dungeon prize (Pendant or Crystal) that warps you out of the dungeon
* Defeating either Agahnim

In normal gameplay this is straightforward: If you beat Misery Mire and then die three times before beating Turtle Rock, you'll have 3 "Games Played" in the Turtle Rock bucket. If you then go to Ganon's Tower and die two more times before defeating Agahnim 2, that will get you 2 games played in Gannon's Tower, with 2 Ns because spelling is hard.


## Agahnim's Tower State

As indicated above, if you're in Agahnim's Tower, the step of setting `GPNOW` to 0 is skipped. Additionally, at the end of the game, the Games Played for the AT segment are ignored: they're neither displayed in the credits nor counted up in the _Total Games Played_ tally. It's like the devs kept track of the counter but decided not to use it, so they hacked around it.

In practice this just means that triggering an event that would move `GPNOW` to a segment counter just doesn't matter if you're in AT state, although technically memory is getting written. This is kinda rare anyway since normal prizes don't drop in AT state.


## Credits

During the credits, the value of `GPNOW` is *added* to the _Gannon's Tower_ value. For example, if you die once in GT and a second time to Ganon, you should have 2 deaths under _Gannon's Tower_ in the credits.
