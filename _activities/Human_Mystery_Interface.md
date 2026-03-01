---
title: "Human Mystery Interface"
layout: activity
---

## Human Mystery Interface

## Designed by Steve Wolfman

## Overview To KLA

Summary: A KLA for HCI courses in which a student is a robotic toy with a simple, broken interface.  The class watches another person interact with the toy and then discusses what went wrong.  They design a new interface for the toy which they test in similar fashion.  Students learn to use their classroom knowledge to fashion and iterate on a simple example.  Because the "system" is a human, students have no concerns about the fidelity of their interface design or its "hardware constraints".

Learning Goals: At the end of this exercise, students will...

- better understand how features of a design support or hinder users' understanding of the design
- believe that careful design of an interface can cultivate an intended mental model of the interface
- know roughly what a speak-aloud protocol is and how it can help design investigations

Course And Level:  HCI or UI design course.  Students must be familiar with some concepts that will help them construct successful designs (e.g., Norman's "affordances").  Whatever student (or other helper) interacts with the "robots" must be familiar with speak-aloud protocols.

Class Size: best for a small class (when everyone can physically approach the "robot" during design); scales to large classes via stage*audience separation or possibly group work

Preparation Time: ~20-30 minutes of pre-class preparation

Execution Time: ~15-60 minutes; roughly tunable by ~10 minute chunks (based on ` of design iterations)


## Planning For KLA

Materials:

- Robot limitations handout
- Robot interface handout

Preparation: Design functionality, constraints ("hardware" limitations), and an interface for your "robot" that will illustrate the terminology and concepts that are important to your course.  (An example is below.)  Prepare separate handouts detailing the constraints and the interface.  

Also, know who will play your users and know how you will select your robots.  The robots must be willing to be touched on their arms and willing to play along with a silly situation.  The users must be capable of performing an effective think-aloud for the class, unfamiliar with the KLA, willing to miss portions of the exercise, and willing to be the only people not "in the know" in the room.  Fellow instructors, senior students, or TAs might make good choices.  Explain the rough outline of the exercise to the users before class: 

  - They will interact with a robotic "toy", which may require touching the robot's arms, no higher than the elbows.  They should narrate their thought process throughout the exercise as though they were in a think-aloud user study.  At some point you will ask them to describe their model of the behaviour and interface of the robot.

As always, read this description carefully and practice the KLA before using it in class!

Here is an example:

- Functionality: `The Carosolo 9000 Robotic Toy is designed to spin 360 degrees to the left and to the right to amuse its user.`
- Constraints: 
  - `The robot requires 5 seconds of processing between receiving a command to spin and 2 seconds of processing afterward before it is ready to receive commands again.`
  - `The robot is activated by proximity of a user (and deactivated by departure).`
  - `The robot otherwise only supports "hand and elbow button" input; that is, it may only receive commands via taps to the hand and elbow (four possible buttons).`
  - `The robot is capable of replaying one 10-word introductory message.`
- Interface:
  - `On startup, the robot raises its right and left arms, open palm facing out above elbow, forearm vertical.`
  - `On startup, the robot (approximately) replays the message: "Welcome to Carosolo 9000!  Use arm controls to activate functions."`
  - `On shutdown, the robot lowers its arms.`
  - `Tapping the robot's right palm activates the "spin left" behaviour (but remember the 5 second pre-delay and 2 second post-delay from constraints).`
  - `Tapping the robot's right elbow activates the "spin right" behaviour (but remember the delays).`
  - `There are no controls on the robot's left arm (it is up purely for the aesthetic effects of symmetry).`
  - `Once a behaviour is activated, further input is ignored until pre-delay, the behaviour, and the post-delay are complete; however, the arms remain in the same raised position throughout the process.`

This setup will stress concepts like affordances, natural mappings, and clear feedback.

## Execution Of KLA

Description: Besides the instructor, there will be three roles in the KLA: robots, users, and designers.  The robots will be the robotic "toys"*interfaces.  Start by selecting one student to play the robot and two users.  (You may have chosen the users during preparation.)  Before going further, the users must leave the room to avoid hearing the robot description.  In a large class, set the action happen at the front; in a small class, set the action in the center and allow designers to choose their preferred vantage point.

Explain how the exercise will work to the remaining students.  Describe the robot's functionality while handing out the descriptions of the robot's constraints and interface.  Talk through the constraints and interface, ensuring that the robot understands both clearly.  Practice a few steps with the robot.

Ask the audience (designers) to observe and take notes (as if this were a use test).  Call in the first user.  Explain that the class is here to test their interface design, not to test her.  Remind her that she is to explore the robot's behaviour and interface, that the interface may require touching the robot's arms but no further up than the elbow, and to think aloud during the exercise.  Then, stand back and watch.  

When you feel the class has seen the problems with the given interface, stop the exercise and ask the user to explain her mental model of the robot's behaviour and interface.

The user will likely have trouble understanding what the robot does, which of its parts are its controls, how to activate those controls, how the controls map to behaviour, and why some commands on the controls are ignored.

Thank the robot and user for their participation.

Ask the designers to redesign the robot's interface subject to performing the same functionality and respecting the same constraints as the original interface.  Have them support proposed changes from the notes based on the first user study.  Here is a sample redesign:

  - `On startup, the robot (approximately) replays the message: "Hello!  Tap a palm to make me spin that direction."`
  - `The robot raises both hands, palms out and prominent, during its welcome message.`
  - `Tapping the robot's left hand activates its left spin; tapping its right hand activates its right spin.`
  - `The robot lowers its hands after receiving a command (tap) and nods once per second during its 5 second pre-delay.`
  - `The robot's hands stay down and it again nods once per second during the 2 second post-spin.  It then returns to the palms-extended position.`
  - `On shutdown, the robot lowers its arms.#

This design uses relevant instructions, clear affordances (extended palms), a natural mapping (left hand to left spin, right to right spin), clear causality (a tap clearly activates behaviour and removes the potential for further control), etc.

Once your class has settled on their design, practice it with the robot.  Then, call in the second user and run the exercise as above.  After thanking the robot and user, discuss how the new design differed from the old one, other techniques that could have improved the design, etc.  To emphasize the value of think-aloud, discuss its place in understanding both iterations' user interactions.

Variants And Extra Topics: below

- Super-Human Interface: bring various physical props to create an interface such as post-its, string, and coloured hats.
- Abort: add the ability to cancel pending commands (during the 5 second delay); note, however, that even small increases in complexity make the interface much more difficult to design successfully!
- Voice Control: add some voice recognition (even a single word such as "abort" for the extension above).  A *very* important problem with this variant is that it can interfere with the user's think-aloud process.  Be sure to brief your user on this aspect of the exercise if you will use voice control.
- Group Work: in a large class where students are familiar with think-aloud, break into ~5 person groups for the *first* user study.  Each group should have one user (who must leave during the exercise intro), one robot, and three designers.  Then, return to a whole-class format for the second user study (or else too many second-iteration "users" will have to miss the entire first iteration and part of the second).

## Constraints On KLA

There are natural ways to alter the robot's interface, constraints, and functionality to include people with limited vision or mobility, trouble speaking, and touch aversion.  Indeed, in a design exercise any of these constraints can be used to explore inclusive design. (Be sensitive, however, about singling students out for their insights about inclusive design.)

Limited hearing poses a challenge because of the importance of the exercise's indispensible think-aloud element.  Good signing support will probably make this element successful. 

## Pitfalls Of KLA

Some key pitfalls:

- User Think-Aloud: ensure that the user is very familiar with think-aloud protocols; it's important not to confound the user's introduction to the robot with the user's fresh experience with think-alouds
- User Embarassment: laughter at the user's "fumbling" is inevitable; use this as an opportunity to remind students how much support users need during a study: test the interface, not the user!
- Malfunctioning Robot: the "robot" has to be willing to play the role and not speak up or break in during the exercise
- Constraints: be sure to accomodate students' constraints (as mentioned above, esp. touch aversion and limited sight)
- Tie To Principles: be sure to help the students tie their design insights clearly to formal design principles studied in the class

One issue that is *not* a pitfall: poor design for second iteration.  As long as students improve some elements of the design, you can make them feel successful about those changes.  If other elements prove difficult, these are just lessons about the difficult of design and the individual variation among users.

## Feedback And Use Notes

Feedback: **add your feedback here!**

Use Notes: **add your use notes here!**

- Used Spring of 2005 in a 40 person UI Design course.  Clearly demonstrated some design techniques.  Had some trouble with think-aloud b*c of confusion between voice interface and think-aloud.  (User focused on speaking to robot rather than audience.)  Intro message said "push my hands" to control, which caused an interesting problem: user kept trying to push both hands simultaneously.  Good lesson for students. (Steve Wolfman)

## Related Resources

- The ![LeapFrog](LeapFrog.md) Twist and Shout is a simple but effective toy interface listed in Don Norman's list of good designs: http:**www.jnd.org*[GoodDesign](GoodDesign.md).html