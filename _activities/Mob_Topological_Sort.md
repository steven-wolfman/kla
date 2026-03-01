---
title: "Mob Topological Sort"
layout: activity
---

From: Guest ()
Date: February 27, 2006, 11:43 pm

## Mob Topological Sort

Designed by <a href="http:/*www.cs.berkeley.edu*~ddgarcia*">Dan Garcia<*a> (ddgarcia@cs.berkeley.edu) and <a href="http:/*www.imdb.com*name*nm0002017*">Emilio Barzini<*a>. (I didn't know until this day, that it was Barzini all along.)

## Overview To KLA

Summary: This is an entire-class activity to demonstrate the topological sort algorithm and the concept of cycle detection. Students play the role of nodes and a single arm as a directed edge, and the instructor simulates the topological sort algorithm on this human graph. When the algorithm terminates, everyone either has a labeling or there are cycles in the graph.

Learning Goals: At the end of this exercise, students will understand the topological sort algorithm, having run it firsthand.

Course And Level: This is appropriate for any class in which topological sort is being taught, which presumably would be after students understand graphs...probably CS2 (Data Structures and Algorithms). Younger students could enjoy this as simply a fun activity, or as a gentle demonstration of a graph algorithm.

Class Size: This exercise works well with any class larger than about 5 people, and scales well to an unlimited number (the instructor simply runs the 'days' faster as the numbers grow into the hundreds).

Preparation Time: Virtually no preparation is involved (other than practicing it a few times to get the directions correct). It helps to have a slide or transparency shown to reiterate what you are saying.

Execution Time: The exercise runs until termination, which is about 5-7 minutes (even with a class of 250). Estimate 2 minutes to explain, 2-4 minutes to run, and a minute to settle folks down.

## Planning For KLA

Materials:  Optional: Slide explaining the KLA (ppt, <a href="/assets/attachments/KLATopologicalSort.pdf>pdf<*a>)

Preparation:  None really required, other than being assured you understand the KLA. 

## Execution Of KLA

<img src="/assets/attachments/SIGCSE2004MobTopoSort.jpg" width="640" style="display: block; margin: 0 auto;">

Description: All students are asked to stand, and choose a nearby neighbor (but don't tell them they've been chosen). Then, all at once, they should put a hand on that person's shoulder. Tell them they've just formed a human graph (their bodies are nodes, their hand a directed edge) of *n* nodes and *n* edges. You're simulating the world of "The Godfather" with mob bosses on every corner, but really running the topological sort algorithm. (The instructor controls the flow of time in this activity, in a unit of "days".)

First day: At once, all those with no hand on their shoulder are **mob bosses**, and are immediately "whacked" (labeled with the 'day' and asked to sit down and put their hands on their lap). The rest remain standing, and "live" (i.e., remain standing) to see the next day (second, in this case). This process continues, with the instructor saying *Ok, it's day i. Raise your free hand if there's no hand on your shoulder. You're now a mob boss, but because you're so conspicuous, you're whacked, labeled i and need to sit down with your hands in your lap.* 

Instructor continues to iterate, with the mob bosses for that day sitting, and fewer and fewer remaining standing. When a day goes by without whacking, either all are sitting or there are simple cycles remaining. All mob bosses who were whacked on a particular day have no relation, so they can be labeled anything as long as everyone from day 1 is labeled before those from day 2, etc. Said another way, the labeling of each node can be thought of as having an integer and fractional part. The day determines the integer part and each mob boss gets to pick their own unique fractional part.

To close, thank everyone for participating in the KLA and (optional) comment on the number or size (or lack) of the remaining cycles.

**Variants And Extra Topics**: 

- Multiple Edges Per Node: Since every node has exactly one outgoing edge, all cycles contain *k* nodes and exactly *k* edges in a circle. This is an interesting result, but to remove that constraint, you could ask each student to use both their arms as edges.

## Constraints On KLA

Would your KLA work if your students had the following constraints:
- Limited Vision: These students may have trouble picking a random neighbor, may need assistance putting a hand on their shoulder, and may not know when they became a mob boss if they were wearing a sweater.
- Limited Hearing: These students may not hear the directions to sit at the appropriate time, possibly because they were caught up in the actions of their classmates.
- Limited Mobility: Standing and sitting are not *really* required, but an equivalent would have to be created for these students. Also, touching a neighbor's shoulder could be difficult for some  each student could make sure the "touchee" knows they've got a potential mob boss pointing at them.
- Touch Aversion: This could be worked around by placing a held pencil (or other simple pointing device) on the shoulder instead of a hand (for the touch-averse pointer or pointee).
- Other: Some may be offended by the ethnic or violent reference (certainly not appropriate for younger students). Another metaphor can easily be swapped in if desired.

## Pitfalls Of KLA

Mob Topological Sort shares some pitfalls with all other KLAs. Students may be uncomfortable participating or acting "silly." We believe that establishing a culture of participation early in the course can ameliorate these issues. Also, as everyone is acting in concert, there's less of a feeling of being put on "the spot". The instructor must also make sure to control the time and speed up the "day counter" if the class size is large.

The metaphor of people=nodes and hands=directed-edge is quite strong, so there's no real chance of confusing the analogy.

The point of this exercise is not necessarily to get a perfect numbering, but to have everyone understand the algorithm. As such, even if people don't sit when they are supposed to, the exercise can still be a success. It's also resiliant to troublemakers who don't want to play correctly and revel in making life miserable for the instructor.

## Feedback And Use Notes

Feedback: **add your feedback here!**

Use Notes: **add your use notes here!**

- Used Spring 2004 in a 250 person CS3 course and as the flagship KLA in a 50-person SIGCSE 2004 KLA session, both with great success (see photo above). (Dan)

## Related Resources

- <a href="http://www.nist.gov/dads*HTML*topologcsort.html">NIST definition of Topological Sort<*a>
- <a href="http://mathworld.wolfram.com/[TopologicalSort](/activities/TopologicalSort/).html">Mathworld Topological Sort</a>