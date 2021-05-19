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

Hash Indexes. For example: Key and offset pairs. SSTable - Sorted String Table.

B-Trees - most widely used indexing structure, standard index implementation for almost all relational databases and for many non-relational databases. B-trees keep key-value pairs sorted by key, which allows efficient key-value lookups. The number of references to child pages in one page of the B-tree is called the branching factor. A B-tree with *n* keys always has depth of *O(log n)*. Most databases can fit into a B-tree that is 3-4 levels deep. 4-level tree of 4KB pages with a branching factor of 500 can store up to 256TB of data.

In order to make db resilient to crashes, it is common for B-tree implementations to include an additional data structure on disk - WAL - write-ahead log - append only file, every B-tree modification must be written before it can be applied on the pages of the tree. When db crashes, this log is used to restore the B-tree to consistent state.

LSM-tree:

- faster for writes 
- can be compressed better, thus often produce smaller files on disk
- lower storage overheads
- compaction process can sometimes interfere with the performance of ongoing reads and writes
- if throughput is high and compaction is not configured carefully, compaction might not keep up with with the rate of incoming writes

B-trees are so old, and so well optimised so that they can deliver good, consistent performance for many workloads.

Key-value indexes are for primary key index in the relational model. It is also common to have secondary index. They don't have to be unique - this can be solved for example by appending row ID.

Clustered index - storing all row data within the index.

Concatenated index - multi-column index, combines several fields into one key by appending one column to another.

What if you search for misspelled data or similar data. Lucene is able to search text for words   within a certain edit distance.

Data structures discussed so far are specific for disks. However, as RAM becomes cheaper and many datasets are feasible to keep in memory. This led to the development of in-memory databases. Some in-memory key-value stores (Memcached) are intended for caching, data can be lost on machine restart. Other in-memory databases aim for durability, which can be achieved with special battery-powered RAM, by writing a log changes to disk or replicating memory state to other machines. When restarted it needs to load the data from the disk of from a replica. Even though it is a in-memory database, a disk is still used. Other in-memory databases with relational model: VoltDB, MemSQL, Oracle TimesTen. RAMCloud is a key-value store, Redis and Couchbase provide weak durability by writing to disk asynchronously.

In-memory databases achieve better performance.

OLTP - Online Transaction Processing - interactive applications - look up fa small number of records, insert or update records based on user's activity. 

OLAP - Online Analytic Processing - second patterns - analytic queries.

In 90s companies stopped using OLTP  systems for analytics purposes and shifted to OLAP for running analytics on a separate database. This separate database is called a data warehouse.

Data warehouse - separate database that analyst can query without affecting OLTP operations. Read-only copy of the data. Data extracted fro OLTP databases, transformed into analysis-friendly  schema. Process fo getting data info the ware house is known as Extract-Transform-Load. Biggest advantage of OLAP for analysis is that this database can be optimised for large queries. 

Many data warehouses use star schema (dimensional modeling). Variation of this schema is called the snowflake schema. Snowflakes are more normalised than stars.

Fact tables are often 100 columns wide, however `SELECT * ` queries are rarely used. In most OLTP databases, storage is laid out in a row-oriented fashion. How to execute queries more efficiently? The idea behind column-oriented storage is simple: don't store all the values from one row together, but store all values from each columns together. Eg. one file = one column - much faster than parsing each row.

Columns can be compressed using for example bitmap encoding - unique values encoded using bits. Efficient in situations where only few unique values and millions of records. Column compression allows mor rows from a column to fit in L1 cache.

## Chapter 4: Encoding and Evolution

Rolling update / staged rollout - deploying the new version to a few nodes at a time, checking whether the new version is running smoothly. With client-side applications you are at mercy of the user, who may not install the update for some time. This means that old and new versions of the code might co exists for some time. 

Backward compatibility - newer code can read data that was written by older code (normally not hard).

Forward compatibility - older code can read data that was written by newer code (this is trickier).

Programs usually work with data in 2 representations:

- in memory - objects, lists, arrays, trees - data structures optimised for efficient access and manipulation by the CPU
- byte sequence structures - for example JSON

The translation from the in-memory to a byte sequence is called encoding. The reverse is called decoding (also: parsing, deserialisation, unmarshaling).

Many programming languages have built-in support for encoding in-memory data structures. Python has pickle, Java has Serialisable, Ruby has Marshal, however:

- encoding is tied to programming language
- potential source of security issues
- Java's built-in serialisation is said to have bad performance

In general it is bad idea to use language's built-in encoding for anything other than very transient purposes.

JSON:

- built-in support in browsers
- distinguishes strings and numbers
- good support for unicode, no support for binary strings

XML:

- too verbose
- no distinction between numbers and strings
- good support for unicode, no support for binary strings

CSV:

- less powerful than XML and JSON
- no distinction between numbers and strings
- no data schema

Despite flaws of JSON, XML and CSV they are good enough for many purposes and thy will remain popular.

JSON is less verbose than XMAL, but still uses a lot of space - this might be an issue when you are dealing with terabytes of data. This led to the development of binary encodings for JSON - BSON, BJSON, UBJSON, BISON. XMAL has olso its binary encodings - WBXML and Fast Infoset. However, non of them are widely adopted.

Apache Thrift (Facebook), Protocol Buffers (Google) are binary encoding libraries that are based on the same principle. Schema defined in interface definition language, this schema can generate code for encoding and decoding data.

Field numbers in Apache Thrift are used for more compact encoding (no need for passing field names through the wire - CompactProtocol). Required / optional makes no difference for encoding, this is used for the runtime.

Every field you add after the initial deployment of schema must be optional of have default value. Removing is like adding, you can remove only optional fields. Also with ProtoBuf / Thrift you can never use use the same tag number again.

Avro is another binary encoding format, it has optional code generation for dynamically typed programming languages.

Data can flow through:

- database
- services - REST and RPC, services are similar to databases, they allow clients to submit and query data. A key design goal of a service-oriented / micro services architecture is to make the application easier to change and maintain by making services independently deployable and evolvable.

REST is not a protocol, but rather a design philosophy that builds upon the principles of HTTP.

SOAP - XML-based protocol for making network API requests.

RPC - Remote Procedure Call - seems convenient at first, but the approach is fundamentally flawed, because a network request is very different from a local function call:

- local function is predictable - it can either succeed or fail depending on the input, a network request is unpredictable - connection might be lost
- a local function call either returns a result or throws an exception, a network request may return without a result - timeout
- retry mechanism might cause duplication (fist request went went through), unless you build deduplication mechanism
- duration of remote call depends on the network congestion
- when you call a local function you can effectively pass references
- if client and server use different languages, data translation might end up ugly

Despite these problems RPC is not going away, modern frameworks are more explicit about the fact that a remote call i different from local function invocation.

- message passing - something between database passing and services. Similar to RPC because client's request is delivered with low latency, similar to databases because message is not sent via a direct network connection but goes through message broker.

Message brokers have couple of advantages comparing to RPC:

- can acs as a buffer when recipient is unavailable
- can automatically redeliver messages
- avoids the sender to know the IP address and port 
- one message can be sent to multiple recipients
- logical decoupling between sender and receiver

## Chapter 5: Replication

Shared-Nothing Architecture - each machine or virtual machine running the database is called a node. Each node uses its own CPU, RAM and disks independently. Any coordination between nodes is done at the software level using network.

Replication - means keeping a copy of the same data on multiple machines that are connected via a network. Why?

- to reduce latency - copy close to the users
- to allow the system to continue working 
- to scale out

If data is not changing, replication is easy, for dealing with replication changes, following algorithms can be used: single-leader, multi-leader and leaderless replication.

Leaders and Followers - each node (replica) stores a copy of the database . One of the replicas is designated to be a leader (master), when clients want to write to the database, they must send their requests to the leader. Other replicas - followers (slaves), take the log from the leader and updates local copy of the data, applying all writes in the same order as they were processed by the leader. Writes are accepted only to the leader, read can be performed using any follower. 

On follower failure, if the connection between leader and follower is temporarily corrupted, follower can recover easily, because it knows the last processed transaction from the log. It can request missing data from the last successful transaction. Leader failure is more trickier. One of the followers can be promoted to be the new leader, for example replica with the most recent data (election) - data loss minimisation.

Implementation of Replication Logs:

- Statement-based replication - leader logs every request (statement) - for relational database this means thet every INSERT / UPDATE / DELETE statement is forwarded to followers, each follower executes received SQL statement (as if it had been received from a client)
  - Problems - what about NOW, RAND - nondeterministic, what about auto-incrementing fields, what about triggers. There are some workarounds, like sending request and result or requiring deterministic transactions.
- Write-ahead log (WAL) shipping - log is append-only sequence of bytes containing all writes, this log can be used to build replica. This method is used in PostgreSQL and Oracle. Disadvantage of this approach is that log contains low-level information - like which disk blocks were changed, so replication is closely coupled to the storage engine (or even storage engine version!).
- Logical log replication - alternative approach that uses different log format for replication - decoupling. Usually a sequence of records describing writes to database tables at the granularity of a row. Easier backward compatibility - leaders and followers can run different engine versions 
- Trigger-based replication - triggers have ability to log changes to a separate table, from which an external process can read. This allows for replicating for example subset of data.

Problems with replication lag:

- leader-based replication is cool when we need to scale reads, not necessarily writes - common on the web
- synchronous replication - single node failure can make entire system unavailable 
- asynchronous replication - follower might fall behind -> inconsistent data (this is temporary situation, if you stop writing for a while, the followers will catch up and become consistent with the leader - eventual consistency)

Replica lag - anomalies:

- if user writes and then views, the new data might not yet have reached the replica. Read-your-writes consistency - needed guarantee that if the user reloads the page, whey will always see updates they submitted themselves.
  - Solution: owner of the profile views data from the leader, other users view from replica. There are modifications, for example: if last update older than 1m -> view from replica.
- when reading from asynchronous followers is that user can see things moving back in time - happens when user makes several reads from different replicas
  - Solution: monotonic reads - guarantee stronger than eventual consistency, if user makes several reads in sequence, they will not see time go backward (never data after older data)
- consistent prefix reads - is a sequence of writes happens in certain order, then anyone reading those writes will see them appear in the same order
  - Solution: make sure that any writes that are casually related to each other are written to the same partition OR use algorithm that keep track of casual dependencies

When working with an eventual consistent system, it is worth thinking about how the application behaves if the replication lag increases to several minutes or hours.

