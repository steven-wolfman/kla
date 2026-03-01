---
title: "Mystery Machine Schedule"
layout: activity
---

From: Gerard Tel (gerard@cs.uu.nl)
Date: December 8, 2009, 6:54 am

## Mystery Machine Schedule

Designed by Gerard Tel (gerard@cs.uu.nl, Utrecht University)


## Overview To KLA

Summary: Some 10 students come forward and write a time interval on a sheet.  Using a Greedy Algorithm, a maximal-size subset without overlap is constructed.
The activity gives students insight in the role of a Greedy Choice Property for a certain optimization problem.


Learning Goals: 

At the end of this exercise, students will...

- understand the Greedy-Activity-Selector (of Cormen, Leiserson etal, Sec 16.1),
- are aware of the role of a Greedy Choice Property, and that a GCP should be formulated for each optimization problem they encounter,
- understand that other greedy strategies do not work.

Course And Level: The activity was made up for a course on Algoritmics, taken in the 2nd or 3rd year, based on "Introduction to Algorithms" by Cormen, Leiserson, Rivest, Stein.

Class Size: At most ten students can participate, the rest of the group can watch.

Preparation Time: You should have a dozen of sheets on which a student can write (his name,) a starting time and finishing time.

Execution Time: 10 to 20 minutes.


## Planning For KLA
Materials: A dozen pre-printed sheets to write on, a handful of markers.

Preparation: The activity is part of a lecture on the Greedy strategy for solving optimization problems.

As always, read this description carefully and practice the KLA before using it in class!

## Execution Of KLA


Description: Teacher asks the class for a name of a fantasy machine that does not, but should exist.  (People may respond "world peace machine", "pocket torch on wind energy", "smoke liquefier" or whatever.)  Now the teacher states that we will build this machine, and invites 10-12 persons who would like to test it.  Each tester will write an interval of time (starting plus ending time) during which he would like to test the machine.  Clearly, not everybody can test the machine if the intervals overlap.  Goal is to find a LARGE subset of testers that can test the machine at the disired time.
The setting defines a search space (subset of testers), a feasibility (freedom of overlap), and a goal function (size).  A greedy strategy will select testers one by one, and eliminate after each choice, all overlapping requests.  Will it work to start picking the guy A with the shortest interval?  Will it work to pick the guy B with the earliest starting time?  Will it work to pick guy C with minimal finishing time? Perhaps in this example, but is it provable as a general property?
I ran the activity in Slovakia (Nov 2009) and, quite nicely, all three strategies mentioned above gave a result of 5 accepted requests.
What property should we prove to support the claim that we can safely pick the tester C with minimal ending time?  It is the GCP for this strategy: For each feasible subset S without C, there exists a feasible subset S' with C of at least the same size.
Steps in the proof are illustrated by having students step forward, step backward, sit, permute, and so on.


**Variants And Extra Topics**: 

- Try what happens if we select the shortest interval first.

- Try what happens if we select the earliest starting point first.

- Try what happens if we select the latest starting point first.

## Constraints On KLA

Would your KLA work if your students had the following constraints:
- Limited Vision: A participant must observe the intervals of other students.
- Limited Hearing: hearing-impaired can participate because the activity does not make use of sound communication, but the rules should be communicated in written form, of course.
- Limited Mobility: The participants must be able to "sort themselves by ending time" or other greedy criteria.
- Trouble Speaking: Participants need not speak at all.
- Touch Aversion: In the basic form, no touching is required, just looking at each others intervals. 
- Other: Not that I know of.

## Pitfalls Of KLA


## Feedback And Use Notes

*(don't give feedback on your own KLA!)*

Feedback: **add your feedback here!**

Use Notes: **add your use notes here!**

- Used on September 15, 2009, in a group of 60 students of Algorithmics (Utrecht Univ. by author, Gerard Tel).  Reactions of students, most: nice way of learning, allows for longer span of attention, helps to understand topic faster.  But also: chaotic, time consuming.
- Used on November 4, 2009, in a group of 25 students of Algorithmic Desing (Kosice Slovakia, byauthor, Gerard Tel).

## Related Resources

*You or later users of the wiki can add links (that don't fit into the text above) to related discussions, papers, repositories, examples, etc.*