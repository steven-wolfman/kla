---
title: "Event handlers in Java"
layout: activity
---

From: Guest ()
Date: March 7, 2006, 4:13 pm

## Event Handlers In Java

Designed by Dean, Kristan, Sebastian and Barabara.

## Overview To KLA

Summary: Learn what it means for an object to register as a listener, and to be notified when an event occurs. 

Course And Level: CS1/CS2

Class Size: Small class, 20 people.

Preparation Time: 10 minutes

Execution Time: 20 minutes

## Planning For KLA

Materials: Playing cards, Dice, Magic wands, post it notes, pens, random set of objects. 

Preparation: Write a set of funny actions on the post-it notes. Color code the actions for the red or black events. Organize cards into 13 sets of each rank. 


## Execution Of KLA

Description: 

Assign two students to be event registrars. One is the red registrar, one is the black registrar. Give one registrar a die, and the other a coin to flip. 

Give each student a rank of cards (all the twos, or threes, or fours, etc.) 

Instruct the students to give one red card to the red registrar if they are interested in the red event. Likewise for the black registrar. The students should keep the other like-colored card in their pair and display it on their desk. As they give the card to the registrar, they should take a like-colored post-it note with an action to perform when they get notified about the event.

Each registrar rolls his die or flips his coin to determine whether to trigger the event. Odd rolls are red, even rolls are black. Heads is red, tails is black. For each card they received that matches the color chosen by the die or coin flip, find the student with the matching card and tap them with the magic wand.

If a student is tapped by the magic wand, he should do the action listed on the post-it note.

Interesting effects to look for:

- What if one student is tapped by a magic wand while already performing an action from the same or different event? Should they be serialized or done in parallel?

- When should the student stop performing an action that repeats (e.g. jump up and down)? Is there an event termination event?

**Variants And Extra Topics**: 

- Extra Topic One: Handle only a certain number of events and then unregister your event handler by taking back your card. 

## Constraints On KLA

Would your KLA work if your students had the following constraints:
- Limited Vision: (including color-blindness)
- Limited Hearing: 
- Limited Mobility:
- Trouble Speaking: Yes
- Touch Aversion: (including cultural)  Yes
- Other:

## Pitfalls Of KLA

Be sure to explain the metaphors while performing the KLA. If you don't have enough students to be the event registrars, play this role yourself. 

Be sure to have innocuous actions to perform for the shy students. 

## Feedback And Use Notes

Feedback: **add your feedback here!**

Use Notes: **add your use notes here!**

## Related Resources