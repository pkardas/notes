[go back](https://github.com/pkardas/learning)

# Release It! Design and Deploy Production-Ready Software

Book by Michael T. Nygard (Second Edition)

- [Chapter 1: Living in Production](#chapter-1-living-in-production)
- [Chapter 2: Case Study: The Exception That Grounded an Airline](#chapter-2-case-study-the-exception-that-grounded-an-airline)
- [Chapter 3: Stabilise Your System](#chapter-3-stabilise-your-system)
- [Chapter 4: Stability Antipatterns](#chapter-4-stability-antipatterns)
- [Chapter 5: Stability Patterns](#chapter-5-stability-patterns)
- [Chapter 6: Case Study: Phenomenal Cosmic Powers, Itty-Bitty Living Space](#chapter-6-case-study-phenomenal-cosmic-powers-itty-bitty-living-space)
- [Chapter 7: Foundations](#chapter-7-foundations)
- [Chapter 8: Processes on Machines](#chapter-8-processes-on-machines)
- [Chapter 9: Interconnect](#chapter-9-interconnect)
- [Chapter 10: Control Plane](#chapter-10-control-plane)
- [Chapter 11: Security](#chapter-11-security)
- [Chapter 12: Case Study: Waiting for Godot](#chapter-12-case-study-waiting-for-godot)
- [Chapter 13: Design for Deployment](#chapter-13-design-for-deployment)
- [Chapter 14: Handling Versions](#chapter-14-handling-versions)
- [Chapter 15: Case Study: Trampled by Your Own Customers](#chapter-15-case-study-trampled-by-your-own-customers)
- [Chapter 16: Adaptation](#chapter-16-adaptation)
- [Chapter 17: Chaos Engineering](#chapter-17-chaos-engineering)

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

## Chapter 10: Control Plane

The control plane encompasses all the software and services that run in the background to make production load successful. One way to think about it is this: if production user data passes through it, it is production software. If its main job is to manage other software, it is control plane.

Every part of control plane is optional if you are willing to make trade-offs. - for example: logging and monitoring helps with postmortem analysis, without it all those will take longer or simply not be done. 

Mechanical advantage is the multi9plier on human effort that simple machines provide. With mechanical advantage, a person can move something much heavier than themselves. It works for good of for ill. High leverage allows a person to make large changes with less effort. 

Every postmortem review has 3 important jobs to do: Explain what happened. Apologise. Commit to improvement.

Automation has no judgement. When it goes wrong, it tends to do so really, really quickly. By the time a human perceives the problem, it is a question of recovery rather than intervention. We should use automation for the things humans are bad at: repetitive tasks and fast response. We should use humans for the things automation is bad at: perceiving the whole situation at a higher level.

Monitoring team should be responsible for providing monitoring tools - offer a monitoring service to customers.

Log collectors can work in push (the instance is pushing logs over the network, helpful with containers) or pull mode (the collector runs on a ventral machine and reaches out to all known hosts to remote-copy the logs). Getting all the logs on one host is a minor achievement, the real beauty comes from indexing the logs - then you can search for patterns, make trend line graphs and raise alerts when bad things happen. This can be done using Elasticsearch, Logstash and Kibana.

Categories of metrics that can be useful:

- Traffic indicators - page requests, transaction count
- Business transaction for each type - number processed, aborted, conversion rate
- Users - demographics, number of users, usage patterns, errors encountered
- Resource pool health - enabled state, total resources, number of resources created, number of blocked threads
- Database connection health - number of SQLExceptions thrown, number of queries, average response time
- Data consumption - number of rows present, footprint in memory and on disk
- Integration point health - state of circuit breaker, number of timeouts, number of requests, average response time, number of good responses, number of network, protocol errors, actual IP address
- Cache health - items in cache, memory used by cache, cache hit rate, items flushed by garbage collector

Canary deployment - a small set of instances that get the new build first. For a period of time, the instances running the new build coexist with instances running the old build. The purpose of the canary deployment is to reject a bad build before it reaches the users.

The net result is that GUIs make terrible administrative interfaces for long-term production operation. The best interface for long-term operation is the command line. Given a command line, operators can easily build a scaffolding of scripts, logging and automated actions to keep your software happy.

## Chapter 11: Security

Security must be baked in. It is not a seasoning to sprinkle onto your system at the end. You are responsible to protect your consumers and your company. 

OWASP Top 10 - catalogued application security incidents and vulnerabilities. Top 10 list represents a consensus about the most critical web ap[plication security flaws:

1. Injection - an attack on a parser or interpreter that relies on user-supported input. Classic example - SQL injection, it happens when code bashes strings together to make queries, but every SQL library allows the use of placeholders in query strings. Keep in mind that "*comes from a user*, doesn't only mean the input arrived just now in an HTTP request, data from a database may have originated fro a user as well. XML parsers are vulnerable as well (XXE injection).

2. Broken Authentication and Session Management - at one time, it was common to use query parameters on URLS and hyperlinks to carry session IDs, not only are thoseIDs are visible to every switch, router and proxy server, they are also visible to humans. Anyone who copies and pastes their link from their browser shares their session. Session hijacking can be dangerous when it is stolen from administrator. OWASP suggest the following guidelines for handling session IDs:

   1. Use long session ID with lots of entropy
   2. Generate session ID using a pseudorandom number generator with good cryptographic properties (`rand` is not a good choice)
   3. Protect against XSS to avoid script execution that would reveal session ID
   4. When user authenticates, generate a fresh session ID
   5. Keep up to date with security patches and versions, too many systems run outdated versions with known vulnerabilities
   6. Use cookies to exchange session IDs, do not accept session IDS via other mechanisms

   *Authentication* means we verify the identity of the caller. Is the caller who he or she claims to be? Some do's and and don'ts:

   1. Don't keep passwords in your database
   2. Never email a password to a user as a part of "*forgotten password*" process
   3. Do apply strong hash algorithm to password. Use "*salt*, which is some random data added to the password to make dictionary attacks harder
   4. Do allow users to enter overly long passwords
   5. Do allow users to paste passwords into GUIs
   6. Do allow users to paste passwords into GUIs
   7. Do plan on rehashing passwords at some point in future. We have to keep increasing the strength of our hash algorithms. Make sure you can change the salt too
   8. Don't allow attackers to make unlimited authentication attempts

3. Cross-site Scripting - happens when a service renders a user's input directly into HTML without applying input escaping, it is related to injection attacks. Bottom line is: never trust input, scrub it on the way and escape it on the way out. Don't build structured data by smashing strings together.

4. Broken Access Control - refers to application problems that allow attackers to access data they shouldn't. One of common forms of broken access control is "*direct object access*", this happens when a URL contains something like a database ID as a query parameter. Solution for this is to reduce the value of URL probing and checking authorisation to objects in the first place. Generate unique but non-sequential identifiers or use a generic ULR that is session-sensitive (`/users/123` -> `/users/me`). Rule of thumb: *If a caller is not authorised to see the contents of a resource, it should be as if the resource doesn't even exist* (`404` instead of `403`). When a request involves a file upload, the caller can overwrite any file the service is allowed to modify. The only safe way to handle file uploads is to tread the client's filename as an arbitrary string to store in a database field. Don't build a path from the filename in the request.

5. Security Misconfiguration - default passwords are a serious problem. Security misconfiguration usually takes the form of omission. Servers enable unneeded features by default. Admin consoles are a common source of problems. Another common security misconfiguration relates to servers listening too broadly. You can improve information security right away by splitting internal traffic onto its own NIC separate from public-facing traffic. Make sure every administrator uses a personal account, not a group account. Go ahead and add some logging to those administrative and internal calls.

6. Sensitive Data Exposure - credit cards, medical records, insurance files, purchasing data, emails - all these valuable things people can steal from you or use against you. Hackers don't attack your strong points, they look for cracks in your shell. It can be as simple as employee's stolen laptop with a database extract in a spreadsheet. Some guidelines:

   1. Don't store sensitive information that you don't need
   2. Use HTTP Strict Transport Security - it prevents clients from negotiating their way to insecure protocols
   3. Stop using SHA-1 
   4. Never store passwords in plain text
   5. Make sure sensitive data is encrypted in the database
   6. Decrypt data based on the user's authorisation, not the server's

   Consider using AWS Key Management Service. Ap[plication can request data encryption keys, which they use to encrypt or decrypt data. HashiCorp Vault - alternative to AWS KMS.

7. Insufficient Attack Protection - always assume that attackers have unlimited access to other machines behind firewall. Services do not typically track illegitimate requests by their origin. They do not block callers that issue too many bad requests. That allows an attacking program to keep making calls. API Gateways are a useful defence here. An API Gateway can block callers by their API key. It can also throttle their request rate. Normally this helps preserve capacity. In the case of an attack, it slows the rate of data compromise, thereby limiting the damage.

8. Cross-Site Request Forgery - used to be a bigger issue than it is now. A VCSRF attack starts on another website, an attacker uses a web page with JS, CSS or HTML that includes a Lin to your system. When the hapless user's browser accesses your system, your system thinks it is a valid request from that user. Make sure that requests with side effects (password change, mailing address update, purchases) use anti-CSRF tokens. These are extra fields containing random data that your system emits when rendering a form. Most frameworks today do this for you.You can also tighten up your cookie policy with the "*SameSite*" property. The SameSite attribute causes browser to send the cookie only if the documents origin is the same as the target's origin. SamsSite cookie may require change session management approach.

9. Using Components with Known Vulnerabilities - most successful attacks are not the exciting "*zero day, rush to patch before they get it*". Most attacks are mundane. It is important to keep applications up-to-date.

10. Underprotected APIs - it is essential to make are sure that APIs are not misused. APIs must ensure that malicious request cannot access data the original user would not be able to see. API should use the most secure means available to communicate. Make sure the parser is hardened against malicious input.Fuzz-testing APIs is especially important.

The principle of Least Privilege - a process should have the lowest level of privilege needed to accomplish the task. Anything application services need to do, they should do as nonadministrative users. Containers provide a nice degree of isolation from each other. Instead of creating multiple application-specific users on the host operating system, you can package each application into its own container. 

Configured Passwords - at the absolute minimum, passwords to production databases should be kept separate from any other configuration files. Password vaulting keeps passwords in encrypted files, which reduces the security problem. AWS Key Management Service is useful here. With KMS applications use API calls to acquire decryption keys. That way the encrypted data don't sit in the same storage as the decryption keys.

Frameworks can't protect you from the Top 10, neither can a one-time review by your company's applications security team. Security is an ongoing activity. It must be part of system's architecture. You must have a process to discover attacks.

## Chapter 12: Case Study: Waiting for Godot

## Chapter 13: Design for Deployment

How to design applications for easy rollout - packaging, integration point versioning and database schema.

Once upon a time, we wrote our software, zipped it up and threw it over the wall to the operations so they could deploy it. Operations would schedule some *planned* downtime to execute the release. HOWEVER, users should not care about downtime, application should be updated without them knowing about the release.

Most of the time, we design for the state of the system after a release. It assumes the whole system can be changed in some instantenous quantum jump. We have to treat deployment as a feature. Three key concerns: automation, orchestration and zero-downtime deployment. 

AUTOMATED DEPLOYMENTS. Build pipeline is the first tool of interest. It picks up after someone commits a change to VCS. Build pipelines are often implemented with CI servers. CI would stop after publishing a test report and an archive, the build pipeline goes beyond - run a series of steps that culminate in a production deployment (deploy code to trial env, run migrations, perform integration tests). Each stage of build pipeline is looking for reasons to reject the build - failed tests, lint complaints, integration fails.

Tools: Jenkins, GoCD, Netflix Spinnaker, AWS Code Pipeline. Do not look for the best tools, pick one that suffices and get good with it. Avoid analysis trap.

At the end of the build pipeline, build served interacts with one of the configuration management tools.

Between the time a developer commits code to the repository and the time it runs in production, code is a pure liability. It may have unknown bugs, may break scaling or cause production downtime. It might be a great implementation of a feature nobody wants. The idea of continuous deployment is to reduce that delay as much as possible to reduce the liability of undeployed code. 

A bigger deployment with more change is definitely riskier. "*If it hurts, do it more often* - do everything continuously, for the build pipeline it means - run the full build on every commit.

Shim - a thin piece of wood that fills a gap where two structures meet. In deployments, shim is a bit of code that helps join old and new versions of the application. For example when migrating database, old instances will fead for the old table, new instances will be reading from the new table. Shims can be achieved using SQL triggers - insert to one table is propagated to the other. 

[MUTABLE INFRASTRUCTURE] We typically update machines in batches. You match choose to divide your machines into equal-sized groups. Suppose we have five groups: Alpha, Bravo, Charlie, Delta, Foxtrot. Rollout would go like this:

1. Instruct Alpha to stop accepting new requests
2. Wait for load to drain from Alpha
3. Run the configuration management tool to update code and config
4. Wait for green health checks on all machines in Alpha
5. Instruct Alpha to start accepting requests
6. Repeat the process for Bravo, Charlie, Delta, Foxtrot

First group should be the canary group. Pause there to evaluate the build before moving on to the next group. Use traffic shaping at your load balancer to gradually ramp up the traffic to the canary group while watching monitoring for anomalies and metrics. 

Every application should include an end-to-end health check. 

[IMMUTABLE INFRASTRUCTURE] To roll code out here, we don't change the old machines. Instead we spin up new machines on the new version of the code. Machines can be started in the existing cluster or in a new cluster. With frequent deployments, you are better of starting new machines in the existing cluster, that avoids interrupting open connections when switching between clusters. Be careful about cache and session. 

Remember about the post-rollout cleanup - drop old tables, views, columns, aliases, ...

DEPLOY LIKE THE PROS - Currently deployments are frequent and should be seamless. The boundary between operations and development has become fractal. Designing for deployment gives the ability to make large changes in small steps. This all rests on a foundation of automated action and quality checking. The build pipeline should be able to apply all the accumulated wisdom of your architects, developers, designers, testers and DBAs.

Software should be designed to be deployed easily. Zero downtime is the objective. Smaller, easier deployments mean you can make big changes over a series of small steps. That reduces disruption to your users.

## Chapter 14: Handling Versions

It is better for everyone if we do some extra work on our end to maintain compatibility rather than pushing migration costs out onto other teams. How your software can be a good citizen?

Each consuming application has its own development team that operates on its own schedule. If you want others to respect your autonomy, then you must respect theirs. That means you can't force consumers to match your release schedule. Trying to coordinate consumer and provider deployments doesn't scale. 

TCP specification (Postel's Robustness Principle):

> Be conservative in what you do, be liberal in what you accept from others. 

Consumer and provider must share a number of agreements in order to communicate: connection handshaking and duration, request framing, content encoding, message syntax, message semantics, authorisation and authentication.

Postel's Robustness Principle can be seen as Liskov Substitution Principle: We can always accept more than we accepted before, but we cannot less or require more. We can return more than we returned before, but we cannot return less. 

Handling breaking changes - best approach is to add a version discriminator to the URL. This is the most common approach. You have to support both the old and the new versions for the some period of time. Both versions should operate side by side. This allows consumers to upgrade as they are able. Internally you want to avoid duplication. Handle this in the controller, methods that handle the new API go directly to the most current version of the business logic, methods that handle the old API get updated so they convert old objects to the current ones on requests and convert new objects to old ones on responses.

When receiving requests or messages, your application has no control over the format. The same goes for calling out to other services. The other endpoint can start rejecting your requests at any time. After all, they may not observe the same safety rules we just described. Always be defensive. 

## Chapter 15: Case Study: Trampled by Your Own Customers

Conway's Law:

> If you have four teams working on a compiler, you will get a form-pass compiler. 

Conway argues, two people must - in some fashion - communicate about the specification for that interface. If the communication does not occur, interface cannot be built.

Sometimes when you ask questions but you don't get answers, it means nobody knows the answers. At other times, it means nobody wants to be seen answering the questions. 

Load testing is about: defining a test plan, creating some scripts, configuring the load generators and test dispatchers. 

Tests often are prepared wrongly, real word is crude and rude, there are scrapers not respecting your cookie policy, search browsers indexing your website, users doing weird stuff. 

Most websites have terms and conditions stating "*By viewing this page you agree to ...*, with this you can sue or at least block sources of bots hitting your website millions of times. 

## Chapter 16: Adaptation

To make a change, your company has to go through a decision cycle - plan -> do -> check -> act. In small companies this communication may involve just one or two people, in larger companies an entire committee. Getting around the cycle faster makes you more competitive. This drives the "*fail fast*" motto for startups.

Agile and lean development methods helped remove delay from "act", DevOps helps remove even more in "act" and offers tons of new tools to help with "observe".

Thrashing - happens when organisation changes direction without taking the time to receive, process and incorporate feedback. You may recognise it as constantly shifting development priorities or an unending series of crises. It creates team confusion, unfinished work and lost productivity. To avoid trashing, try to create a steady cadence of delivery and feedback.

The platform team should not implement all your specific monitoring rules, instead this team should provide an API that lets you install your monitoring rules into the monitoring service provided by the platform. 

> If your developers only use the platform because it is mandatory, then the platform is not good enough

The Fallacy of the DevOps Team - in larger companies, it is common to find a group called DevOps team. This team sits between development and operations with the goal of moving faster and automating releases into production. *This is an anti pattern*. DevOps should soften the interface between different teams. DevOps goes deeper than deployment automation. It is a shift from ticket and blame-driven operations with throw-it-over-the-wall releases TO one based on open sharing of information and skills, data-driven decision making about architecture and design, production availability and responsiveness. Isolating these ideas to a single team undermines the whole point.

Frequent releases with incremental functionality allow your company to outpace its competitors.

Blue/green deployment - machines are divided into pools. One pool is active in production. The other pool gets the new deployment. That leaves time to test it before exposing it to customers. Once the new pool looks good, you shift production traffic over to it. 

More code, means it is harder to change. Large codebases are more likely to become overgeneralised. A shared database means every change has a higher potential to disrupt. The big service will accumulate complexity faster than the sum of two smaller services. It is easier to maintain and prune a bonsai juniper than a hundred-foot oak.

The key to making evolutionary architecture work is failure. You have to try different approaches to similar problems and kill the ones that are less successful. 

Jeff Bezos said that every team should be sized no bugger than you can feed with 2 large pizzas. Important but misleading. It is not just about having fever people on a team. A self-sufficient two-pizza team also means each team member has to cover more than one discipline. You can't have a two-pizza team if you need a dedicated DBA, frontend developer, an infra guru a backend developer, a ML expert, a product manager, a GUI designed, and so on. The two-pizza team is about reducing external dependencies. Thousand of dependencies will keep you from breaking free. It is really about having a small group that can be self-sufficient and push things all the way through to production.

No coordinated deployments - If you ever find that you need to update both the provider and the caller of a service interface at the same time, it is a warning sign that those services are strongly coupled. 

Evolutionary architecture is the one that supports incremental, guided c change as a first principle across multiple dimensions. Architecture styles:

- Microservice - very small, disposable units of code. Emphasise scalability, team-scale autonomy. Voulnerable to coupling with platform for monitoring, tracing and continuous delivery
- Microkernel and plugins - in-process, in-memory message passing core with formal interfaces to extensions. Good for incremental change in requirements, combining work from different teams. Vulnerable to language and runtime environment.
- Event-based - prefers asynchronous messages for communication, avoiding direct calls. Good for temporal decoupling, Allows new subscribers without change to publishers. Allows logic change and reconstruction from history. Vulnerable to semantic change in message formats over time.

Microservice size: ideally it should be no bigger than what fits in one developer's head.

Don't pursue microservices just because the Silicon Valley unicorns are doing it. Make sure they address a real problem you are likely to suffer. Otherwise, the operational overhead and debugging difficulty of micro services will outweigh your benefits.

Systems should exhibit loose clustering. In a loose cluster, the loss of an individual instance is no more significant than the fall of a single tree in a forest. The members of a cluster should not be configured to know the identities of other members of the cluster.

Modular systems inherently have more options than monolithic ones. 5 modular operators - borrowed from a hardware:

1. Splitting - breaking things into modules, or a module into submodules. The key with splitting is that the interface to the original modules is unchanged. Before splitting, it handles the whole thing itself. Afterward, it delegates work to the new modules but supports the same interface.
2. Substituting - is just replacing one module with another (like swapping nVidia card with AMD). The original module and the substitute need to share a common interface.
3. Augmenting and Excluding - augmenting is adding a module to a system. Excluding is removing one. If you design your parent system to make augmenting and excluding into first-class citizens, then you will reach a different design. 
4. Inversion - works by taking functionality that is distributed in several modules and raising it up higher in the system. 
5. Porting - is about repurposing a module from a different system. Any time we use a service created by a different project or system, we are porting that service to our system. Porting risks adding a coupling.

Information architecture is how we structure data. It is the data and the metadata we use to describe the things that matter to our systems. It is a set of related models that capture some facets of reality. Your job in building systems is to decide what facets of reality matter to your system, how are you going to represent those and how that representation can survive over time. 

Events can be used for:

- Notifications - fire and forget, one-way announcement, no response is expected
- Even-carried state transfer - an event that replicates entities or parts of entities so other systems can fo their work
- Event sourcing - when all changes are recorded as events that describe the change
- Command-query responsibility segregation - reading and writing with different structures. Not the same as events, but events are often found on the "command" side.

Versioning can be a real challenge with events, especially once you have yers' worth of them. Stay away from closed formats like serialised objects. Look toward open formats like JSON or self-describing messages. Avoid frameworks that require code generation based on schema. Treat messages like data instead of objects and you are going to have a better time supporting very old formats. 

Extract "*policy proxy*", questions of ownership and access control can be factored out of the service itself into a more centrally controlled location.

Use URL dualism to support many databases by using URLs as both the item identifier and a resolvable resource. Be careful you should be able to verify that whatever you receive back is something you generated.

One of the basic enterprise architecture patterns is the "Single System of Record". The idea is that any particular concept should originate in exactly one system, and that system will be enterprise-wide authority on entities within that concept.

We need to be careful about exposing internal concepts to other systems. It creates semantics and operational coupling that hinders future change.

## Chapter 17: Chaos Engineering

Chaos engineering - the discipline of experimenting on a distributed system in order to build confidence in the system's capability to withstand turbulent conditions in production. Staging or Qa environments aren't much of a guide to the large-scale behaviour of systems in production.

Congested networks behave in a qualitatively different way than uncontested ones. Systems that work in a lo-latency, low-loss network mat break badly in a congested network. Related paradox - *Volkswagen microbus* - you learn how to fix the things that often break. You don't learn how to fix the things that rarely break. But that means when when they do break, the situation is likely to be more dire. We want a continuous low level of breakage to make sure our system can handle the big things. 

We use chaos engineering the way a weightlifter uses iron: to create tolerable levels of stress and breakage to increase the strength of the system over time. 

At Netflix, chaos is an opt-out process. That means every service in production will be subject to Chaos Monkey. Other companies adopting chaos engineering have chosen an opt-in approach. When you are adding chaos engineering to an organisation, consider starting with opting-in.

You must be able to break the system without breaking the bank. It that is not the case, chaos engineering is not for you.

> If you have a wall full of green dashboards, that means your monitoring tools aren't good enough. There is always something weird going on.

Make sure you have a recovery plan. The system may not automatically return to a healthy state when you turn off the chaos.You need to know what to restart, disconnect or clean up.

Chaos Monkey does one kind of injection - it kills instances (randomly). There are different types of monkeys: Latency Monkey, Janitor Monkey, Chaos King, ...

Killing instances is the most basic and crude kind of injection. It will absolutely find weaknessess in your system.

Netflix uses failure injection testing (FIT). FIT can tag a request at the inbound edge with a cookie that says, eg. "Does the line, this request is going to fail when service G calls service H". Netflix uses a common framework for all its outbound service calls, so it has a way to propagate this cookie and treat it uniformly. 

High-reliability organisations use drills and simulations to find the same kind of systematic weaknesses in their human side as in the software side. You can make this more fun by calling it a "*zombie apocalypse simulation*". Randomly select 50% of your people and tell them they are zombies for the rest of the day.

After the simulation review the issues. 
