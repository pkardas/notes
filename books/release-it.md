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

Cookies are a clever way to pass state back and forth from client to server and vice versa. They allow all kinds of new applications, such as personalised portals and shopping sites. Cookies carry small amount of data because they need to be encrypted and this is CPU heavy task.

A session is an abstraction that makes building applications easier. All the user really sends are series of HTTP requests, the server receives them, compute and returns response. Sessions are about caching data in memory. 

Truly dangerous users are the ones that target your website, once you are targeted, you will almost certainly be breached. 

Adding complexity to solve one problem creates the risk of entirely new failure modes, eg. multithreading - enables scalability but also introduces concurrency errors. 

Caching can be a powerful response to performance problem, however caching can cause troubles - it can eat away at the memory available for the system, when that happens the garbage collector will spend more and more time attempting to recover enough memory to process requests. You need to monitor hit rates for the cached items to see whether most items are being used from cache. **Caches should be built using weak references to hold the cached item itself.** It will help the GC reclaim the memory. 

Libraries are notorious sources of blocking threads.

Self-Denial Attack - any situation in which the system conspires against itself. For example a coupon code sent to 10k users to be used at certain date is going to attract millions of users (like XBOX preorder). Self-Denial can be avoided by building a shared-nothing architecture (no databases nor other resources)  - ideal horizontal scaling. Talk to marketing department when they are going to send out mass emails - you will be able to pre-scale (prepare some additional instances for increased load). Also be careful for open links to the resources, also watch out for Fight Club bugs - increased front-end load causes exponentially increasing backend processing. 

WIth point-to-point connections, each instance has to talk directly to every other instance - this means O(n^2) scaling - be careful. Point-to-point communication can be replaced by: UDP broadcasts, TCP/UDP multicast, pub/sub messaging, message queues.

XP principle: Do the simplest thing that will work. 

Watch out for shared resources - they can be a bottleneck, stress-test it heavily, be sure clients will keep working despite malfunctioning resource. 

Frontend always has the ability to overwhelm the backend, because their capacities are not balanced. However you can not build every service to be large enough to serve enormous load from the frontend - instead you myst build services to be resilient in the face of tsunami od requests (eg. Circuit Breaker, Handshaking, Back-pressure, Bulkheads). 

Dog-pile - when a bunch of servers impose transient load all at once (term from American football). Can occur: when booting all servers at once, on cron job, when the config management pushes out a change. Use random clock slew to diffuse the demand from cron job (every instance does something at different time). Use a backoff algorithm so every client retries at different time. 

Infrastructure management tools can cause a lot of trouble (eg. Reddit outage) - build limiters and safeguards into them so they won't destroy entire system at once. 

Slow response is worse than refusing a connection or returning an error - because ties up resources in the calling system and in the called system. Slow responses usually result from excessive demand. System should have the ability to monitor its own performance, so it can also tell when it isn't meeting its SLAs (service-level agreement).

Why slow responses are dangerous: because they trigger cascading failures, users hitting *reload* button cause even more traffic to already overloaded system. If system tracks its own responsiveness, then it can tell when it is getting slow. In such situation developer should consider sending an immediate error response. 

>  Design with scepticism, and you will achieve resilience. Ask "What can system X do to hurt me" and then design a way to dodge whatever wrench your supposed ally throws.

Use realistic data volumes - typical development and test data sets are too small to exhibit problems, you need production size-data to see what happens when your query returns a million rows that you turn into objects. Calls should be paginated. Do not rely on data providers, once they will go *berserk* and fill up a table for no reason.

## Chapter 5: Stability Patterns

Healthy patterns to reduce, eliminate or mitigate the effects of cracks in the system. Apply patterns wisely to reduce the damage done by an individual failure.

TIMEOUTS - Today every application is a distributed system, every system must grapple with the fundamental nature of networks - they are fallible. When any element breaks, code can't wait forever for a response that may never come - sooner or later. *Hope is not a design method*. 

Timeout is a simple mechanism allowing you to stop waiting for an answer once you think it will not come. Well placed timeouts provide fault isolation - **a problem in some other service does not have to become your problem**.  

Timeouts can also be relevant within a single service. Any resource pool can be exhausted. Any resource that block threads must have a timeout to ensure that calling threads eventually unblock. 

Timeouts are often found in the company of retries, fast retries are very likely to fail again (wait between retries). 

CIRCUIT BREAKER - in the past houses were catching fire because of heated wires, when too many appliances were connected to the power source. Energy industry came up with a device that fails first in order to prevent fire. 

The circuit breaker exists to fail without breaking the entire system, furthermore once the danger has passed , the circuit breaker can be reset to restore full function to the system.

The same technique can be applied to software, dangerous operations can be wrapped with a component that can circumvent call when the system is not healthy.

In closed state, the circuit breaker executes operations as usual (calls to another system or other internal operations that are subject to timeout or other failure), if it fails, the circuit breaker makes a note of the failure. Once the number of failures exceeds a threshold, the circuit breaker opens the circuit. When the circuit is open, calls are suspended - they fail immediately. After some time the circuit decides the operation has a chance of succeeding so it goes to the half-open state, if call succeeds - goes to the open state, if not - returns to the open state. 

The circuit breaker can have different thresholds for different types of failures. Involve stakeholders to decide how system should behave when circuit is open. 

How to measure number of failures - interesting idea is Leaky Bucket - separate thread counting failures and periodically removing them. If buckets becomes empty quickly it means, the system is flooded with errors. 

It should be possible to automatically open/close circuit. 

Circuit Breaker - don't do it if it hurts. Use it with timeouts. Ensure proper reporting of opened circuit.

BULKHEADS - in a ship, bulkheads prevents water from moving from one compartment to another. You can apply the same technique, by partitioning the system, you can keep  a failure in one part of the system from destroying everything. This can be achieved by for example running application on multiple servers - if one fails we still have redundancy (eg. instances across zones and regions in AWS). 

Bulkheads partitions capacity to preserve partial functionality when bad things happen. Granularity should be picked carefully - thread pools in the application, CPUs, servers in a cluster. Bulkheads are especially useful in service-oriented or micro-service architectures in order to prevent chain reactions and entire company go down. 

STEADY STATE - every time human touches a severer it is an opportunity for unforced errors. It is best to keep people off production systems to the greatest extent possible. People should treat servers as "cattle", not "pets", they should not be logged to the server all the time to watch if everything is fine. 

The Steady State pattern says that for every mechanism that accumulated a resource (log files, rows in the database, caches in memory), some other mechanism must recycle that resource. Several types of sludge that can accumulated and how to avoid the need for fiddling:

- data purging - easy to do, however can be nasty, especially in relational databases there is a risk of leaving orphaned rows, also you need to make sure application will work when the data is gone. 
- log files - logs are valuable source of information, however if left unchecked are risk. When logs fill up the filesystem, they jeopardise stability. Configure log file retention based on size. Probably best you can do is to store logs on some centralised server (especially if you are required to store logs for years because of compliance regime). Logstash - centralised server for logs, where they can be indexed, searched and monitored. 
- in-memory caching - improper usage of caching is the major cause of memory leaks, which in turn lead to horrors like daily server restarts. Limit the amount of memory a cache can consume. 

Steady State encourages better operational discipline by limiting the need for system administrators to log on to the production servers. 

FAIL FAST - if the system can determine in advance that it will fail; at an operation, it is always better to fail fast - the caller does not have waste its capacity for waiting. No, you don't need Deep Learning team to tell whether it will fail. Example: if call requires database connection, application can quickly check if database is available. Other approach is to configure load balancer appropriately (no servers - reject request). Use request validation to know if data is correct.

The Fail Fast pattern improves overall system stability by avoiding slow responses.

LET IT CRASH - there is no way to test everything or predict all the ways a system can break. We must assume that errors will happen. 

There must be a boundary for trashiness. We want to crash a component in isolation, the rest of the system must protect itself from a cascading failure. In a micro-service architecture, a whole instance of the service might be the right granularity.

We must be able to get back to clean state and resume normal operation as quickly as possibile - otherwise we will see performance degradation. 

Supervisors need to keep close track of how often they restart child processes. It might be necessary to restart supervisor. Number of restarts can indicate that either the state is not sufficiently cleaned up of the system is in jeopardy and the supervisor is just masking the underlying problem. 

The final element of a "let it crash" is reintegration - the instance must be able somehow to join the pool to accept the work. This can be done through health checks on instance level.

HANDSHAKING - can be most valuable when unbalanced capacities are leading to slow responses. If the sever can detect that it will not be able to meet its SLAs, then it should have some means to ask the caller to back off. It is an effective way to stop cracks from jumping layers, as in the case of a cascading failure.

The application can notify the load balancer through a health check that is is not able to take more requests (503 - Not Available), then the load balancer knows not to send any additional work to that particular server. 

TEST HARNESSES - you can create test harnesses to emulate the remote system on the other end of each integration point. A good test harness should be as nasty and vicious as real-world systems will be. 

A test harness runs as a separate server, so it is not obliged to conforms to the defined interface. It can provoke network errors, protocol errors or application level errors. 

Consider building a test harness that substitutes for the remote end for every web services call. 

Integration testing environments are good at examining failures only in the seventh layer of the OSI model (application layer) - and not even all of those. 

The test harness can be designed like an application server - it can have pluggable behaviour for the tests that are related to the real application. Broadly speaking, a test harness leads toward "chaos engineering".

The Test Harness pattern augments other testing methods. It does not replace unit tests, acceptance test, penetration tests and so on. 

DECOUPLING MIDDLEWARE - middleware is a graceless name fo tools that inhabit a singularly messy space - integrating systems that were never meant to work together. The connective tissue that bridges gaps between different islands of automation. 

Middleware, integrates systems by passing data and events back and forth between systems, decouples them by letting the participating systems remove specific knowledge of and calls to the other systems. 

Tightly coupled middleware amplifies shocks to the systems, synchronous calls are particularly vicious amplifiers that facilitate cascading failures (this includes JSON over HTTP).

Message oriented middleware decouples the endpoints in bots space and time, because the requesting system doesn't just sit around and wait for a reply. This form of middleware cannot produce a cascading failure. 

SHED LOAD - applications have zero control over their demand, at any moment, more that a bilion devices could make a request.

Services should model TCPs approach: When load gets too high, start to refuse new requests for work. This is related to Fail Fast.

The ideal way to define "load is too high" is for a service toi monitor its own performance relative to its SLA. When requests take longer than SLA, it is time to shed some load. 

CREATE BACK PRESSURE - every performance problem starts with a queue backing up somewhere, if a queue is unbounded, it can consume all available memory. As queue's length reaches toward infinity, response time also heads toward infinity. 

Blocking the producer is a kind of flow control. It allows the queue to apply "back pressure" upstream. Back pressure propagates all the way to the ultimate client, who will be throttled down in speed until the queue releases.

TCP uses back pressure - once the window is full, senders are not allowed to send anything until released. 

GOVERNOR - machines are great ant performing repetitive tasks, humans are great at perceiving high level situation. 

In 18th century steam engineers discovered it is possible to run machines so fast that the metal breaks. The solution was the governor - a person which limits the speed of an engine.

We can create governors to slow down the rate of actions. A governor is stateful and time-aware, it knows what actions have been taken over a period of time. (Reddit uses a governor to slow down the autoscaler, by adding logic that says it can only shut down a certain percentage of instances at a time).

The whole point of a governor is to slow things down enough for humans to get involved. 

## Chapter 6: Case Study: Phenomenal Cosmic Powers, Itty-Bitty Living Space

Launching a new site is like having a baby. You must expect certain thing, such as being awakened in the middle of the night. Monitoring technology provides a great safety net, pinpointing problems when they occur, but nothing beats the patter-matching power of the human brain.

Response time is always a lagging indicator. You can only measure the response time on requests that are done. So whatever your worst response time may be, you can't measure it until the slowest requests finish. Requests that didn't complete never got averaged in. 

Recovery-Oriented Computing - principles:

- Failures are inevitable, in both hardware and software.
- Modeling and analysis can be never sufficiently complete. A priori prediction of all failure modes is not possible.
- Human action is a major source of system failures.

Investigations aim to improve survivability in the face of failures. The ability to restart single components, instead of entire servers, is a key concept of recovery-oriented computing.

## Chapter 7: Foundations

Designing for production means thinking about production issues as first-class concerns (network, logging, monitoring, runtime control, security, people who do operations). There are several layers of concerns:

1. Operations - security, availability, capacity, status, communication
2. Control Plane - system monitoring, deployment, anomaly detection, features
3. Interconnect - routing, load balancing, failover, traffic management
4. Instances - services, processes, components, instance monitoring
5. Foundation - hardware, VMs, IPs

Virtualisation promised developers a common hardware appearance across the bewildering array of physical configurations in the data centre. On the down side, performance is much less predictable. Many virtual machines can reside on the same physical hosts.It is rare to move VMs from one host to another. 

When designing applications to run in virtual machines you must make sure that they are not sensitive to the loss or slowdown of any of the host.

A clock on the VM is not monotonic and sequential, because VM can be suspended for an indefinite span of real time. The bottom line is: don't trust the OS clock. If external time is important, use an external source like a local NTP server. 

Containers have short-lived identity. As a result, it should not be configured on a per-instance basis. Container won't have much, if any, local storage, so the application must rely on external storage for files, data, and maybe even cache.

When you design an application for containers, keep a few things in mind: the whole container image moves from environment to environment, so the image can't hold things like production database credentials. Containers should not contain hostnames or port numbers - because the setting needs to change dynamically while the container image stays the same. Containerised applications need to send their telemetry out to a data collector.

The 12-Factor App [12factor.net] - created by engineers at Heroku, is a succinct description of a cloud-native, scalable, deployable application:

1. Codebase - track one codebase in revision control. Deploy the same build to every environment.
2. Dependencies - explicitly declare and isolate dependencies.
3. Config - store config in the environment.
4. Backing services - treat backing services as attached resources.
5. Build, release, run - strictly separate build and run stages.
6. Process - execute the app as one or more stateless processes.
7. Port binding - export services via port binding.
8. Concurrency - scale out via process model
9. Disposability - maximise robustness with fast startup and graceful shutdown.
10. Dev-prod parity - keep environment, staging and production as similar as possible.
11. Logs - treat logs as event streams.
12. Admin processes - run admin / management tasks as one-off processes.

## Chapter 8: Processes on Machines

Service - a collection of processes across machines that work together to deliver a unit of functionality.

Instance - an installation on a single machine out of a load-balanced array of the same executable. 

Executable - an artefact that a machine can launch as process and created by build process.

Process - an operating system process running on a machine.

Installation - the executable and any attendant directories, configuration files and other resources.

Deployment - the act of creating an installation on a machine.



Developers should not do production builds from their now machines. Developer boxes are hopelessly polluted. We install all kinds of junk on these systems, play games and visit sketchy websites. Only make production builds on a CI server, and have it put the binary into a safe repository that nobody else can write into.

Configuration management tools like Chef, Puppet and Ansible are all about applying changes to running machines. They use scripts, playbooks or recipes to transition the machine from one state to a new state.

We don't want our instance binaries to change per environment, but we do eat their properties to change. That means the code should look outside the deployment directory to find per-environment configurations.

ZooKeeper and etc are popular choices for a configuration service - but any outage to these system can cause a lot of trouble. 

Shipboard engineers can tell when something is about to go wrong by the sound of the giant Diesel engines. We must facilitate that awareness by building transparency into our systems. Transparency refers to the qualities that allow operators, developers and business sponsors to gain understanding of the system's historical trends, present conditions, instantaneous state and future projections. Debugging a transparent system I s vastly easier, so transparent systems will mature faster that opaque ones. System without transparency cannot survive long in production. 

Transparency arises from deliberate design and architecture. Instances should log their health and events to a plain old text file. Any log-scraper can collect these without disturbing the server process. Logging is certainly a white-box technology, it must be integrated pervasively into the source code.

Not every exception needs to be logged as an error. Just because a user entered a bad card number and the validation compound threw an exception doesn't mean anything has to be done about it. Log errors in business logic or user input as WARNINGs. Reserve ERROR for a serious system problem.

Logs have to present clear, accurate and actionable information to the humans who read them.

Message should include an identifier that can be used to trace the steps of a transaction.

Health Checks should be more that just "yup, it is running", it should report at least: IP, interpreter version, application version, if instance is accepting work, the status of connection pools, caches and circuit breakers. Load balancer can use the health check for the "go live" transition too. When the health check on a new instance goes from failing to passing, it means the app is done with its startup.

## Chapter 9: Interconnect

The interconnect layer covers all the mechanisms that knit a bunch of instances together into a cohesive system. That includes a traffic management. Load balancing and discovery. This is the layer where we can really create high availability. 

Consul - dynamic discovery service, suited for large teams with hundreds of small services. On the other hand small business with just a few developers would probably stick with direct DNS entries. 

DNS might be the best choice for small teams, particularly in a slowly changing infrastructure. When using DNS, it is important to have a logical service name to call, rather than physical hostname. Even if that logical name is just an alias to the underlying host, it is still preferable. DNS round robin an easy approach to load balancing but suffers from putting too much control in the client's hands. DNS outage can be serious, do it should not be hosted on the same infrastructure as production system. There should be more than one DNS provider with servers on different locations. 

Almost everything we build today uses horizontally scalable farms of instances that implement request/reply semantics. Horizontal scaling helps with overall capacity and resilience, but it introduces the need for load balancing. Load balancing is all about distributing requests across a pool of instances to serve all requests correctly in the shortest feasible time. 

Software Load Balancing - low cost approach, uses an application to listen for requests and dole them out across the pool of instances. This is basically a reverse proxy (proxy - multiplexes any outgoing calls into a single source IP address, reverse proxy - demultiplexes calls coming into a single IP address and fans them out to multiple addresses). Examples: squid, HAProxy, Apache httpd, nginx.

Hardware Load Balancing - specialised network devices that serve a similar role to the reverse proxy server. They provide better capacity and throughput because they operate closed to the network.

One of the most important services a load balancer can provide is service health checks. The load balancer will not send to an instance that fails a certain number of health checks. 

Load balancers can also attempt to direct repeated requests to the same instance. This helps when you have stateful services, like user session state in an application server. Directing the same requests to the same instances will provide better response time for the caller because necessary resources will already be in that instance's memory. A downside of sticky sessions is that they can prevent load from being distributed evenly. 

Another useful way to employ load balancer is "content based routing". For example, search requests may go to one set of instances, while user-signup requests go somewhere else.

Demand Control - when, where and how to refuse to work under big demand.

> Every failing system starts with a queue backing up somewhere.

Going nonlinear - service slowing down under heavy load, this means fewer and fewer sockets available to receive requests exactly when the most requests are coming in. 

Load shedding - under high load, turning away work system can't complete in time, the most important way to control incoming demand. We want to shed load as early as possible, so we can avoid tying up resources at several tiers before rejecting the request. Service should measure its response time and present it in the health check. 

Service discovery. Services can announce themselves to begin receiving a load. A caller needs to know at least one IP address to contact a particular service. Service discovery is itself another service, it can fail or get overloaded. Service discover can be built on top of a distributed data store such as ZooKeeper or etc. 

In CAP theorem, ZooKeeper is a CP system - when there is a network partition, some nodes will not answer queries or accept writes. HashiCorp's Consul resamples ZooKeeper, however Consul's architecture places it in the AP area - it prefers to remain available and risk stale information when a partition occurrs.
