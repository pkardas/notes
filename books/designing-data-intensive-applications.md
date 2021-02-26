[go back](https://github.com/pkardas/learning)
## Designing Data-Intensive Applications: The Big Ideas Behind Reliable, Scalable, and Maintainable Systems
Book by Martin Kleppmann

[TOC]

#### Chapter 1: Reliable, Scalable and Maintainable Applications

May applications today are data-intensive, CPU is not a problem but amount of data, its complexity and speed of change. They are built from standard building blocks: database, cache, search index, stream processing, batch processing. These building blocks have many variants. 

*Reliability* - performs as expected, tolerates user's mistakes, good performance, continues to work even if things go wrong.

Hardware faults - on a cluster with 10 000 disks, you can expect, on average, one disk to die per day. Nowadays, multi-machine redundancy is no longer required - only in few use cases. 

Software errors - eg. many applications hang simultaneously on 30.06.2012 because of bug in Linux kernel. These kind of bugs lie dormant for a long time until they are triggered by an unusual set of circumstances.

Human errors - humans are responsible for majority of errors. There are measures that can be taken in order to prevent the errors:

- well-defined abstractions, easy to use tools, interfaces that discourage doing the wrong things
- provide fully functional non-production sandbox environment where people can explore and experiment with real data 
- test thoroughly at all levels (unit tests, integration, ...)
- provide tools that can recompute the data in case of errors in the past
- set up detailed monitoring



*Scalability* - system's ability to cope with increased load. Load can be described with a few numbers (load parameters), eg. requests per second, read/write ratio, number of simultaneous connections, hit rate on cache or something else.