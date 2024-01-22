# What is an ancilla?

Ancillae (pronounced an-silly) are things that Link creates[0], mostly by using items. Using an item that spawns a visual effect in the world will generally create at least one ancilla, as will slashing your sword, dashing, being fairy revived, etc. We'll get to the important ones in a bit.

# Ancilla "Slots"

There are 10 "slots" in memory into which ancillae can spawn[1]. These are generally grouped in two halves; the "front slots" and the "back slots." These are numbered starting from 0, so we have

    Front slots
    0 1 2 3 4

    Back slots
    5 6 7 8 9

# The Ancilla Tutorial

I made a [tutorial](ancilla_tutorial.md) for a hopefully fairly gentle introduction to ancilla manipulation.

# How do ancillae spawn?

See [the ancilla spawning codex](ancilla_spawning.md) for the gory details. Be warned that this is a pretty dry and technical document, but it's good for learning any details you may need.

---

[0] Mostly - fairy revives don't really spawn an ancilla normally but are treated like ancillae otherwise.

[1] For programmer types: if you're used to modern languages, you might be tempted to think of this as an array of `Ancilla` structs, but it's actually several different arrays, one per property. This is important later when we write out of bounds.

