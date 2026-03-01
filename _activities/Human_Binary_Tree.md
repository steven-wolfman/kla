---
title: "Human Binary Tree"
layout: activity
---

## Human Binary Tree

## Designed by Steve Wolfman

This is currently a stub.

## Overview To KLA

Summary: This KLA explores binary trees by having students act as nodes in the tree with their arms as child pointers.  Its key strength is giving students a "local" or "embedded" sense of what a binary tree is and how to computate with one; so, its best use is after students have already been introduced to binary trees through other means. 

Learning Goals: At the end of this exercise, students will...

- understand the basic structure of binary trees (nodes, each with 0, 1, or 2 children)
- have a feel for how binary tree computations work locally: as recursive processes executed on a single node, "trusting" that child results are correct and independent of parent computations, all on a tree with a global form that is hidden from students
- recognize that the typical graphical representation of binary trees is just one of many possible abstractions for understanding the trees

Course And Level: *What course is your KLA appropriate for?  How (im)mature should students be for the KLA? Are there prerequisites for your KLA?  There may be many different possibilities, but try to list the most appropriate courses first.  Also, you might mention how variants (using the "extra topics" section below) can address different courses and levels.*

Class Size: works well for about 15 or more; generally improves with larger classes

Preparation Time: minimal

Execution Time: ~10 minutes; can get raucous and therefore take a few extra minutes


## Planning For KLA

Materials: none

Preparation: Essentially none, but as always, read this description carefully and practice the KLA before using it in class!

## Execution Of KLA

Description: Explain to students that they're about to form a single binary tree as a class.  Pick a student to be the root (or solicit volunteers or choose to be the root yourself). Have the root stand up. Explain that the root is one node in the binary tree and, like all the nodes, has two arms to act as pointers. Now, explain how they're going to form the tree. Have the root point one arm, straight and stiff, finger extended, at another student, preferably elsewhere in the classroom. That action and clear eye contact with the other student makes the other student the root's "child". Remind students that each node should have exactly one parent except the root. Tell the other student to stand now that she is part of the tree. Now, explain that when you say "go", the class is going to form itself into a binary tree through this procedure. Students not yet in the tree will remain seated. Students in the tree will find two seated students to point to, ensuring that they make clear eye contact with the other student to confirm the parent-child relationship. As soon as a seated student gets a parent, he will stand and continue the process. If a student can't find anyone to point to with one or both arms, they should point straight down (to "ground" for the EE-trained among us) to indicate a null pointer.

Warning: this process gets quite loud and raucous! 

Once the tree is formed have students verify verbally and through eye contact that they know who their parent and children are. 

Now, you're ready to perform a calculation with the tree. Explain to students how a calculation like "height of the tree", "number of leaves", or "deepest node" would work and then give it a shot. Be aware that it *will* proceed in parallel and, again, become quite raucous. You may want to walk students through several steps in serial to get the idea and help out students who look confused. 

This exercise gives students a very local feeling for how a binary tree and calculations on a binary tree work. You might want to have students explicitly reflect on what sort of patterns of connection and information motion are occurring through the class as a whole to help them see the broader picture. You might also point out some felicitous analogies between the classroom and the arrangement of tree nodes in memory. For example, although the tree is conceptually of the usual form (a root with (up to) two children below it, and (up to) two children below each of those children, ...), it is actually laid out in the classroom and potentially in memory as a spaghetti mess with pointers oriented all over the place. You could even draw a bit of the conceptual tree and a bit of a map of the class's physical tree on the board.

**Variants And Extra Topics**: 

*Fill in a list of variants of and extensions to your KLA. Make the list as in the following:*

- Extra Topic One: describe the extra topic here

*Make sure that the title of each extra topic is capitalized.*

## Constraints On KLA

To be completed.

Notes: assumes students have two arms capable of pointing and may require holding arms up for a few minutes.  Makes some assumptions about ability to see, but (with care to establish parent-child connections) lack of sight will actually just emphasize "local" nature of tree.  Assumes students can stand; while this is not necessary, it is a convenient process element to keep the tree from becoming a graph (i.e., accidentally having two parents claim a child).  For classes with students who can't stand, just stress that parents should ensure that their child confirms having just them as a parent.  (A post-process pass can get rid of illegal links in the tree, setting one parent's child pointer to null.)  Not being able to stand to see the whole tree is, again, not a problem since the emphasis is on a local sense of the tree.

*Fill in your responses to the prompts below.  Please really think about these prompts and, when feasible, alter your description to account for these constraints.  Alternatively, you might summarize your response to all the prompts after the bulleted list.*

Would your KLA work if your students had the following constraints:
- Limited Vision: (including color-blindness)
- Limited Hearing: 
- Limited Mobility:
- Trouble Speaking:
- Touch Aversion: (including cultural)
- Other:

## Pitfalls Of KLA

*What common problems or slip-ups should instructors using your KLA look out for?  Think of pedagogical pitfalls (e.g., students taking the metaphor of the call stack being like a row of students too literally), logistical pitfalls (e.g., the steep rake in many lecture halls will interfere with data movement in the grid multiprocessor simulation), and "environment" pitfalls (e.g., students should avoid use of abusive language while anthropomorphically role-playing various computing platforms or other problems that may lead to a negative classroom environment for one or more students).*

## Feedback And Use Notes

*Leave the feedback section blank (don't give feedback on your own KLA!), but you should be able to add at least one entry to "Use Notes".  Replace the template provided below, including the information most relevant to your KLA.*

Feedback: **add your feedback here!**

Use Notes: **add your use notes here!**

- *Used Fall of 1973 in a 4500 person CS2 course.  Some comments about that use; perhaps how the use relates to variants, pitfalls, or optimal class type. (Author Name)*

## Related Resources

