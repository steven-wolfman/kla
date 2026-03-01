---
title: "KLA Building Blocks"
layout: resource
---

## KLA Building Blocks

A KLA building block is a common idiom or pattern that can be used across many different KLAs.  A good example is the use of a student's arm to represent a pointer or reference (used, e.g., in the [Cons Cell Jeopardy]({{ "/activities/cons-cell-jeopardy/" | relative_url }}) and [Human Binary Tree]({{ "/activities/human-binary-tree/" | relative_url }}) KLAs).  Knowing these can help you brainstorm new KLAs or flesh out exercises that you're already working on.  Here is a list, divided roughly into categories; please feel free to add new building blocks or comments about the existing ones!

High-Level Ideas

- Algorithms Enacted By People: e.g., a group of people pipelining an activity

- Data Structures Built From People: e.g., an array of students

## Body Mappings

- Arm As Pointer: students arms are pointers or references; pointing is referring; pointing down ("to ground") is a null reference; can use touch rather than pointing (constrains references to be local and can make certain pointer arrangements difficult or impossible to construct; does not require sight lines; be aware of student inhibitions toward touching*being touched!); person + 2 arms*pointers is a binary tree node; be aware that some students may have difficulty holding arms up for an extended period of time, may not have two arms, or may not have full use of their arms

- Standing*Sitting As Binary State: usually sitting is reject, unused, waiting while standing is accept, used, processing; be aware that some students may not be able to stand easily or at all, that standing may block sight lines in some rooms, that sitting*standing status may not be clear in some rooms (e.g., w*steep rake), and that some chairs may make standing difficult

- Person As Separate Module: this may seem obvious, but people understand that they are separate entities and the limits on their communication; use the distinction among individuals to show separation of modules in algorithms. [Parameterized Student Sort]({{ "/activities/parameterized-student-sort/" | relative_url }}) has a good example in which a student plays a sorting function and another student plays the comparator function; the comparator never tells the sorter (or the class!) what basis she uses for comparisons, and so the class understands that the sorter does not need that information.  Similarly, it may be easier for students to understand a concept when they are concerned with or can only see a part of it (e.g., understanding the "local" focus necessary to craft recursive algorithms by being one node in a huge binary tree for which they have no global sense as in the [Human Binary Tree]({{ "/activities/human-binary-tree/" | relative_url }}) KLA).

- Students As Data: in the simplest sense, each student is a data point, and you can count students (as in the [Counting the Class]({{ "/activities/counting-the-class/" | relative_url }}) KLA) or compute over the arrangement of students; more generally, students are loaded with data such as height, hair color, amount of hair on head, clothing color, distance from various points in the classroom, student ID number, matriculation year, favorite X (color, number, etc.); beware of privacy concerns and embarassing questions!

## Classroom Layout

- Rows As Time-Slices: have each row in a lecture hall represent one time-slice in a process; watch the process proceed forward or backward through the room

- Grid Of Rows And Columns As 2-D Array: as above, rows and columns together can form a 2-dimensional array, e.g., for simulating the pixels in a picture, the cells in a cellular automata simulation, or for explaining Manhattan Distance vs. straight distance

## Prop Thoughts

- Post-Its As Data: scribble data values on post-it notes and swap them out or cover them up to represent data changing

- Balls For Control Flow: pass a ball, frisbee, or other physical token to represent control flow in algorithms

- Strings For Connectivity: use lengths of string to represent graph connectivity, to constrain physical distance between parts of a structure, and to pass messages (e.g., by tugging on a string)

- Role Cards: prepare handouts beforehand showing students their roles in the KLA, either as a reference*reminder during the KLA or as a source sheet for them to learn the activity

## Accounting For Constraints

Try to make your KLAs as accessible as possible to as many of your students as possible.  Here are a few tricks that can help.

- Narrating The KLA: be aware of elements that are visual in your KLA and describe them verbally.  This will bring all students' attention to the key ideas and also help students who have visual impairments or just poor sight lines.

- String For Touch: many KLAs ask for students to touch each other.  One alternative to touching directly is to hold both ends of a piece of string.  Students are still connected and can feel the connection (by tugging).  However, the connection is more flexible and doesn't require direct touching, which will make some students uncomfortable.

- Pointing For Touch: replace touching with pointing.

- Counting Objects For Steps: replace counting steps in a KLA with counting rows passed instead (so students in wheelchairs can participate equally)

- Small Groups Rather Than Stage: replace a single activity performed on the "stage" of the classroom with many simultaneous activities performed in small groups.  Shy students will be more comfortable participating among a small group of their peers than in front of the whole class.

## KLA Tricks

- The Plant: if you need a particular idea or suggestion or have tricky timing to work out on your KLA, plant a TA among the students to make the suggestion or ask a student in the class to help out beforehand

- Group Median Selection: to find the median of the whole class's numerical guesses, have them write down their number (to commit to it).  Next, call out a number that should be somewhere in the range and tell students to raise their hands if their number is higher.  Adjust the number and repeat until approximately half the hands are raised.

- Distributed Algorithms: each student can perform a process and you can aggregate the data as a class. Example: in a machine learning class, you might want to show the value of committee decision-making algorithms; so, use group median selection (above) to have each student independently guess your weight and then show that the median is remarkably close to the true value (generally will be for large class of people).  Although not a KLA, Dave Reed's estimate the # of 3-letter words in the English language exercise is a great example: http:/*www.creighton.edu*~davereed*Nifty*[WordLab]({{ "/activities/WordLab/" | relative_url }}).html.

- Random Number Generation: students can help you generate random numbers or perform random processes; just ask one or several students to privately select among a set of options; try to make the options "neutral", however (e.g., given the numbers 1, 2, 3, and 4 to choose among, many people will choose 3)

- Small Groups To Scale Participation: if your KLA only involves a few people at the front but you want the whole class to take part, perhaps students can facilitate the same KLA in small groups throughout the class.  You can still perform the KLA once at the front beforehand or afterward as a "model" if necessary.

- Simultaneous Decisions: if you need something to happen in parallel, perhaps students can write down or think of an answer and then share it only once they're committed.  A good example is the selection of a target for each student's pointer in the [Mob Topological Sort]({{ "/activities/mob-topological-sort/" | relative_url }}) KLA.  Everyone looks around at their neighbors and silently chooses who they'll point to.  Once all have chosen, *then* everyone actually points.  
