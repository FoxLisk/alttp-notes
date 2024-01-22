This is my attempt at rewriting the assembly code for `AncillaAdd_ArrowFindSlot` in structured pseudocode, to make it easier for me to read. [See the ASM here](https://github.com/spannerisms/jpdasm/blob/master/bank_09.asm#L6161)

This takes some liberties with the structure of the code - specifically the last block contains some mid-loop-`goto`s that I have treated differently - but I believe correctly maintains the semantics.

```
Y++
$0E = Y # quota; set to 3 before calling the routine
Y = 0
X = 4


# count how many ARROW_IN_WALL ancillae we have (in front slots)
while X >= 0:
	A = 0x0A
	if ANCILLAE_IDS[X] == A:
	Y++
	X--

# if we don't have exactly 3, look for an empty slot (only!)
# note that this branch always returns
if Y != $0E:
	# find an empty slot
	Y = 4

	while Y >= 0:
		A = ANCILLAE_IDS[Y]
		# if this slot is empty, we can spawn here
		if A == 0:
		  return Y
		Y--
	return Y # i.e. return -1, i.e. failure

# if we have exactly 3, find one by starting at the
# search index and looking down, resetting the search index to
# 4 if necessary.
while True:
	SEARCH_INDEX--
	if SEARCH_INDEX < 0:
		SEARCH_INDEX = 4

	A = ANCILLA_IDS[SEARCH_INDEX]
	if A == 0x0A: # ARROW_IN_WALL
	    return SEARCH_INDEX
	if SEARCH_INDEX < 1:
		SEARCH_INDEX = 5
```

