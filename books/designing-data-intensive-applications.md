[go back](https://github.com/pkardas/learning)

# Designing Data-Intensive Applications: The Big Ideas Behind Reliable, Scalable, and Maintainable Systems
Book by Martin Kleppmann

[TOC]

## Chapter 1: Reliable, Scalable and Maintainable Applications

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

*Describing performance*

Response times (client waiting time) vary, always look at averages or medians (p50). In order to know how bad you outliers are you need to look at 95th, 99th and 99.9th percentiles. High percentiles (tail latencies) are important because they directly affect users' experience. Anyhow optimising 99.99th percentile might be really expensive. 

SLO (service level objectives) and SLA (service level agreements) - contracts that define the expected performance and availability of a service. Example SLA: service up and median response time < 200 ms, 99th percentile < 1s. High percentiles are extremely important in backend services that are called multiple times as part of serving a single end-user request.

*Approaches for coping with load*

Architecture might need to be reworked on every order of magnitude load increase. Because application could handle 2x bigger load, it doesn't mean it will handle 10x that load.

Scaling up / vertical scaling- moving to more powerful machine. Scaling out / horizontal scaling - distributing the load across multiple machines.

Distributing stateless services across multiple machines is easy, stateful data systems form a single node to a distributed setup can introduce a lot of additional complexity. There is no a single, universal approach for all applications, design is very often highly specific. 

*Maintainability*

Design and build systems that will minimise pain during maintenance. Make it easy to understand for new engineers. Allow for easy changes, adapting for unanticipated use cases as requirements change.

*Simplicity*

Project's complexity grove with time, this slows everyone down. Symptoms of complexity:

- explosion of state space
- tight coupling of modules
- tangled dependencies
- inconsistent naming and terminology
- special-casing to wark around issues

Complex software makes it easy to introduce bugs, system makes it harder to understand hidden assumptions, unintended consequences and many many more. **Simplicity should be a key goal for the systems we build**. One fo the best tools for removing complexity is *abstraction*. Great abstraction can hide implementation details behind a clean interface.

*Evolvability*

Requirements change, you learn new facts, new use cases emerge, priorities change, etc. Agile provides a framework for adapting to change.  Modify system and adapt it to changing requirements - pay attention to simplicity and abstractions.

## Chapter 2: Data Models and Query Languages

*Relational Model vs Document Model*. Relational Databases turned out to generalise very well. NoSQL (*Not Only SQL*) is the latest attempt to overthrow the relational model's dominance. 

Driving forces behind NoSQL:

- a need for greater scalability - very large datasets / very high write throughput 
- many open source projects
- specialised query operations
- frustration with restrictiveness of relational model

A rule of thumb: is you are duplicating values that could be stored in just one place the schema is not normalised.

Many-to-many relationships are widely used in relational databases, NoSQL reopened the debate on how best to represent such relationship.

If your data has document-like structure, then it's probably a good idea to use a document model. The relational database and its shredding (splitting document-like structure into multiple tables) can lead to unnecessary complicated application code.

Problems with document model: you can not access nested object directly you need to use access path, also it is not performing well in many-to-many relationships. 

Database schema can be compared to languages: relational - compiled language with static typing, document - dynamic (runtime) type checking - schema on read.

Data locality - because document databases store document as a string continuous string - JSON, XML, ... - often access will be faster because of locality, if data is split across multiple tables -> multiple disks -> more disk seeks -> more time required. However the document database will need to load entire document even if you need a small portion of it.

*Query Languages for Data*

SQL is declarative - you define what you want and it is up to the computer do determine how to get this data. Most programming languages are imperative - you define how to process the data. 

*MapReduce Querying*

MapReduce - programming model for processing large amounts of data in bulk across many machines. Limited form of MapReduce is supported by some noSQL data-stores. Something between declarative and imperative programming. 

*Graph-Like Data Models*

Very good approach form data with many-to-many relationships. Each vertex has: ID, set of outgoing edges, set of outgoing edges, a collection of properties (key-value pairs). Each edge has: ID, the tail vertex, the head vertex, label describing the type of relationship, a collection of properties (key-value pairs).

Graphs give great flexibility in modeling relationships. Eg. France has departments and regions, whereas the US has counties and states.

Cypher is a declarative query language for property graphs, created for Neo4j DB, eg.: find the names of all people who emigrated from the US to Europe:

```cypher
MATCH
  (person) -[:BORN_IN]->  () -[:WITHIN*0..]-> (us:Location {name: "United States"}),
  (person) -[:LIVES_IN]-> () -[:WITHIN*0..]-> (eu:Location {name: "Europe"})
RETURN person.name
```

This can be expressed in SQL (recursive common table expressions :grimacing:), but with one difficulty, `LIVES_IN` might point to any location (region, country, state, continent), here we are interested only in the US and Europe. 4 lines in Cypher vs 29 lines in SQL.

*Tripple-Stores*

Very similar to graph model, all information stored in the form of very simple three-part statements: `(subject, predicate, object)`, eg. `(Jim, likes, bananas)`.

## Chapter 3: Storage and Retrieval

In order to tune a storage engine to perform well on your kind of workload, you need to have a rough idea of what the storage engine is doing under the hood.

*Data Structures That Power Your Database*

Hash Indexes. For example: Key and offset pairs.