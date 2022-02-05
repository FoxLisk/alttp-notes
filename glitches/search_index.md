Summary to come (maybe). Thanks to Glan for info.
====

[11:32 PM] Glan: I may not be remembering it exactly right, but I believe this is how making an ancilla works, at least for standard ones and not sparkles.

1) if there is an empty slot in 0-4, create it in the highest available slot. (Special case: bombs start in slot 1)  
2) if there is no empty slot, look at the index:   
2a) if the index is 0, set it to 5.  
2b) decrement the index.  
2c) if the ancilla at slot[index] is replaceable, replace it with the new one and exit.  
2d) If the index is now 0, exit. Otherwise repeat from 2b).  
...
[11:37 PM] Glan: There are some other special cases here too. Something worth noting is that all ancillae have "quotas", i.e. only so many of them can exist at once. E.g., only one dash dust at once, only 3 lamp flames, etc. There can only be 3 stuck arrows at once, and there's a special case there to force you to be able to keep firing arrows still. It won't stop searching when it goes to 0 and will loop back to 5 (I think?), which is unlike any other ancilla 
[11:37 PM] Glan: And yea if it doesnt really make sense, it's because it's a horrible way to implement the system 
...
[11:38 PM] Glan: So the 6 arrow thing done frequently is to set the index to 2 
[11:39 PM] FoxLisk: oh! 
[11:39 PM] FoxLisk: setting index high and then firing 6 arrows sets it to 2? 
[11:39 PM] Glan: Which works by: 

Index is any value greater than 4  
Arrow in slot 4  
Arrow in slot 3  
Arrow in slot 2  
Arrow replaces slot 4, sets index to 4  
Arrow replaces slot 3, sets index to 3  
Arrow replaces slot 2, sets index to 2  
[11:40 PM] FoxLisk: right, because the index decrements before checking if an ancilla is replaceable  
...  
[11:41 PM] Glan: So I'm not sure off the top of my head what happens if you have an ancilla in 4 and then shoot 6 arrows like this  
[11:41 PM] Glan: I'd guess it goes to 1  
[11:41 PM] Glan: Because theyd be in 3,2,1 instead of 4,3,2  
[11:42 PM] FoxLisk: is $ANCILLA is replaceable a function of $ANCILLA alone or a function of ($EXISTING_ANCILLA, $ANCILLA_THAT_WOULD_LIKE_TO_REPLACE_IT)?   
  
