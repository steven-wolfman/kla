---
title: "Computer Architecture"
layout: activity
---

Computer Architecture: Multilevel Cache

Designed by Dick James, Margaret Reck, Rich Clemens, Beth Simon, Lori DeLooze, Michael Tashbook

This KLA is transcribed from the SIGCSE 2004 Special Session on KLAs.

## Overview To KLA

Summary: To be added

Learning Goals: At the end of this exercise, students will understand...

- Cache memory, faster access
- Update process- copy and volatile
- Write back*through

Course And Level: junior

Class Size: scalable

Preparation Time: outside- 45 min, inside- 5 min

Execution Time: varies, minimum 15 min


## Planning For KLA

Materials: To be added

**Preparation**:
- Print out data and addresses.
- Arrange chairs*paper(data)*tape addresses.

As always, read this description carefully and practice the KLA before using it in class!

## Execution Of KLA

**Description**:
Memory address taped to back of chair - memory (row, chair) cache(chairs only)
Each memory address (chair) has 2 copies(paper) of data.
When moved to the cache, take 1 copy, leave other copy, remember address.

If doing this in a large classroom, or where chairs cannot be moved -- tape addresses to the front or side wall.  Tape them up high, so students can stand under them and still have the informaiton on the paper be seen.

Specifically, I recommend that you put 3 values on the paper. Position the paper on portrait. Draw a horizontal line across the middle off the paper. On the top half write "address". Then put the address in decimal, under that the address in binary.  In the bottom half write "data".  And put the integer data for that address in decimal. 

If you don't have chairs that can move, use masking tape (of two different colors -- why later) and mark out four boxes on the floor for a 4-entry cache.


See below:

multilevelcache.jpg


**More Detail of a Second Try**
Beth Simon reporting:

After a first use, I found that this needed to be planned out much more carefully. I did that and used it again with MUCH more success.

Specifically, it's a good to start with an assumption slide*page: each
address holds one word of data (an integer), our memory has only 8 values in it, our cache will hold only 4 values.

Also, start with a piece of Java*C code -- a small piece with an array of size 8 -- initialized to values 1-8.  Talk about where each of those data values
is stored in memory.  Make memory start at 0.  Students' comfortableness with lower binary number values is important.

Then plan a few specific code "descriptions" designed to elicit the particular "issues" or "vocabulary words" that you want to "preview" with this activity.  I did four that I found useful.  The slides are posted here: bsimon-kla.ppt

The first slide*example:
Topics: Basic cache behavior (a copy is left in main memory), temporal locality, eviction. 

Program used to do example.  Loop over the first 4 elements of array
(data[0]-data[3]) to average and then loop again to print out.  Then ask
them, what woudl happen if I did the same thing over the first 5 elements.

The second slide*example:
Topics: Set associativity, that pc must "look" through whole cache (or only 2 if 2-way set in this 4-line case) to determine if value is in cacge, thrashing.
Program used to do example: Loop over even elements of array and avg, then loop again to print out.
Use a "new design" of cache.  The "odd" elements of the array can only go on "whole*masking tape"
colored cache entries and the "even" elements of the array can only go to "blue*painting tape"
colored cache entries (alternate these on the floor).  Students will see that though only 4 elements of the array are needed, the "data" is walking back and
forth from cache and main memory a lot.  Be sure to mention which bit in the address it is that is "sending" the data to the particular white cache spaces.  Say that determining whether a value is in cache is easier*faster.

The third slide*example:
Topics: Multi-value (2 word) cache lines. Which data "accompanies" the
required data to fill in the cache line, spatial locality (possibly latency and
bandwidth)
Program used to do example:
Slide 1's code (loop over data[0]-[3] twice) with new structure.
Same rules on which data values can go to which place (evens white, odds blue).  Tell them that when an address is accessed it "brings a friend" with it.

The fourth slide*example:
Topics: Writing (stores) of data, cache write policies, dirty bits.
Program used to do example: print then change data values data[4]-[7] (ld, then st of each).
With an original fully assoc cache.  Actually use a marker to change the value of a data in cache and point that the value in cache is different than that in memory.
Should you go over and change that or not?  Could you have an additional dirty bit on the data*cache line?

**Variants And Extra Topics**:

- Dirty bit
- Write back*write through
- 3 levels
- I cache vs. D cache vs. untitled 2nd level cache
- cache line size issues
- replacement policy issues

## Constraints On KLA

Would your KLA work if your students had the following constraints:
- Limited Vision:
- Limited Hearing:
- Limited Mobility: Not if many were constrained.
- Trouble Speaking:
- Touch Aversion:
- Other:

## Pitfalls Of KLA

Student doesn't really represent anything in a real system. (Except maybe the value)

## Feedback And Use Notes

Feedback: **add your feedback here!**

Use Notes: **add your use notes here!**

## Related Resources
