---
title: "Massive Boolean Short Circuit"
layout: activity
---

From: brianacardysqa (brianacardysqa@gmail.com)
Date: March 14, 2012, 11:04 pm

## Massive Boolean Short Circuit

## KLA Overview

Author: Steve Wolfman, University of British Columbia

Summary: a whole class activity that shows short-circuit evaluation of Boolean operations.  Every student picks a `true` * `false` value, the instructor then calculates the `and` (`or`) over those values, emphasizing the futility of going beyond the first `false` (`true`) calculated.

Learning Goals: at the end of the exercise, students will...
- understand short circuit evaluation
- believe that short circuit evaluation is logically equivalent to full evaluation
- believe short circuit evaluation can save work for the computer

Course And Level: CS1 or later to teach short-circuit evaluation; also, useful for tail recursion; also possibly useful for introducing checksums (in a cryptography class?)

Class Size: works better the larger the class is

Preparation Time: minimal

Execution Time: &lt; 5 minutes


## Planning For KLA

Materials: none

Preparation: Make the indicated choices in this description (e.g., which comparator to use).  As always, read this description carefully and practice the KLA before using it in class!

## Execution Of KLA

Description: Ask everyone to pick a value at random: `true` or `false`.  Make students nod or raise their hands to confirm that they have committed to a value.  Then, announce that you'll be calculating the logical `and` of all the values in the class.  Ask for the first person's value and announce that this is the value of the `and` so far.  Ask for the second person's value and describe how this combines with the first person's value to make a new value.  Continue until at least two people past the first `false`.

Now, pause and look around the class.  Make a show of how much more calculation is left to perform and ask students whether there isn't a faster way.  If necessary, prompt them to come up with short-circuit evaluation.

Go back and quickly redo the calculation, this time using short-circuit evaluation, making it clear at what point evaluation can stop.

Variants And Extra Topics: below

- Or Rather Than And: just use `or` rather than `and` (recognizing that `or` short-circuits on a `true` rather than a `false`)
- Tail Recursion: write out code equivalent to this algorithm (ending with, e.g., `head and (all rest)` ).  Point out that this doesn't look tail recursive since it appears that the `and` will have to wait for `all rest` to execute.  Then compare it to the execution of the KLA in class (even redo a bit of the algorithm).  Explain how short-circuit `and` obviates the need to keep uncomputed results around.  (Remember that it's not keeping the left side around that makes it tail-recursive, *not* stopping on the first `false`! )
- Exclusive Or And Checksums: show how short-circuiting `xor` is not possible because the result depends on every student's value.  Explain that the `xor` is essentially a one-bit checksum and use that to introduce larger checksums. (For the ambitious: have the students figure out an efficient way to calculate the `xor` of the entire class.  One fun solution is to use a human binary tree to organize a large, parallel computation as in the [Human Binary Tree](/activities/Human_Binary_Tree/) KLA.)
- Raising The Stakes: first have students pick their values and then announce that, if the `and` across the whole class is `true`, you'll cancel the final.  Obviously, in any reasonably large class, the `and` will be `true` with negligible probability; however, you have to trust your students (and know they don't know about the exercise in advance) to try this one!  (It might be advisable to pick something smaller to jettison, like a weekly quiz that you didn't want to give anyway!  Then, you can cancel it even when the answer comes out `false`. )

## Constraints On KLA
Would your KLA work if your students had the following constraints:
- Limited Vision (including colour-blindness)
- Limited Hearing
- Limited Mobility
- Trouble Speaking
- Touch Aversion (including cultural)
- Other

With care on the instructor's part, this KLA should work in spite of all the constraints listed above.  Of course, the instructor must ensure that she narrates*illustrates the process in a way that is accessible to her students, but the students need not move, touch or be touched, or (necessarily) see or hear to participate.

## Pitfalls Of KLA

- Without errors or side-effects, the short-circuited version of `and` and `or` is equivalent to full evaluation; however, with errors and side-effects, they can be quite different.  Know beforehand whether you will discuss these issues and be prepared to defuse questions about them if you are not!
- This KLA treats students as data, which can reinforce a sense of inhumanity in the course.  Try to learn and use students' names during the exercise.  
- With malicious students, this exercise can go on for a while.  If your class is adversarial enough to do that to you, you may not want to try the exercise.  If you still want to try it, consider having them write down their random value on a bit of scrap paper beforehand.
- Assuming your students are not malicious, taking a long time because everyone picked `true` (or `false` for `or`) really is not a pitfall.  It doesn't happen.
- If you offer a reward for `true` on an `and` or `false` on an `or`, you may get some silly antagonism toward the first student who says the unpopular answer (and some embarassment on that student's part).  Know whether your class can handle this as a joke rather than as putting a student on the spot (to lie for the "good" of his classmates or tell the truth about his Boolean value).

## Feedback And Use Notes

Feedback: **add your feedback here!**

Use Notes: **add your use notes here!**

- Used Spring of 2001 in a 200 person CS1 course.  A few early `true` answers made it exciting, but otherwise it went off without a hitch. (Steve Wolfman)

- Used Fall of 2004 in a 13 person CS1 course.  A bit too small for this exercise to be really effective, but it still generally got the point across.  Just talking with the students might have been a better use of time.  (Steve Wolfman)

- Used Fall of 2004 in a 45 person Functional and Logic Programming class to show why short-circuit `and` is tail-recursive in the naive implementation of the `all` function over lists.  I offered to cancel the final exam if the `and` was true and had a moment of concern after two `true` responses in a row, but the third student responded `false`.  I had to explain that it wasn't stopping at `false` that made it tail recursive but rather not having to wait on the recursive call (though they're linked!).  


