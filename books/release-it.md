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

## Chapter 3: Stabilise Your System

Enterprise software must be cynical - expects bad things to happen and is never surprised when they do. It doesn't even trust itself, it refuses to get too intimate with other systems, because it could get hurt.

Poor stability means real costs - millions lost for example in lost transaction in trading system, reputation loss. On the other hand, good stability does not necessarily cost a lot. Highly stable design usually costs the same to implement as the unstable one.

Transaction - abstract unit of work processed by the system.

Impulse - rapid shock to the system. For example rumor about a new console, causes impulse on the manufacturer's website or celebrity tweet. Things that can fracture (break) the system in a blink of an eye.

Stress - a force applied to the system over an extended period. 

The major dangers to system's longevity are memory leaks and data growth, difficult to catch during tests. Applications never run long enough in development environment to reveal longevity bugs. 

Failures will happen, you have ability to prepare system for specific failures (like car engineers areas designated to protect passengers by failing first). It is possible to create failure modes that protect the rest of the system. 

Lees-couples architectures act as shock absorbers, diminishing the effect of the error instead of amplifying them.

Terminology:

- Fault - a condition that creates an incorrect internal state in the software.
- Error - visibly incorrect behaviour, eg. trading system buying 10M Pokemon futures
- Failure - an unresponsive system

Chain of failure: Triggering a fault opens the crack, faults become errors and errors provoke failures. On each step, a fault may accelerate. Tight coupling accelerate cracks. 

One way to prepare for every possible failure is to look at every external call, every I/O, every use of resources, and ask WHAT IF IT:  can't make connection, takes 10 minutes to make the connection, makes connection and then disconnects, takes 10 minutes to respond my query, 10k requests arrive at the same time, ...?

IT community is divided into 2 camps: 

1. Make system fault-tolerant, catch exceptions, check error codes, keep faults from becoming errors
2. "let it crash", so you can restart from a good known state

## Chapter 4: Stability Antipatterns

Antipatterns that can wreck the system, they create, accelerate or multiply cracks in the system. These bad behaviours should be avoided. 

You have to set the socket timeout if you want to break out of blocking call, for example request may be stuck in the listening queue for minutes or forever. Network failure can hit you in 2 ways: fast (immediate exception, eg. connection refused) or slow (dropped ACK). The blocked thread can't process other transactions, so overall capacity is reduced. If all threads are blocked, from practical point of view, the server is down. 

Sometimes not every problem can be solved at the level of abstraction where it manifests. Sometimes the causes reverberate up and down the layers. You need to know how to drill through at least two layers of abstraction to find the reality at that level in order to understand problems.

REST with JSON over HTTP is the lingua franca for services today. HTTP-based protocols have their own issues:

- TCP connection can be accepted but never respond to HTTP request
- provider may accept the connection but not read the request
- provider may send back a response the caller doesn't know how to handle
- provider may send back a response with a content type the caller doesn't expect or know how to handle
- provider may claim to be sending JSON but in actually sending plain text

Treat response as data until you have confirmed it meets your expectations.

Libraries can have bugs too, they all have the variability in quality, style, and safety that you see from any other random sampling of code.

The most effective stability patterns to combat integration points failures are *Circuit Breaker* and *Decoupling Middleware*.

BEWARE NECESSARY EVIL - every integration point will fail in some way, you need to be prepared.

PREPARE FOR MANY FORMS OF FAILURE - failure may take several forms: network errors, semantic errors, slow response, ...

KNOW WHEN TO OPEN UP ABSTRACTIONS - debugging integration point failures usually requires peeling back a layer of abstraction

FAILURES PROPAGATE QUICKLY - failure in remote systems quickly becomes your problem, when your code isn't defensive enough

APPLY PATTERNS TO AVERT INTEGRATION POINT PROBLEMS - use patterns like Circuit Breaker, Timeouts, Decoupling Middleware and Handshaking - discussed later

Horizontal scaling - adding capacity through adding more servers, fault tolerance through redundancy. Vertical scaling - scaling by building bigger and bigger servers (more cores, memory and storage).

RECOGNISE THAT ONE SERVER DOWN JEOPARDISED THE REST - a chain reaction can happen because the death of one server makes the others pick up the slack

HUNT FOR RESOURCE LEAK - mos of time, chain reactions happens when application has a memory leak

HUNT FOR OBSCURE TIMING BUGS - race conditions can be triggered by traffic, if one server dies because of deadlock, the increased load on the others makes them more likely to hit the deadlock too

USE AUTOSCALING - create health-checks for every autoscaling group, the scaler could shut down instances that fail their health checks and start new ones

DEFEND WITH BULKHEADS - partitioning servers with Bulkheads - more details later.

Cascading failures - occurs when a crack in one layer triggers a crack in a calling layer. If caller handles errors badly it will start to fail, resulting in cascading failure (for example database failure is going to impact any system that is calling the database). Every dependency is a chance for a failure to cascade.

- a cascading failure often results from a resource pool (eg. connection pool) that gets exhausted, safe resource pools always limit the time a thread can wait to check out a resource
- defend with timeouts and circuit breaker 

Capacity is the maximum throughput your system can sustain under a given workload while maintaining acceptable performance. Breaking limits creates cracks in the system. Limits:

- heap memory - for example in memory-based sessions, memory can get short- many things can go wrong: out-of-memory exceptions, not working logging. It is possible to use Weak References - Garbage Collection may reclaim memory if it is too low (before out-of-memory error occurs). Callers have to behave nicely when payload is gone. Weak references are useful  but they do add complexity. 
- off-heap memory, off-host memory - for example Redis, but this is slower than local memory and there is a problem with replication
- number of sockets on the server is limited, every request corresponds to an open socket, the OS assigns inbound connections to an ephemeral port that represents the receiving side of the connection. Because of TCP packet format, one server can have up to 64 511 connections open. How can we serve millions of concurrent connections? The virtual IP addresses. 
- closed sockets can be problematic too - before socket can be reused it goes through couple of states, for example bongos defence algorithm. Bogon is a wandering packet that got routed inefficiently and arrives late (out of sequence), if socket were reused too quickly, late packet could trigger response.





