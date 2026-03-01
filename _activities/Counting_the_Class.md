---
title: "Counting the Class"
layout: activity
---

## Counting The Class

## Designed by Steve Wolfman

## Overview To KLA

Summary: Students invent and analyze algorithms for counting the number of people in the class and implement at least one on the spot.

Learning Goals: After the exercise, students will understand that many different algorithms may address a single problem.  They will recognize that there may be tradeoffs between speed, accuracy, and accuracy guarantees (such as upper and lower bounds).

Course And Level: Suitable for an introduction to algorithms, algorithmic thinking, or analysis of algorithms.  Tunable (e.g., through vocabulary or formality of algorithm descriptions) for any level at which these topics are introduced &mdash; probably an algorithms or introductory programming class.

Class Size: large; at least 50 students

Preparation Time: minimal

Execution Time: 5-20 minutes, easy to cut off when instructor chooses

## Planning For KLA

Materials: No materials are required.

Preparation: The instructor should decide what specific algorithms she wishes to address.  For example, an instructor might wish to ensure that an algorithm providing a good upper bound and a randomized algorithm is discussed.

The instructor should also decide what vocabulary to use.  For an introductory programming course, this might be intuitive vocabulary (e.g., "no more than" rather than "upper bound").  For an introduction to algorithms or algorithm analysis, the instructor might want to insist on precise terminology.

Finally, the instructor may wish to have on hand materials students might use for their algorithms such as attendance lists or dice.  

As always, read this description carefully and practice the KLA before using it in class!

## Execution Of KLA

Description: Start by posing the problem: to design algorithms for counting the number of people in the class.

As a strawman, suggest that you could count the students one by one in a well-defined order.  For example, in a lecture hall you might say, "Here's a first algorithm.  I will walk along the rows counting each of you, one by one, starting on the left side of the first row and working my way left to right, front to back over every row."  Actually start performing the algorithm to begin drawing students into the activity.

Ask about the properties of this algorithm you'd like to emphasize throughout the discussion.  For example, you might ask "About how long will this take?  Will I have an exact count when I'm done?  How and why can you guarantee that I'll have an exact count?"  Note also that you should monitor the language students use in responding and encourage the level of precision you expect: perhaps "a long time" is an appropriate response, but you might be looking for an answer like "about two seconds times the number of people plus ten seconds times the number of rows" or "order <i>n<*i>".  (Will students notice that you failed to count at least one person in the class: you?)

Now, ask students to contribute their own algorithms and discuss their properties.  A think*pair*share might be appropriate here.  Note that your questions on the strawman algorithm will likely guide students' thought processes as they design algorithms.  For example, asking how many "CPUs" the first algorithm required would encourage thoughts of parallel algorithms.

Once the students have finished discussing or you feel you need to move on, actually perform one or two of the more interesting algorithms.  (If there is a specific algorithm you wanted to perform and your students didn't suggest it, you may need to do so yourself.  Bear in mind that your questions can encourage a desired line of thought, however.)  You should already have discussed the analysis of the algorithm before performing it, 

A fun one to perform in class is a randomized algorithm.  Have all students stand and pick from a set of `k` numbers.  Choose one of the numbers and have everyone who didn't select that number sit down.  Now, count the remaining students and multiply by `k` for an approximation of the total number of students.  Of course, you can do multiple rounds of selection or use entities other than numbers.  Also, certain sets of numbers might bias your result (e.g., people have a penchant for the number "3").

**Variants And Extra Topics**: 

## Pitfalls Of KLA

The algorithm(s) actually used may entail pitfalls (i.e., dangers of touching if you tap students on the head as you count them off).  However, a careful instructor should be able to remove most such dangers.  Particular concerns that may be difficult to avoid are reliance on sight, hearing, and standing.

Holding a productive and respectful discussion can be challenging as well.  That's somewhat outside the scope of a KLA's pitfall section.   However, given the potentially critical nature of the algorithm analysis, an important point is to be supportive and positive about student contributions (e.g., discuss *properties*, not *limitations/ of the algorithm).

## Feedback And Use Notes

Feedback: **add your feedback here!**

Use Notes: **add your use notes here!**

- Used spring of 2001 in a ~200 person introductory programming class to introduce the notion of algorithm.  I suggested the strawman algorithm described above and focused on intuitive runtime and guarantees of accuracy.  Students suggested checking the class enrollment list (fast approximation, not guaranteed to be an over- or under-estimate at that stage of the term), checking the maximum occupancy of the room (fast over-estimate), counting the number of people in one row and multiplying by the number of rows (somewhat fast approximation), counting the number of seats in one row and multiplying by the number of rows (somewhat fast over-estimate for that room), and refining that algorithm by counting and subtracting the number of empty seats (somewhat fast accurate count).  I congratulated them on the scope of their algorithms (especially realizing that they could refine algorithms!) and then suggested and performed the randomized algorithm above with the numbers 1, 2, 3, and 4 and then the colors red, green, and blue.  We ended up with an approximate count of 48 and discussed why the approximation was so bad. (Steve Wolfman)

## Related Resources
