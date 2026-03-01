---
title: "Network Routing on Strings"
layout: activity
---

From: anonymous (noone@nowhere.com)
Date: January 2, 2007, 12:52 pm

## Network Routing On Strings

Designed by Tammy [VanDeGrift]({{ "/activities/VanDeGrift/" | relative_url }}) and Sarah Schwarm

## Entered by Steven Wolfman

## Overview To KLA

Summary: Students simulate the operation of a network (of routers) using notecards to represent packets and string to represent network links.  

Learning Goals: By the end of this exercise, students will have discovered and resolved many of the following common networking issues...

- route discovery and routing
- the need for packet fragmentation
- key meta-data necessary for packets (including packet length*offset-style information once they've fragmented packets)
- responses to network failures (such as overburdened routers and broken links)
- the need for acks
- distinction between a "god's-eye" and "in-the-trench" view of the network

Course And Level: This KLA seems most appropriate a 2nd-year course that discusses networks, but it has been used in a CS0 course as well.

Class Size: Probably best with ~6-12 students participating directly.  Larger classes can observe (and the distinction between "in the experiment" and "above the experiment" is pedagogically valuable).

Preparation Time: ~20 minutes pre-class (mostly materials gathering) and ~5 minutes in class

Execution Time: 10-25 minutes, depending on the number of points and level of depth you want to work on; relatively easy to tune within this range


## Planning For KLA
Materials: You'll need..

- String (probably not precut so you can be flexible about spacing)
- Scissors
- Abundant 3x5 notecards
- Fat black marker

Preparation: Before class, be sure you have a sense of which networking ideas you'd like to emphasize.  To an extent, the students will develop problems and solutions themselves, but the way you design the network and the way you pose and guide the exercise will heavily influence their discovery process.

Sketch out roughly what you'd like the network to look like.  Most likely, you want multiple routes of different hop lengths from a sender to a receiver.  Possibly, you want to plan a link to cut.  You may also want to have a flexible plan that can accommodate different numbers of student participants depending on your class (which is easy by adding nodes with just two links).

For simplicity, it's helpful for the sender and the receiver to each have exactly one link to their local router.  (This is also realistic in many cases.)

Prepare a simple (but sufficiently long) message to be sent across the network (or have students think of one in class).

As always, read this description carefully and practice the KLA before using it in class!

## Execution Of KLA

Description: Bring student volunteers to the front and arrange them roughly into your desired topololgy.  They are the nodes in the network.

For a large class (where most students are not directly participating) and with students who trust you, have the participants close their eyes before you move them into position.  This emphasize the god's-eye vs. local view aspect.

Have students introduce themselves to each other and the class, but don't mention who is the sender and who is the receiver.

Cut off a piece of string for each network link and hand one end to each router in the link.

As you go, explain the rules of the network:

- messages travel through the network on notecards
- student-nodes should try to avoid looking around during the exercise but can (and should!) look at the packets they receive
- a notecard can travel freely down one string*link to the next node, but students will need to figure out how to send notecards greater distances
- each link can pass along one notecard*packet at a time
- for the purposes of the exercise, students*nodes can communicate with neighbouring students along a string to figure out information about the network (to get a neighbour's attention with your eye's closed, just tug on their string)

Hand the marker and notecards to the sender and ask them to prepare their message.  Make a point of whispering the message and the intended recipient, but be sure to talk aloud through the rest of the exercise to keep the class and especially the students with their eyes closed engaged in the exercise!

Now, let the students go.

Occasionally, have a router drop a packet because it is "overburdened" or come in with your scissors and cut a physical link.

From this point on, students should discover issues like:

- with a long message, small notecards, and a fat marker, the message will not all fit on one card
- when the message hits the network, the routers don't know where to send it unless the recipient is on each card
- no one in the network knows the topology; so, they have to discover routes
- they must find a way to choose among alternate routes

Be sure to play devil's advocate to stress these issues and to bring up other issues.  E.g., if students include serial numbers in packet headers but not a total number of packets in the message, cause a router to drop the last couple of packets and ask what the receiver will think.

Other issues that can arise:

- need for acks in order to resend dropped packets
- weakness of the metaphor in using physical notecards for packets (rather than easily copied digital data)
- discussion of how and when to send meta-data through the network
- out-of-order packet delivery
- discussions of cost besides number of hops
- security, privacy, and trust

**Variants And Extra Topics**: 

- IP Comparison: compare the students' header information against the header data actually included in IP packets; discuss what's added or missing
- Multiple Sender*Receiver Pairs: have more than one student sending*receiving messages at the same time.  Stresses complexity of routing problem and the need for reasonable data structures for routing tables and protocols for keeping them up-to-date.  Multiple senders and one receiver also brings up good issues with reassembly of messages.
- TCP And Acks: have the students develop or simulate a reliable transmission protocol using acknowledgment packets

## Constraints On KLA

Would your KLA work if your students had the following constraints:
- Limited Vision: (including color-blindness)
- Limited Hearing: 
- Limited Mobility:
- Trouble Speaking:
- Touch Aversion: (including cultural)
- Other:

This KLA can potentially work well for students with limited mobility even in the network itself (if they can reach an area where they can hold string*links), but its reliance on both visual and auditory information could make it challenging for students who either have limited vision or limited hearing.  Of the two, limited vision is probably easiest to accommodate, at least in the network itself (simply read packets aloud as they're passed around).  

The KLA should not be a problem for students with trouble speaking or touch aversion (as long as the instructor is sensitive when "laying out" the network).

## Pitfalls Of KLA

The two key roles of the instructor in this KLA are:

- ensure that students actually discover the problems that arise.  (It's easy to work around a problem through "illicit" means, like not noticing that the recipient has to be on the packets because everyone heard who the message was to.)
- keep the whole class engaged in the problem discovery and solution process, both by narrating what's happening and by getting students both in the network and outside to talk out loud about what's happening and what problems are occurring

There are several weaknesses to the metaphor, such as the fact that cards are physical individuals rather than easily-copied digital data.  

Finally, string can get tangled, especially if any one node connects to too many neighbours!

## Feedback And Use Notes

Feedback: **add your feedback here!**

Use Notes: **add your use notes here!**

- Used Summer of 2006 in a 60 person CS0 course.  The exercise worked beautifully to demonstrate a variety of routing issues to students who had absolutely no prior experience with computing (in the first week of the class).

## Related Resources

- Header information used in the Internet Protocol (IP): http://www.erg.abdn.ac.uk/users*gorry*course*inet-pages*ip-packet.html