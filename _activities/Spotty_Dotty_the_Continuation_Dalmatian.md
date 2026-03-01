---
title: "Spotty Dotty the Continuation Dalmatian"
layout: activity
---

From: Guest ()
Date: February 16, 2006, 11:51 am

## Spotty Dotty The Continuation Dalmatian

Designed by Steve Wolfman, UBC

## Overview To KLA

Summary: Students learn the essentials of continuations and control flow by acting out a simple recursive "function" with the assistance of a throwable token.  In the original, we used a Beanie Baby Dalmatian named "Spotty Dotty, the Continuation Dalmatian."  The slightly silly, friendly face on continuations makes a challenging topic more fun.

Learning Goals: 

At the end of this exercise, students will...

- understand that a continuation represents all remaining flow of control in the program
- see the connection between true recursion, tail recursion, and continuation lists
- have a powerful reference point to ground their future studies into continuations
- have learned a bit about their classmates and their instructor

Course And Level: Continuations are a challenging topic appropriate for an upper-level programming languages or compilers course or an advanced programming course in a language like Scheme with continuation support.  This KLA could probably also be simplified to focus only on control flow and recursion for an introductory or second CS course.  The variants in the "extra topics" section below should eventually show how to use several techniques to deepen and extend the discussion of various continuation-based techniques.

Class Size: The class size should be more than about 10 (for sufficient distinct people to include in the recursive calls).  A class of 30-60 is probably optimal.  As class size gets significantly larger, students may have trouble seeing, hearing, and understanding the flow of the exercise.

Preparation Time: About 25 minutes fixed preparation time and 5 minutes marginal prep (in subsequent uses).  The instructor needs to collect the appropriate props (which may take more time than 20 minutes if you haven't got something cute and throwable already).  You'll also want to massage the code below into a form that's appropriate for your class and invent some good topics for discussion.  Finally, as always, you'll want to practice with one or two colleagues before "unleashing" the KLA on your students.

Execution Time: 10-25 minutes.  It will definitely take several minutes to nail down the meaning of the code and the sequence of actions that need to be taken.  From there on out, it's a question of how many repetitions you want to perform and how many of the variants below you want to try.  I recommend spending at least 15 minutes on the activity because repeated runs of the "function" let your students learn more about each other and also hammer the idea of continuations home.

## Planning For KLA

Materials: You'll need something soft, throwable, and preferably cute to represent the current locus of control in the program.  I used Dotty the Dalmatian, a Beanie Baby (now known as Spotty Dotty, the Continuation Dalmatian):

spotty-dotty.jpg

You'll also need a "program" to follow.  The program I used was tailored to include real recursion, return values, and some fun interaction.  Here it is in Scheme:

<pre>
(define startup
  (lambda ()
    (let ((topic (choose-a-topic)))
      (announce "The topic is ~s." topic)
      (give-sample-topic-answer)
      (announce-your-name)
      (describe-current-continuation)
      (let ((next-answer (call-on-next-person topic)))
        (announce "~s is a good answer.  Here's mine.." 
          (summarize next-answer))
        (announce (answer topic))))))



(define call-on-next-person
  (lambda (topic)
    (cond ((unwilling-to-participate?)
           (call-on-next-person topic))

          ((have-answer? topic)
           (announce-your-name)
           (describe-current-continuation)
           (let ((next-answer (call-on-next-person topic))
             (announce "~s is a good answer.  Here's mine.." 
               (summarize next-answer))
             (announce (answer topic))))

          (else
           (announce "I'm fresh out of answers!")))))
<*pre>

I posted this code before class so that students could look it over.  I also explained each of the functions that are called:

- unwilling-to-participate? is a predicate that's true iff the current invocation (person) is unwilling to discuss the current topic
- have-answer? is a predicate that's true iff the current invocation (person) can answer the current topic.  (For example, if the current topic is "tell us something about your oldest sibling" and you have no siblings, have-answer? would be false.)
- announce takes a string, speaks it aloud to the class, and also returns it as its result value
- describe-current-continuation is best explained by demonstration in class
- the remaining undefined things are pretty straightforward

You should have the code in some projectable form, and handing out copies to the students is also a good idea.

Preparation: Modify the code above to match your class (changing it to the appropriate language, altering it to fit whatever variants you plan to use, simplifying it, etc.).  Think of a few good topics.  I used things like "describe your oldest sibling (who may be a younger brother or sister if you are the oldest child in the family)", "tell us a sport you like to participate in", or "tell us an odd hobby you have".

As always, read this description carefully and practice the KLA before using it in class!

## Execution Of KLA

Description: Perform the KLA in three phases.  First, run through a few calls yourself.  Then, walk two or three student volunteers through a dry run.  Finally, do as many iterations of the program as you'd like.

When you run through yourself, pretend to be a few different function invocations*people and step through each line of the code.  Be sure to explain what the code does in the abstract and also give examples.  For instance, if I were using the code above:

"We'll always start with the call (startup).  I'll be the function invocation for startup.  My first action is to choose a topic and bind that to the name topic.  Then, I announce the topic by speaking it aloud: *The topic is something interesting about your oldest sibling.*  Next, I give a sample answer so we all understand the topic.  For instance, *My oldest sibling's bachelor party included a cruise from Mexico to Cuba.*  Next, I describe the current continuation.  This means saying out loud ALL the control information needed to complete execution of the program from this point.  That probably doesn't make much sense right now, which is why we're going to work through the exercise.  In this case, I might say something like *After the next person gives their answer, I'll summarize their answer, announce my answer, and we'll be done.*

Now, we get to the heart of the method: I make a call to the function call-on-next-person with the current topic.  We'll simulate that here by choosing someone who isn't already standing (which means they're busy executing a function invocation) by throwing Spotty Dotty to that person.  For the moment, I'll just toss it to myself..

Now, let's imagine I'm a student.  I catch the Dalmatian and stand up to start executing the call-on-next-person function.  If I'm not willing to participate in the Spotty Dotty exercise, I just pass the Dalmatian on without saying anything, and my invocation is done.  Otherwise, if I have an answer, I state my name, I describe the current continuation, I call on another person in turn, and when they're done, I summarize the answer to the topic that they gave and give my own answer.  Once I give my answer, I'm done, and I can throw Spotty Dotty back to the person who called me.  The flow of control returns to them, and the value they get back is my answer to the topic!

If I am willing to participate, but I don't have an answer, I announce that I'm fresh out of answers, and that becomes my return value.  Again, I pass Spotty Dotty back to my caller, who continues execution of the program.  When we eventually pop all the way back up to the first call to startup, the startup invocation (me!) wraps up by summarizing the previous answer, giving his own answer, and ending the program."

For the dry run, talk students carefully through the steps of the program and ESPECIALLY the description of the current continuation.  It's crucial that they build up a chain like: *After the next person gives their answer, I'll summarize their answer, I'll announce my answer, Nathan will summarize my answer and announce his, Katherine will summarize his answer and announce hers, Eugene will summarize her answer and announce his, Steve will summarize Eugene's answer and announce his own, and we'll be done.*

Furthermore, make clear that this verbal description of the continuation is all anyone would need to finish the program from that point.  Also, point out that if, say, Oliver is unwilling to participate and passes Spotty Dotty on to Nathan, then Oliver is NOT part of the continuation list because there is no work for him to do.  His call is tail recursive and does not add to the length of the continuation list!  Ideally, this should wait until someone is unwilling to participate.  Making the token a Beanie Baby helps encourage that decision for some people! :)

Once you have the dry run done, start the process going with a topic or three more.  Try NOT to be the one to correct misstatements of the current continuation or violations of the algorithm.  Get the students supporting and correcting each other in that.  For your part, ensure that you include different students at the start of the chain, set an example of tossing the Beanie Baby far across the classroom, disclose interesting information, and solicit topics (if you feel comfortable handling them on the fly).

**Variants And Extra Topics**: 

*Fill in a list of variants of and extensions to your KLA. Make the list as in the following:*

- Extra Topic One: describe the extra topic here

*Make sure that the title of each extra topic is capitalized.*

## Constraints On KLA

Would your KLA work if your students had the following constraints:
- Limited Vision: (including color-blindness) yes, with modifications
- Limited Hearing: yes, with a key modification
- Limited Mobility: yes
- Trouble Speaking: yes, with modification
- Touch Aversion: (including cultural) yes
- Other:

One of the key elements of this KLA is the repeated statement of the current continuation aloud for all students to hear.  Constraints that relate to this element would be the most difficult to accomodate and still use this KLA successfully.  Students with difficulty speaking can still easily observe the KLA.  Students with limited hearing will have trouble performing that observation.

Two reasonable modifications to alleviate this are to emphasize the visual aspect of the KLA (with much pointing and gesturing), which will probably improve the experience for all students without limited vision, anyway, and to express the continuation descriptions in a SHARED written form.  Note that the shared part is absolutely crucial, since all students (not just the one performing the description) need to take in the description.  Writing it on a whiteboard or overhead projector should work.  Mobile students could do the writing themselves, or the instructor could write for them.

Students with limited vision may not be able to catch the thrown control flow token, but it's a simple matter to pass it gently or toss it to a neighbour (and in my experience, the tossed Dalmatian often goes astray, regardless!).

## Pitfalls Of KLA

*What common problems or slip-ups should instructors using your KLA look out for?  Think of pedagogical pitfalls (e.g., students taking the metaphor of the call stack being like a row of students too literally), logistical pitfalls (e.g., the steep rake in many lecture halls will interfere with data movement in the grid multiprocessor simulation), and "environment" pitfalls (e.g., students should avoid use of abusive language while anthropomorphically role-playing various computing platforms or other problems that may lead to a negative classroom environment for one or more students).*

## Feedback And Use Notes

*Leave the feedback section blank (don't give feedback on your own KLA!), but you should be able to add at least one entry to "Use Notes".  Replace the template provided below, including the information most relevant to your KLA.*

Feedback: **add your feedback here!**

Use Notes: **add your use notes here!**

- *Used Fall of 1973 in a 4500 person CS2 course.  Some comments about that use; perhaps how the use relates to variants, pitfalls, or optimal class type. (Author Name)*

## Related Resources

*You or later users of the wiki can add links (that don't fit into the text above) to related discussions, papers, repositories, examples, etc.*