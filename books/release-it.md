[go back](https://github.com/pkardas/learning)

# Release It! Design and Deploy Production-Ready Software

Book by Michael T. Nygard (Second Edition)

[TOC]

## Chapter 1: Living in Production

"Feature complete" doesn't mean it is "production ready". A lot of bad things can happen on production (crazy users, viruses, high traffic, ...). Production is the only place to learn how the software will respond to real-world stimuli, hence software should be delivered to production quickly and gradually.

Most software architecture and design happens in clean and distant from production environments. 

Design and architecture decisions are also financial decisions (downtime, resource usage, ...). It is important to consider availability, capacity and flexibility when designing software. Pragmatic architect should consider dynamic of change. 

## Chapter 2: Case Study: The Exception That Grounded an Airline

A tiny programming error starts the snowball rolling downhill.

In any incident, author's priority is always to restore service. Restoring service takes precedence over investigation. If it is possible to gather some data for postmortem analysis, that's great - unless it makes the outage longer. The trick to restoring the service is figuring out what to target. You can always "reboot the world" by restarting every single server, layer by layer but that's not effective. Instead be a doctor diagnosing a disease, look at the symptoms and figure what disease to treat. 

A postmortem is like a murder mystery, there are set of clues - some are reliable like logs, some are unreliable like comments from people, there is no corpse - the servers are up and running, the state that caused the error no longer exists. 

Log analysis helped to identify the root cause. 

Bugs are inevitable, how to prevent bugs in one system from affecting everything else?  We are going to look at design patterns that can prevent this type of problem from spreading. 



