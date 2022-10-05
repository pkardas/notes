[go back](https://github.com/pkardas/learning)

# Designing Data-Intensive Applications: The Big Ideas Behind Reliable, Scalable, and Maintainable Systems

Book by Martin Kleppmann

- [Chapter 1: Reliable, Scalable and Maintainable Applications](#chapter-1-reliable-scalable-and-maintainable-applications)
- [Chapter 2: Data Models and Query Languages](#chapter-2-data-models-and-query-languages)
- [Chapter 3: Storage and Retrieval](#chapter-3-storage-and-retrieval)
- [Chapter 4: Encoding and Evolution](#chapter-4-encoding-and-evolution)
- [Chapter 5: Replication](#chapter-5-replication)
- [Chapter 6: Partitioning](#chapter-6-partitioning)
- [Chapter 7: Transactions](#chapter-7-transactions)
- [Chapter 8: The Trouble with Distributed Systems](#chapter-8-the-trouble-with-distributed-systems)
- [Chapter 9: Consistency and Consensus](#chapter-9-consistency-and-consensus)
- [Chapter 10: Batch Processing](#chapter-10-batch-processing)
- [Chapter 11: Stream Processing](#chapter-11-stream-processing)
- [Chapter 12: The Future of Data Systems](#chapter-12-the-future-of-data-systems)

## Chapter 1: Reliable, Scalable and Maintainable Applications

May applications today are data-intensive, CPU is not a problem but amount of data, its complexity and speed of change.
They are built from standard building blocks: database, cache, search index, stream processing, batch processing. These
building blocks have many variants.

*Reliability* - performs as expected, tolerates user's mistakes, good performance, continues to work even if things go
wrong.

Hardware faults - on a cluster with 10 000 disks, you can expect, on average, one disk to die per day. Nowadays,
multi-machine redundancy is no longer required - only in few use cases.

Software errors - e.g. many applications hang simultaneously on 30.06.2012 because of bug in Linux kernel. This kind of
bugs lie dormant for a long time until they are triggered by an unusual set of circumstances.

Human errors - humans are responsible for the majority of errors. There are measures that can be taken in order to
prevent the errors:

- well-defined abstractions, easy to use tools, interfaces that discourage doing the wrong things
- provide fully functional non-production sandbox environment where people can explore and experiment with real data
- test thoroughly at all levels (unit tests, integration, ...)
- provide tools that can recompute the data in case of errors in the past
- set up detailed monitoring

*Scalability* - system's ability to cope with increased load. Load can be described with a few numbers (load parameters)
, e.g. requests per second, read/write ratio, number of simultaneous connections, hit rate on cache or something else.

*Describing performance*

Response times (client waiting time) vary, always look at averages or medians (p50). In order to know how bad you
outliers are you need to look at 95th, 99th and 99.9th percentiles. High percentiles (tail latencies) are important
because they directly affect users' experience. Anyhow, optimising 99.99th percentile might be really expensive.

SLO (service level objectives) and SLA (service level agreements) - contracts that define the expected performance and
availability of a service. Example SLA: service up and median response time < 200 ms, 99th percentile < 1s. High
percentiles are extremely important in backend services that are called multiple times as part of serving a single
end-user request.

*Approaches for coping with load*

Architecture might need to be reworked on every order of magnitude load increase. Because application could handle 2x
bigger load, it doesn't mean it will handle 10x that load.

Scaling up / vertical scaling- moving to more powerful machine. Scaling out / horizontal scaling - distributing the load
across multiple machines.

Distributing stateless services across multiple machines is easy, stateful data systems form a single node to a
distributed setup can introduce a lot of additional complexity. There is no a single, universal approach for all
applications, design is very often highly specific.

*Maintainability*

Design and build systems that will minimise pain during maintenance. Make it easy to understand for new engineers. Allow
for easy changes, adapting for unanticipated use cases as requirements change.

*Simplicity*

Project's complexity grove with time, this slows everyone down. Symptoms of complexity:

- explosion of state space
- tight coupling of modules
- tangled dependencies
- inconsistent naming and terminology
- special-casing to work around issues

Complex software makes it easy to introduce bugs, system makes it harder to understand hidden assumptions, unintended
consequences and many more. **Simplicity should be a key goal for the systems we build**. One of the best tools for
removing complexity is *abstraction*. Great abstraction can hide implementation details behind a clean interface.

*Evolvability*

Requirements change, you learn new facts, new use cases emerge, priorities change, etc. Agile provides a framework for
adapting to change. Modify system and adapt it to changing requirements - pay attention to simplicity and abstractions.

## Chapter 2: Data Models and Query Languages

*Relational Model vs Document Model*. Relational Databases turned out to generalise very well. NoSQL (*Not Only SQL*) is
the latest attempt to overthrow the relational model's dominance.

Driving forces behind NoSQL:

- a need for greater scalability - very large datasets / very high write throughput
- many open source projects
- specialised query operations
- frustration with restrictiveness of relational model

A rule of thumb: is you are duplicating values that could be stored in just one place the schema is not normalised.

Many-to-many relationships are widely used in relational databases, NoSQL reopened the debate on how best to represent
such relationship.

If your data has document-like structure, then it's probably a good idea to use a document model. The relational
database and its shredding (splitting document-like structure into multiple tables) can lead to unnecessary complicated
application code.

Problems with document model: you can not access nested object directly you need to use access path, also it is not
performing well in many-to-many relationships.

Database schema can be compared to languages: relational - compiled language with static typing, document - dynamic (
runtime) type checking - schema on read.

Data locality - because document databases store document as a string continuous string - JSON, XML, ... - often access
will be faster because of locality, if data is split across multiple tables -> multiple disks -> more disk seeks -> more
time required. However, the document database will need to load entire document even if you need a small portion of it.

*Query Languages for Data*

SQL is declarative - you define what you want, and it is up to the computer do determine how to get this data. Most
programming languages are imperative - you define how to process the data.

*MapReduce Querying*

MapReduce - programming model for processing large amounts of data in bulk across many machines. Limited form of
MapReduce is supported by some noSQL data-stores. Something between declarative and imperative programming.

*Graph-Like Data Models*

Very good approach form data with many-to-many relationships. Each vertex has: ID, set of outgoing edges, set of
outgoing edges, a collection of properties (key-value pairs). Each edge has: ID, the tail vertex, the head vertex, label
describing the type of relationship, a collection of properties (key-value pairs).

Graphs give great flexibility in modeling relationships. e.g. France has departments and regions, whereas the US has
counties and states.

Cypher is a declarative query language for property graphs, created for Neo4j DB, e.g.: find the names of all people who
emigrated from the US to Europe:

```cypher
MATCH
  (person) -[:BORN_IN]->  () -[:WITHIN*0..]-> (us:Location {name: "United States"}),
  (person) -[:LIVES_IN]-> () -[:WITHIN*0..]-> (eu:Location {name: "Europe"})
RETURN person.name
```

This can be expressed in SQL (recursive common table expressions), but with one difficulty, `LIVES_IN` might point to
any location (region, country, state, continent), here we are interested only in the US and Europe. 4 lines in Cypher vs
29 lines in SQL.

*Triple-Stores*

Very similar to graph model, all information stored in the form of very simple three-part
statements: `(subject, predicate, object)`, e.g. `(Jim, likes, bananas)`.

## Chapter 3: Storage and Retrieval

In order to tune a storage engine to perform well on your kind of workload, you need to have a rough idea of what the
storage engine is doing under the hood.

*Data Structures That Power Your Database*

Hash Indexes. For example: Key and offset pairs. SSTable - Sorted String Table.

B-Trees - most widely used indexing structure, standard index implementation for almost all relational databases and for
many non-relational databases. B-trees keep key-value pairs sorted by key, which allows efficient key-value lookups. The
number of references to child pages in one page of the B-tree is called the branching factor. A B-tree with *n* keys
always has depth of *O(log n)*. Most databases can fit into a B-tree that is 3-4 levels deep. 4-level tree of 4KB pages
with a branching factor of 500 can store up to 256TB of data.

In order to make db resilient to crashes, it is common for B-tree implementations to include an additional data
structure on disk - WAL - write-ahead log - append only file, every B-tree modification must be written before it can be
applied on the pages of the tree. When db crashes, this log is used to restore the B-tree to consistent state.

LSM-tree:

- faster for writes
- can be compressed better, thus often produce smaller files on disk
- lower storage overheads
- compaction process can sometimes interfere with the performance of ongoing reads and writes
- if throughput is high and compaction is not configured carefully, compaction might not keep up with the rate of
  incoming writes

B-trees are so old, and so well optimised so that they can deliver good, consistent performance for many workloads.

Key-value indexes are for primary key index in the relational model. It is also common to have secondary index. They
don't have to be unique - this can be solved for example by appending row ID.

Clustered index - storing all row data within the index.

Concatenated index - multi-column index, combines several fields into one key by appending one column to another.

What if you search for misspelled data or similar data. Lucene is able to search text for words within a certain edit
distance.

Data structures discussed so far are specific for disks. However, as RAM becomes cheaper and many datasets are feasible
to keep in memory. This led to the development of in-memory databases. Some in-memory key-value stores (Memcached) are
intended for caching, data can be lost on machine restart. Other in-memory databases aim for durability, which can be
achieved with special battery-powered RAM, by writing a log changes to disk or replicating memory state to other
machines. When restarted it needs to load the data from the disk of from a replica. Even though it is an in-memory
database, a disk is still used. Other in-memory databases with relational model: VoltDB, MemSQL, Oracle TimesTen.
RAMCloud is a key-value store, Redis and Couchbase provide weak durability by writing to disk asynchronously.

In-memory databases achieve better performance.

OLTP - Online Transaction Processing - interactive applications - look up fa small number of records, insert or update
records based on user's activity.

OLAP - Online Analytic Processing - second patterns - analytic queries.

In 90s companies stopped using OLTP systems for analytics purposes and shifted to OLAP for running analytics on a
separate database. This separate database is called a data warehouse.

Data warehouse - separate database that analyst can query without affecting OLTP operations. Read-only copy of the data.
Data extracted from OLTP databases, transformed into analysis-friendly schema. Process of getting data info the
warehouse is known as Extract-Transform-Load. Biggest advantage of OLAP for analysis is that this database can be
optimised for large queries.

Many data warehouses use star schema (dimensional modeling). Variation of this schema is called the snowflake schema.
Snowflakes are more normalised than stars.

Fact tables are often 100 columns wide, however `SELECT * ` queries are rarely used. In most OLTP databases, storage is
laid out in a row-oriented fashion. How to execute queries more efficiently? The idea behind column-oriented storage is
simple: don't store all the values from one row together, but store all values from each column together. e.g. one file
= one column - much faster than parsing each row.

Columns can be compressed using for example bitmap encoding - unique values encoded using bits. Efficient in situations
where only few unique values and millions of records. Column compression allows mor rows from a column to fit in L1
cache.

## Chapter 4: Encoding and Evolution

Rolling update / staged rollout - deploying the new version to a few nodes at a time, checking whether the new version
is running smoothly. With client-side applications you are at mercy of the user, who may not install the update for some
time. This means that old and new versions of the code might co-exist for some time.

Backward compatibility - newer code can read data that was written by older code (normally not hard).

Forward compatibility - older code can read data that was written by newer code (this is trickier).

Programs usually work with data in 2 representations:

- in memory - objects, lists, arrays, trees - data structures optimised for efficient access and manipulation by the CPU
- byte sequence structures - for example JSON

The translation from the in-memory to a byte sequence is called encoding. The reverse is called decoding (also: parsing,
deserialization, unmarshalling).

Many programming languages have built-in support for encoding in-memory data structures. Python has pickle, Java has
Serializable, Ruby has Marshal, however:

- encoding is tied to programming language
- potential source of security issues
- Java's built-in serialisation is said to have bad performance

In general, it is bad idea to use language's built-in encoding for anything other than very transient purposes.

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

Despite flaws of JSON, XML and CSV they are good enough for many purposes, and they will remain popular.

JSON is less verbose than XMAL, but still uses a lot of space - this might be an issue when you are dealing with
terabytes of data. This led to the development of binary encodings for JSON - BSON, BJSON, UBJSON, BISON. XMAL has also
its binary encodings - WBXML and Fast Infoset. However, none of them are widely adopted.

Apache Thrift (Facebook), Protocol Buffers (Google) are binary encoding libraries that are based on the same principle.
Schema defined in interface definition language, this schema can generate code for encoding and decoding data.

Field numbers in Apache Thrift are used for more compact encoding (no need for passing field names through the wire -
CompactProtocol). Required / optional makes no difference for encoding, this is used for the runtime.

Every field you add after the initial deployment of schema must be optional of have default value. Removing is like
adding, you can remove only optional fields. Also, with ProtoBuf / Thrift you can never use the same tag number again.

Avro is another binary encoding format, it has optional code generation for dynamically typed programming languages.

Data can flow through:

- database
- services - REST and RPC, services are similar to databases, they allow clients to submit and query data. A key design
  goal of a service-oriented / microservices architecture is to make the application easier to change and maintain by
  making services independently deployable and evolvable.

REST is not a protocol, but rather a design philosophy that builds upon the principles of HTTP.

SOAP - XML-based protocol for making network API requests.

RPC - Remote Procedure Call - seems convenient at first, but the approach is fundamentally flawed, because a network
request is very different from a local function call:

- local function is predictable - it can either succeed or fail depending on the input, a network request is
  unpredictable - connection might be lost
- a local function call either returns a result or throws an exception, a network request may return without a result -
  timeout
- retry mechanism might cause duplication (fist request went through), unless you build deduplication mechanism
- duration of remote call depends on the network congestion
- when you call a local function you can effectively pass references
- if client and server use different languages, data translation might end up ugly

Despite these problems RPC is not going away, modern frameworks are more explicit about the fact that a remote call i
different from local function invocation.

- message passing - something between database passing and services. Similar to RPC because client's request is
  delivered with low latency, similar to databases because message is not sent via a direct network connection but goes
  through message broker.

Message brokers have a couple of advantages comparing to RPC:

- can acs as a buffer when recipient is unavailable
- can automatically redeliver messages
- avoids the sender to know the IP address and port
- one message can be sent to multiple recipients
- logical decoupling between sender and receiver

## Chapter 5: Replication

Shared-Nothing Architecture - each machine or virtual machine running the database is called a node. Each node uses its
own CPU, RAM and disks independently. Any coordination between nodes is done at the software level using network.

Replication - means keeping a copy of the same data on multiple machines that are connected via a network. Why?

- to reduce latency - copy close to the users
- to allow the system to continue working
- to scale out

If data is not changing, replication is easy, for dealing with replication changes, following algorithms can be used:
single-leader, multi-leader and leaderless replication.

Leaders and Followers - each node (replica) stores a copy of the database . One of the replicas is designated to be a
leader (master), when clients want to write to the database, they must send their requests to the leader. Other replicas

- followers (slaves), take the log from the leader and updates local copy of the data, applying all writes in the same
  order as they were processed by the leader. Writes are accepted only to the leader, read can be performed using any
  follower.

On follower failure, if the connection between leader and follower is temporarily corrupted, follower can recover
easily, because it knows the last processed transaction from the log. It can request missing data from the last
successful transaction. Leader failure is trickier. One of the followers can be promoted to be the new leader, for
example replica with the most recent data (election) - data loss minimisation.

Implementation of Replication Logs:

- Statement-based replication - leader logs every request (statement) - for relational database this means thet every
  INSERT / UPDATE / DELETE statement is forwarded to followers, each follower executes received SQL statement (as if it
  had been received from a client)
    - Problems - what about NOW, RAND - nondeterministic, what about auto-incrementing fields, what about triggers.
      There are some workarounds, like sending request and result or requiring deterministic transactions.
- Write-ahead log (WAL) shipping - log is append-only sequence of bytes containing all writes, this log can be used to
  build replica. This method is used in PostgreSQL and Oracle. Disadvantage of this approach is that log contains
  low-level information - like which disk blocks were changed, so replication is closely coupled to the storage engine (
  or even storage engine version!).
- Logical log replication - alternative approach that uses different log format for replication - decoupling. Usually a
  sequence of records describing writes to database tables at the granularity of a row. Easier backward compatibility -
  leaders and followers can run different engine versions
- Trigger-based replication - triggers have ability to log changes to a separate table, from which an external process
  can read. This allows for replicating for example subset of data.

Problems with replication lag:

- leader-based replication is cool when we need to scale reads, not necessarily writes - common on the web
- synchronous replication - single node failure can make entire system unavailable
- asynchronous replication - follower might fall behind -> inconsistent data (this is temporary situation, if you stop
  writing for a while, the followers will catch up and become consistent with the leader - eventual consistency)

Replica lag - anomalies:

- if user writes and then views, the new data might not yet have reached the replica. Read-your-writes consistency -
  needed guarantee that if the user reloads the page, whey will always see updates they submitted themselves.
    - Solution: owner of the profile views data from the leader, other users view from replica. There are modifications,
      for example: if last update older than 1m -> view from replica.
- when reading from asynchronous followers is that user can see things moving back in time - happens when user makes
  several reads from different replicas
    - Solution: monotonic reads - guarantee stronger than eventual consistency, if user makes several reads in sequence,
      they will not see time go backward (never data after older data)
- consistent prefix reads - is a sequence of writes happens in certain order, then anyone reading those writes will see
  them appear in the same order
    - Solution: make sure that any writes that are casually related to each other are written to the same partition OR
      use algorithm that keep track of casual dependencies

When working with an eventual consistent system, it is worth thinking about how the application behaves if the
replication lag increases to several minutes or hours.

Multi-Leader Replication - more than one node accepting writes, each leader simultaneously acts as a follower to the
other leaders. It rarely makes sense to use a multi-leader setup within a single datacenter, because benefits rarely
outweigh the added complexity, however there are some situations in which this configuration makes sense:

- multi-datacenter operation - one leader in each datacenter, multi-leader setup requires conflict resolution mechanism
  which can be problematic. Multi-leader replication is often considered dangerous territory that should be avoided if
  possible.
- clients with offline operation - for example calendar app have to work even if it is disconnected from the internet,
  if you make changes while you are offline then they need to be synced with a server and all other devices. This
  basically means every device has a local database that acts as a leader. For example CouchDB is designed for this mode
  of operation.

- collaborative editing - multiple people editing the same document - e.g. Google Docs, very similar case to the
  previous one. If you want to guarantee that there will be no editing conflicts, the application must obtain a lock on
  the document before user can edit - this collaboration model is equivalent to single-leader replication with
  transaction on the leader.

Handling Write Conflicts:

- make the conflict detection synchronous - wait for the write to be replicated to all replicas before telling the user
  that write was successful
- avoid conflicts - all writes can go through the same leader, requests from particular user are always routed to the
  same datacenter and use the leader in that datacenter for writing and reading.
- each replica should converge toward consistent state
- custom conflict resolution - this might depend on the application, code might be executed on write or on read

Automatic Conflict Resolution - Amazon was frequently cited example of surprising effects due to conflict resolution
handler - customers were seeing items removed from the cart. Some ideas for automatic conflict resolution:

- conflict-free replicated datatypes - family of data structures that can be concurrently edited by multiple users
- merge-able persistent data structures - similar to GIT
- operational transformation - algorithm behind Google Docs - designed specifically for concurrent edits of an ordered
  list of items - e.g. string.

Replication topology describes the communication paths along which writes are propagated from one node to another (
circular, star, all-to-all).

Leaderless replication - the client sends directly its writes to several replicas, or coordinator node does this on
behalf of the client. When one node is down, some data might be down. For this reason when a client reads from the
database, it sends its requests to multiple replicas and uses data with the most version number. Eventually all the data
will be copied to every replica. 2 approaches with dealing with inconsistent data: whenever client notices inconsistency
or background process looking for differences in the data.

For example in DynamoDB it is possible to set minimum number of replicas that saved the data to mark write as valid.

It is important to monitor replication lag, even if your application can tolerate stale reads.

Dynamo-style databases allow several clients to concurrently write to the same key - this means potential conflicts!
Events may arrive in a different order at different nodes, due to network delays and partial failures (replicas might
store different values). In order to become eventually consistent, the replicas should converge toward the same value.
It is up to the developer to resolve conflict:

- last write wins - discard older values
- detecting happens-before operations (btw. two operations might be considered concurrent when they overlap in time, not
  necessarily at the same time)
- merge concurrently written values
- use version vectors - version number per replica and per key, each replica increments its own version number

## Chapter 6: Partitioning

Partitioning - breaking up the data into partitions (each piece of data belongs to exactly one partition). The main
reason for partitioning is scalability - different partitions can be placed on different nodes.

Partitioning is usually combined with replication. Copies of each partition are stored on multiple nodes. The goal with
partitioning is to spread the data and the query load evenly across nodes. If every node takes fair share, e.g. 10 nodes
should be able to handle 10x much data. If partitioning is unfair it is called skewed. Skew makes partitioning less
effective. In order to reduce skew data needs to be distributed evenly.

One way is to assign a continuous range of keys to each partition (PARTITION 1: A-B, PARTITION 2: C-D, ...). The ranges
of keys are not necessarily evenly spaced, for example majority of entries with letter A. Partition boundaries need to
be carefully selected by application developer with domain knowledge. Partitioning by data is problematic too - all
writes going to single partition, whereas remaining partitions are idle. For example, you could solve this issue by
partitioning first by name (for example sensor name) and then by the time, this will balance the load.

Skew can be reduced by using hash function that is evenly distributing data across partitions. The partition boundaries
can be evenly spaced or chosen pseudorandomly (consistent hashing).

Consistent Hashing - a way of evenly distributing load across an internet-wide system of caches such as CDN. Uses
randomly chosen partition boundaries to avoid the need for central control or distributed consensus.

Using hash of the key loses the ability to do efficient range queries (sort order lost).

Hashing a key can reduce hot spots, but can not reduce them entirely. For example celebrity on social media can cause
storm of activity - this may lead to many writes to the same key. It is up to application developer to handle hot spots

- e.g. add random prefix.

Secondary indexes are slightly more problematic because they don't identify a record uniquely. There are 2 main
approaches to partitioning a database with secondary indexes:

- document-based (local index) - each partition have (local) partitioned secondary indexes, this means reading requires
  extra care. I am looking for a red car - needs to scatter query to two partitions - quite expensive. However, widely
  used.

- term-based (global index) - instead of each partition having its own secondary index, we can construct a global index.
  A global index also needs to be partitioned - for example secondary key `color:red`, cars with names a-d on partition
  0, rest on partition 1. Reads are more efficient, writes are slower.

Data change in the database - throughput increases, dataset increases, machine can fail. Rebalancing - the process of
moving data from one node to another. After rebalancing data should be shared fairly between nodes, when rebalancing
database should remain available for writes and reads and only minimal amount of data should be moved between nodes.

DO NOT USE hash mod N when rebalancing between partitions. Problem with this approach is that number of nodes changes.
This requires moving more data than necessary when new node is added.

Better solution is to create fixed number of partitions (more partitions than the nodes, e.g. 10 nodes - 1000
partitions)
. If new node is added to the cluster, it can steal few partitions from the others. The only thing that changes is
partitions assignment. This is followed by for example by ElasticSearch (number of partitions set up at the beginning).
Choosing the right number of partitions is difficult.

Dynamic partitioning is suitable for key range partitioning.

Automatic rebalancing can be unpredictable, because it is expensive operation - rerouting requests and moving a large
amount of data, this can overload the network. For this reason it is a good approach to have human administrator
performing rebalancing.

How to route request to particular partition? How can system know where is data? This problem is known as service
discovery. System can keep track of the data in separate register. Another possibility is that client connects to any
node, if node can not serve the request, client is forwarded to another node.

## Chapter 7: Transactions

Overhead of transactions > lack of transactions and coding around the lack of transactions.

A transaction is a way for an application to group several reads and writes together into a logical unit. Either entire
transaction succeeds (commit) or fails (abort, rollback). If transaction fails, application can retry. With this error
handling is much simpler.

However sometimes it might be beneficial to weaken transactions or abandon them entirely (for higher availability).

The safety guarantees provided by transactions are often described by ACID acronym. Implementations of ACID might vary
between DBMSs.

- Atomicity - (atomic refers to something that can not be broken into smaller parts), if error happens in the middle of
  transaction, it has to be reverted. If a transaction was aborted, the application can be sure that it didn't change
  anything, so it can be safely retried. Perhaps "abortability" would have been a better term than atomicity.
- Consistency - (terribly overloaded term) in ACID - certain statements about the data must be always true (for example
  correct account balance in banking system). If a transaction starts with a database that is valid, any writes during
  the transaction preserve the validity.
- Isolation - most databases are accessed by several clients at the same time, if they are accessing the same database
  records, you can run into concurrency problems. Isolation means that concurrently executing transactions are isolated
  from each other, they can not step on each other's toes. The classic database textbooks define isolation as
  serialisability (however this is rarely sued because it has performance penalty).
- Durability - the promise that once a transaction has committed successfully, any data it has written will not be
  forgotten, even if there is a hardware fault or the database crash. Anyhow, perfect durability does not exist (for
  example all backup destroyed at the same time).

ACID databases are based on this philosophy: "if the database is in danger of violating its guarantee of atomicity,
isolation or durability, it would rather abandon the transaction entirely than allow it to remain half-finished".

Isolation make life easier by hiding concurrency issues. In reality serialisation is not that simple, it has performance
cost , therefore it so common for systems to use weaker levels of isolation, which protect against some concurrency
issues. Common wisdom: "Use ACID databases if you are handling financial data", however many popular relational
databases use weak isolation even though are considered ACID.

Read committed - most basic level of transaction isolation, makes 2 guarantees:

- no dirty reads - you will only see data that has been committed
- no dirty writes - you will only override data that has been committed

Snapshot isolation - read committed is not solving all the issues (for example non-repeatable reads - when you select
data in the middle of transaction). Data unavailable for few seconds is not a problem, more problematic are long-lasting
data inconsistencies. Read committed is a boon for long-running , read-only queries such as backups and analytics.
Transaction should see a consistent snapshot of the database, frozen at a particular point in time (so data is not
changing when it is being processed). Key principle of snapshot isolation is: readers never block writers and writers
never block readers.

FOR UPDATE tells the database to lock all rows returned by this query.

Serialisable isolation is usually regarded as the strongest isolation level. It guarantees that even though transactions
may execute in parallel, the end result is the same as if they had executed one at a time, serially, without any
currency. Database prevents all possible race conditions.

The simplest way of avoiding concurrency problems is to remove the concurrency entirely - one transaction at a time, in
serial order or a single thread.

Stored procedures gained bad reputation for various reasons: each db vendor has its own language for stored procedures,
code running in a database is difficult to manage (hard to debug, awkward to version and deploy, trickier to test),
badly written procedure may harm overall DB performance. Modern implementations of stored procedures have abandoned
PL/SQL and use existing general-purpose programming languages instead.

Serial execution of transactions makes concurrency control much simpler, but limits the transaction throughput of the
database to the speed of a single CPU core on a single machine. Simple solution is to partition the database, each CPU
core have its own partition. However, if partition needs to access multiple partitions, the database must coordinate
across all the partitions that it touches.

Serial execution is a viable way of achieving serialisable isolation within certain constraints:

- every transaction must be small and fast
- write throughput must be low enough to be handled on a single CPU core
- cross-partition transactions are possible, but there is a hard limit to the extent to which they can be used

2PL - Two-Phase Locking - widely used algorithm for serialisability in databases. Similar to "no dirty writes" - if two
transactions concurrently try to write the same object, the lock ensure that the second writer must wait until the first
one has finished its transactions before it may continue. More specifically:

- If transaction A reads and B wants to write - B must wait until A commits or aborts
- If A writes and B wants to read, B must wait until A commits or aborts

2PL - writers don't just block other writes, they also block readers and vice-versa. The big downside of 2PL is
performance - worse throughput and response times comparing to weak isolation (because of overhead of acquiring and
releasing locks). Also called a "pessimistic concurrency control mechanism" - better to wait until situation is safe
before doing anything.

SI - Serialisable Snapshot Isolation - full serialisability with small performance penalty compared to snapshot
isolation. Very young technology - 2008. Called "optimistic concurrency control technique". Instead of blocking
potentially dangerous transactions, it allows them to work, hoping everything will turn out all right. When transaction
wants to commit, database checks if everything is fine. It performs badly in high contention (many transactions
accessing the same object) - many of transactions need to be aborted.

Reads from the database are made based on snapshot isolation.

## Chapter 8: The Trouble with Distributed Systems

Anything that can go wrong, will go wrong. Working with distributed systems is fundamentally different from writing
software on a single computer. When writing software that runs on several computers, connected by a network, the
situation is fundamentally different.

Partial failure - some parts of the system are broken in an unpredictable way. Partial failures are nondeterministic.
Nondeterminism and partial failures is what makes distributed systems hard to work with.

High-performance computing - supercomputers with thousands of CPUs are used for computationally intensive scientific
computing tasks, such as whether forecasting or molecular dynamics.

Cloud computing - often associated with multi-tenant data centres, commodity computers connected with an IP network,
on-demand resource allocation and metered billing.

Traditional enterprise data centres are somewhere between these two extremes.

If we want to make distributed systems work, we must accept the possibility of partial failure and build fault-tolerance
mechanisms into the software. We need to build a reliable system from unreliable mechanisms (like communication over the
internet, network may fail, bits might be lost, however it somehow works, engineers managed to build something reliable
basing on unreliable foundations).

What can go wrong when sending a request:

- request may be lost
- request might be waiting in a queue and will be delivered later
- remote node may have failed or temporarily stopped responding
- request might have been processed but was lost on a way back or was delayed or will be delivered later

Network problems can be surprisingly common, even in controlled environments like a datacenter operated by one company (
even 12 network faults per month in a medium-sized datacenter, half of them disconnected a single machine and a half an
entire rack). EC2 is notorious for having frequent transient network glitches.

Many systems need to automatically detect fault nodes, for example: load balancer needs to stop sending requests to a
node that is dead. Unfortunately it is hard to tell whether a node is working or not.

Timeout is the only sure way of detecting a fault. Appropriate duration of timeout is difficult to estimate. The
telephone network uses circuit - a fixed, guaranteed amount of bandwidth between 2 callers. On the other hand TCP
dynamically adapts the rate of data transfer to the available network capacity. TCP is optimised for busy networks,
circuit would not work for internet's use case.

Clocks and time is important, in distributed systems we never know the delay between send and received.

Time-of-day clocks - returns current date and time according to some calendar. Usually synchronised with NTP (Network
Time Protocol). Time-of-day clocks are unsuitable for measuring time (clock might be reset during measurement, because
it was desynchronised).

Monotonic clocks - suitable for measuring elapsed time, they are guaranteed to always move forward (time-of-day clock my
jump back in time). NTS may adjust monotonic clock frequency if it discovers it is too slow or too fast.

Software must be designed on the assumption that the network will occasionally be faulty, and the software must handle
such faults gracefully.

> Distributed systems are different from programs running on a single computer - there is no shared memory, only massage
> passing through unreliable network with variable delays and the systems may suffer from partial failures, unreliable
> clocks and processing pauses.

There are algorithms designed to solve distributed systems problems:

- synchronous model - assumes bounded network delay, process pauses and clock error, this means you know the delay, and
  it will not exceed some fixed value. This model is not realistic
- partially synchronous system - system behaves like a synchronous most of the time, but sometimes exceeds the bounds
  for network delay, process pauses and clock drift
- asynchronous model - any timing assumptions are not allowed
- crash-stop faults - algorithm may assume that a node can fail in only one way - by crashing, once crashed never comes
  back
- crash-recovery faults - node can fail at any moment, but has some nonvolatile disk storage that is preserved across
  crashes
- byzantine faults - nodes may do absolutely anything, including trying to trick and deceive other nodes

Partially synchronous and crash-recovery faults are the most common models.

Safety of a system - nothing bad happens, liveness of a system - something good eventually happens. These two are often
used for reasoning about the correctness of a distributed algorithm.

## Chapter 9: Consistency and Consensus

Tolerating faults - keeping the service functioning correctly, even if some internal component is faulty. The best way
of building fault-tolerant systems is to find some general-purpose abstractions with useful guarantees (e.g.
transactions).

When working with a database that provides only weak guarantees (e.g. eventual consistency), you need to be constantly
aware of its limitations (e.g. when you write and immediately read there is no guarantee that you will see the value you
just wrote).

LINEARIZABILITY (atomic consistency, strong consistency, immediate consistency) - is to make a system appear as if there
were only one copy of the data and all operations are atomic.

Easily confused with serialisability (both mean something like "can be arranged in a sequential order"):

- Serialisability - an isolation property of transactions, it guarantees that transactions behave the same as if they
  had executed in some serial order.
- Linearisability - a recency guarantee on reads and writes of a register, it doesn't group operations together into
  transactions, so does not prevent problems like write skew.

Use cases for linearisability:

- locking and leader election - a single-leader system needs to ensure there is indeed only one leader, not several (
  split brain) - it must be linearlisable, all nodes must agree which node owns the lock.
- constraints and uniqueness guarantees - for example unique usernames - you need linearisability. Hard uniqueness
  constraint requires linearisability.
- cross-channel timing dependencies - multiple components in a system can communicate which opens a possibility for race
  conditions

CAP theorem has been historically influential but nowadays has little practical value for designing systems. Better way
of paraphrasing CAP would be "either consistent or available when partitioned".

ORDERING GUARANTEES.

Causality imposes an ordering on the events (what happened before what) - question comes before answer, a message is
sent before it is received, ... These chains of casually dependent operations define the casual order in the system. If
system obeys the ordering imposed by causality, we say it is causally consistent.

Linearisability ensures causality. However, it is not the only way of preserving causality - system can be causally
consistent without incurring the performance (the strongest possible consistency model that does not slow down due to
network errors).

Sequence Number Ordering - sequence numbers or timestamps (not really time-of-day clock, but some logical clock) used to
order events. If there is not a single leader it is less clear how to generate sequence numbers for operations:

- each node can generate its own independent sequence number + node ID
- attach timestamp to each operation
- preallocate blocks of sequence numbers (1-1000 for node A, 1001-2000 for node B, ...)

Methods above allow generating unique sequence numbers efficiently, but do not capture correctly the ordering of
operations across different nodes.

Lamport timestamp - method for generating sequence numbers that is consistent with causality. Every node keeps track of
the maximum counter value it has seen so far, and includes that maximum on every request. Each node appends its node ID
to the final counter, if 2 counter values are the same, higher node ID wins.

The goal to get several nodes to agree on something is not easy, examples:

- leader election - lack of communication may lead to split brain (multiple nodes believe themselves to be the leader)
- atomic commit - in a system that supports transactions spanning several nodes, transaction may fail on some nodes but
  succeed on others (all nodes have to agree on the outcome - abort or accept)

The Impossibility of Consensus - there is no algorithm that is always able to reach consensus if there is a risk that a
node may crash, in a distributed system we must assume that node may crash, so reliable consensus is impossible.

Two-phase locking is an algorithm for achieving atomic transaction commit across multiple nodes (all commit or all
abort). 2 phases:

- the coordinator begins phase 1 - it sends prepare to each of the nodes, asking whether they are able to commit
- the coordinator tracks the responses from the participants, if all say yes - the coordinator sends out a commit
  request, if any of the participant say no - the coordinator sends an abort request to all nodes

This is very similar to wedding ceremony in Western cultures. If the decision was to commit there is no going back, no
matter how many retries it takes. The protocol has 2 crucial points of no return. If the coordinator dies, the nodes
should communicate and come to some agreement. 2PC has bad reputation because of operational problems, low performance
and promising more than it can deliver.

## Chapter 10: Batch Processing

> A system cannot be successful if it is too strongly influenced by a single person. Once the initial design is complete
> and fairly robust, the real test begins as people with many viewpoints undertake their own experiments.

3 types of systems:

- services (online systems) - a service waits for a request or instruction from a client to arrive, when received, the
  service tries to serve it as quickly as possible.
- batch processing (offline systems) - system takes a large amount of input data, runs a job to process it and produces
  some output data. Batch jobs are often scheduled to run periodically. The primary performance measure is throughput.
- stream processing systems (near-real-time systems) - something between online and offline systems. A stream processor
  consumes inputs and produces outputs (rather than responding to request).

Simple Batch Processing can be performed in UNIX via awk, grep and other command line tools (using a chain of commands).

The Unix Philosophy - the idea of connecting programs with pipes. This is possible because of common interface (programs
operating on file descriptors) of programs, which are small and are doing one thing.

The biggest limitation of UNIX tools is that they run only on a single machine and that is where tools like Hadoop come
in.

MapReduce is a bit like Unix tools, but distributed across potentially thousands of machines. MapReduce jobs read and
write files on a distributed filesystem, in Hadoop's implementation of MapReduce the filesystem is called HDFS (Hadoop
Distributed File System - reimplementation of the Google File System).

HDFS is based on the shared-nothing principle. HDFS consists of a daemon process running on each machine, exposing a
network service that allows other nodes to access files stored on that machine. In order to tolerate machine and disk
failures, file blocks are replicated on multiple machines.

To create a MapReduce job, you need to implement 2 callback functions:

- mapper - called once for every inout record, its job is to extract the key and value from the input record.
- reducer - the framework takes the key-value pairs produced by the mapper, collects all the values belonging to the
  same key and calls the reducer with an iterator over collection of values.

Principle:

> Put the computation near the data

it saves copying the input file over the network, reducing network load and increasing locality.

In order to achieve good throughput in a batch processing, the computation must be as much as possible local in one
machine.

HDFS is somewhat like a distributed version of UNIX, where HDFS is the filesystem and MapReduce is a quirky
implementation of a UNIX process. When MapReduce was published it was not all new. Some concepts were already known -
e.g. massively parallel processing databases. Hadoop vs Distributed Databases:

- databases require you to structure data according to particular model, whereas files in a distributed filesystem are
  just byte sequences. Hadoop opened up the possibility of indiscriminately dumping data into HDFS and later figuring
  out how to process it further. MPP databases require careful, up-front modeling of the data. The Hadoop has often been
  used for implementing ETL processes, MapReduce jobs are written to clean up the data, transform it into a relational
  form and import it into an MPP data warehouse for analytic purposes.
- MPP databases are great because they take care of storage, query planning and execution, moreover they use SQL -
  powerful query language. On the other hand not all kinds of processing can be sensibly expressed as SQL queries (
  recommendation systems, full-text search or image analysis). MapReduce gave the engineers the ability to easily run
  their own code over large datasets.
- MPP databases and MapReduce took different approach to handling faults and the use of memory and disk. Natch processes
  are less sensitive to faults than online systems, because they do not immediately affect users if they fail, and they
  always can be run again. If a node fails, most MPP databases abort the entire query, MapReduce can tolerate the
  failure of a map or reduce task. MapReduce dumps partial results to the disk, so they can be restored after failure.
  MPP databases are more willing to store data in the memory for faster access. MapReduce is designed to tolerate
  frequent unexpected task termination, not because hardware is unreliable, it is because the freedom to arbitrarily
  terminate processes enables better resource utilisation in a computing cluster (Google came up wit this idea, this
  design was designed by their resource usage).

MapReduce is just one of many possible programming models for distributed systems. MapReduce has problems with *
materialisation* of the data - the process of writing out intermediate state files. Several new execution engines for
distributed batch processing were developed in order to fix this problem with MapReduce (data-flow engines) - Spark,
Tez, Flink. Dataflow engines provide several options for connecting one operator's output to another's input - sort by
key, tak several inputs and to partition them, but skip the sorting, for broadcast hash joins, the same output from one
operator can be sent to all partitions of the join operator.

Systems like Dryrad and Nephele offer several advantages compared to MapReduce model:

- expensive work (e.g. sorting) only performed in places where it is actually required
- no unnecessary map tasks
- intermediate state between operators kept in memory or written to local disk
- operators can start executing as soon as their input is ready
- existing JVMs can be reused to run new operators

Fully materialised intermediate state to a distributed filesystem makes fault tolerance fairly easy in MapReduce. Spark,
FLink and Tes avoid writing intermediate state to HDFS.

MapReduce - is like writing the output of each command to a temporary file.

Dataflow engines look like much more like UNIX pipes (final result still might be saved to HDFS).

High level APIs like Hive, Pig, Cascading and Crunch became popular because programming MapReduce jobs is quite
laborious.

## Chapter 11: Stream Processing

> Complex systems always evolve from simple system that works. A complex system designed from scratch never works and
> cannot be made to work.

Batch processing must artificially divide data into chunks of fixed duration (for example: processing a day's worth of
data at the end of every day). The problem with daily batch processes is that changes in the input are only reflected in
the output a day later, which is too slow for many impatient users. Delay can be reduced by running the processing more
frequently.

Stream processing - processing every event as it happens. "Stream" refers to data that is incrementally made available
over time.

Event - a small, self-contained, immutable object containing the details of something that happened at some point in
time. An event usually contains a timestamp indicating when it happened (according time-of-day clock). Related events
are usually grouped together into a topic or stream.

Polling the datastore to check for events that have appeared since it last ran becomes expensive if the datastore is not
designed for this kind of usage. It is better for consumers to be notified when new events appear.

Common approach for notifying consumers about new events is to use a messaging system - producer sends a message
containing the event, which is then pushed to consumers.

Direct messaging - direct communication between producers and consumers without going via intermediary nodes. Brokerless
libraries: ZeroMQ, nanomsg - pub-sub messaging over TCP or IP multicast. StatsD and Brubeck use unreliable UDP messaging
for collecting metrics from all machines on the network and monitoring them. Webhooks - a pattern in which a callback
URL of one service is registered with another service, and it makes a request to that URL whenever an event occurs.

Message brokers - kind of database, that is optimised for handling message streams. It runs as a server, with producers
and consumers connecting to it as clients. Producers write messages, consumers receive them by reading them from the
broker. By centralising the data in the broker, these systems can more easily tolerate clients that come and go. A
consequence of queueing is also that consumers are generally asynchronous: when a producer send a message it normally
only waits for the broker to confirm that it has buffered the message, and it does not wait for the message to be
consumed.

Multiple consumers - when multiple consumers read messages in the same topic, two main patterns of messaging are used:

- load balancing - each message is delivered to one of the consumers, so the consumers can share the work of processing
  the messages in the topic. This pattern is useful then the messages are expensive to process, and you want to bale to
  add consumers to parallelize the processing.
- fan-out - each message is delivered to all the consumers, equivalent of having several batch jobs that read the same
  input file.

Message brokers use acknowledgements: a client must explicitly tell the broker when it has finished processing a message
so that the broker can remove it from the queue.

Messages can go out of order because for example network problem and lack of acknowledgement.

Log-based message brokers - durable storage approach of databases combined with the low-latency notification facilities
of messaging. A log is simply an append-only sequence of records on disk. A producer can send a message by appending it
to the end of the log and a consumer can receive message by reading the log sequentially.

In order to scale to higher throughput that a single disk can offer, the log can be partitioned. Different partitions
can be hosted on different machines. A topic can then be defined as a group of partitions that carry messages of the
same type.

Apache Kafka, Amazon Kinsesis Streams and Twitter's DistributedLog are log-based message brokers. Google Pub/Sub is
architecturally similar but exposes a JMS-style API rather than log abstraction.

Even though these message brokers write all messages to disk, they are able to achieve throughput of millions of
messages per second by partitioning across multiple machines.

Log-based approach trivially supports fan-out messaging.

Change Data Capture - the process of observing all data changes written to a database and extracting them in a form in
which they can be replicated to other systems. You can capture the changes in a database and continually apply the same
changes to search index.

Event Sourcing - involves storing all changes to the application state as log of change events. Events are designed to
reflect things that happened at the application level, rather than low-level state changes. Powerful technique for data
modeling: from an application point of view it is more meaningful to record the user's actions as immutable events,
rather than recording the effect of those actions on a mutable database: "student cancelled their course enrolment" vs "
one entry was deleted from the enrolments table". Event Store is a specialised database to support applications using
event sourcing.

Applications that use event sourcing typically have some mechanism for storing snapshots of the current state that is
derived from the log of events, so they don't need to repeatedly reprocess the full log.

CQRS - Command Query Responsibility Segregation - separating the form in which data is written from the form it is read,
by allowing several read views.

Streams can be used to produce other, derived streams. Stream processing has long been used for monitoring purposes:
fraud detection, trading system examining price changes, machines monitoring, monitoring in military.

Complex Event Processing (CEP) - an approach developed in the 1990s for analysing event streams, especially geared
toward the kind of application that requires searching for certain event patterns. CEP allows you to specify rules to
search for certain patterns of events in a stream. CEP systems use a high-level declarative query language like SQL or
GUI.

Stream processing is used also for analytics on streams, boundary between CEP and stream analytics is blurry.
Frameworks: Apache Storm, Spark Streaming, Flink, Concord, Samza, Kafka Streams, Google Cloud Dataflow, Azure Stream
Analytics.

Types of time windows:

- tumbling windows - has a fixed length, and every event belongs to exactly one window. Fo example 1-minute tumbling
  window, events with timestamp between 10:03:00 and 10:03:59 are grouped into one window.
- hopping window - has a fixed length, but allows windows to overlap in order to provide some smoothing.
- sliding window - contains all the events that occur within some interval of each other. For example. a 5-minute
  sliding window would cover events at 10":03:39 and 10:08:12 because they are less than 5 minutes apart.
- session window - has no fixed duration, instead it is defined by grouping together all events for the same user that
  occur closely together in time, and the window ends when the user has been inactive for some time.

Types of stream joins:

- stream-stream join (window join) - you need to choose a suitable window for the join (seconds, days weeks between
  events), also be careful about ordering of received events.
- stream-table join (stream enrichment) - to perform this join, the stream process needs to look at one activity event
  at a time, look up something in the database (local or remote)
- table-table join (materialised view maintenance) - twitter example: when user wants to see their feed, it is too
  expensive to load all profiles' most recent tweets, instead we want a timeline cache, so reading is a simple lookup.
  To implement cache maintenance (append to cache new tweets, remove deleted, ...) you need streams of events for
  tweets.

If events on different streams happen around a similar time, in which order they are processed? If the ordering of
events across streams is undetermined, the join becomes nondeterministic, which means you cannot rerun the same job on
the same input and get the same result. In data warehouses, this issue is known as a slowly changing dimension (SCD). It
is often addressed by using a unique identifier for a particular version of the joined record.

Batch processing frameworks can tolerate faults fairly easily. In stream processing, fault tolerance is less
straightforward to handle. Possible approaches:

- microbatching and checkpointing - break the stream into small blocks, and treat each block like a miniature batch
  process (used in Spark Streaming, batch approx. 1 second long). Apache Flink periodically generate rolling checkpoints
  of state and write them to durable storage.
- atomic commit revisited - in order to give the appearance of exactly-once processing in the presence of faults, we
  need to ensure that all outputs and side effects of processing take effect if and only if the processing is
  successful. Exactly-once message processing in the context of distributed transactions and two-phase commit.
- idempotence - our goal is to discard the partial output of any failed tasks so that they can be safely retried without
  taking effect twice. Distributed transactions are the one way of achieving this, but another way is to rely on
  idempotence. An idempotent operation is one that you can perform multiple times, and it has the same effect as if you
  performed it only once (e.g. setting key in a key-value store, incrementing counter value is not idempotent). Even if
  an operation is not naturally idempotent, it can often be made idempotent with a bit of extra metadata.

## Chapter 12: The Future of Data Systems

The lambda architecture - incoming data should be recorded by appending immutable events to an always-growing dataset,
similarly to event sourcing. From these events, read-optimised views are derived. The lambda architecture proposes
running two different systems in parallel. In the lambda approach, the stream processor consumes the events and quickly
produces an approximate update to the view, the batch processor later consumes the same set of events and produces a
corrected version of derived view.

Federated databases - unifying reads - it is possible to provide a unified query interface to a wide variety of
underlying storage engines and processing methods - an approach known as a federated database or polystore.

Unbundled databases - unifying writes - making it easier to reliably plug together storage systems is like unbundling a
database's index-maintenance features in a way that can synchronise writes across disparate technologies.

Hardware is not quite the perfect abstraction that it may seem. Random bit-flips are very rare on modern hardware but
can happen. Even software lik MySQL or PostgreSQL can have bugs.

Large scale storage systems like HDFS or Amazon S3 do not fully trust disks: they run background processes that
continually read back files, compare them to other replicas and move files from one disk to another, in order to
mitigate the risk of silent corruption.

ACID databases has led us toward developing applications on the basis of blindly trusting technology. Since the
technology we trusted worked well enough most time, auditing mechanisms were deemed worth the investment.

Having continuous end-to-end integrity checks gives you increased confidence about the correctness of your systems,
which in turn allows you to move faster (like automated testing software).

It is not sufficient for software engineers to focus exclusively on the technology and ignore its ethical consequences.
Users are humans and human dignity is paramount.

Algorithmic prison - systematically being excluded from jobs, air travel, insurance coverage, property rentals,
financial services, ... because algorithm said NO. In countries that respect human rights, the criminal system presumes
innocence until proven guilty, on the other hand automated systems can systematically exclude a person from
participating in society without any proof of guilt and with little chance of appeal.

Decisions made by an algorithm are not necessarily any better or worse than those made by a human. Every person is
likely to have biases. In many countries, anti-discrimination laws prohibit treating people differently depending on
protected traits (ethnicity, age, gender, sexuality, disability, beliefs).

Automated decision-making opens the question of responsibility and accountability. Who is responsible if self-driving
car causes an accident?

Besides, the problems of predictive analysis, there are ethical problems with data collection itself. Though experiment,
whenever you see "data" (e.g. data driven company), replace it with the word surveillance (e.g. surveillance driven
company). Even the most totalitarian and oppressive regimes could only dream of putting a microphone in every room and
forcing every person to constantly carry a device capable of tracking their location and movements.

Declining to use a service due to its tracking of users is only an option for the small number of people who are
privileged enough to have the time and knowledge to understand its privacy policy and who are can afford to potentially
miss out on social participation opportunities.

When collecting data, we need to consider not just today's political environments, but all possible future governments.  
