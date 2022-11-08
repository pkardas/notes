[go back](https://github.com/pkardas/learning)

# Fundamentals of Software Architecture: An Engineering Approach.

Book by Mark Richards and Neal Ford

- [Preface: Invalidating Axioms](#preface-invalidating-axioms)
- [Chapter 1: Introduction](#chapter-1-introduction)
- [Chapter 2: Architectural thinking](#chapter-2-architectural-thinking)
- [Chapter 3: Modularity](#chapter-3-modularity)
- [Chapter 4: Architecture Characteristics Defined](#chapter-4-architecture-characteristics-defined)
- [Chapter 5: Identifying Architectural Characteristics](#chapter-5-identifying-architectural-characteristics)
- [Chapter 6: Measuring and Governing Architecture Characteristics](#chapter-6-measuring-and-governing-architecture-characteristics)
- [Chapter 7: Scope of Architecture Characteristics](#chapter-7-scope-of-architecture-characteristics)
- [Chapter 8: Component-Based Thinking](#chapter-8-component-based-thinking)
- [Chapter 9: Foundations](#chapter-9-foundations)
- [Chapter 10: Layered Architecture Style](#chapter-10-layered-architecture-style)
- [Chapter 11: Pipeline Architecture Style](#chapter-11-pipeline-architecture-style)
- [Chapter 12: Microkernel Architecture Style](#chapter-12-microkernel-architecture-style)
- [Chapter 13: Service-Based Architecture Style](#chapter-13-service-based-architecture-style)
- [Chapter 14: Event-Driven Architecture Style](#chapter-14-event-driven-architecture-style)
- [Chapter 15: Space-Driven Architecture Style](#chapter-15-space-driven-architecture-style)
- [Chapter 16: Orchestration-Driven Service-Oriented Architecture](#chapter-16-orchestration-driven-service-oriented-architecture)
- [Chapter 17: Microservices Architecture](#chapter-17-microservices-architecture)
- [Chapter 18: Choosing the Appropriate Architecture Style](#chapter-18-choosing-the-appropriate-architecture-style)
- [Chapter 19: Architecture Decisions](#chapter-19-architecture-decisions)
- [Chapter 20: Analyzing Architecture Risk](#chapter-20-analyzing-architecture-risk)
- [Chapter 21: Diagramming and Presenting Architecture](#chapter-21-diagramming-and-presenting-architecture)
- [Chapter 22: Making Teams Effective](#chapter-22-making-teams-effective)
- [Chapter 23: Negotiation and Leadership Skills](#chapter-23-negotiation-and-leadership-skills)
- [Chapter 24: Developing a Career Path](#chapter-24-developing-a-career-path)
- [Self-Assessment Questions](#self-assessment-questions)

## Preface: Invalidating Axioms

> Axiom - A statement or proposition which is regarded as being established, accepted, or self-evidently true.

Software architects (like mathematicians) also build theories atop axioms (but the software world is _softer_ than
mathematics).

Architects have an important responsibility to question assumptions and axioms left over from previous eras. Each new
era requires new practices, tools, measurements, patterns, and a host of other changes.

## Chapter 1: Introduction

The industry does not have a good definition of software architecture.

> Architecture is about the important stuff... whatever that is ~ Ralph Johnson

The responsibilities of a software architect encompass technical abilities, soft skills, operational awareness, and a
host of others.

When studying architecture - keep in mind that everything can be understood in context - why certain decisions were
made, was based on the realities of the environment (for example building microservice architecture in 2002 would be
inconceivably expensive).

Knowledge of the architecture structure, architecture characteristics, architecture decisions, and design principles is
needed to fully understand the architecture of the system.

- structure/style: microservices, layered, microkernel, ...
- characteristics: availability, reliability, scalability, fault tolerance, security, ...
- decisions: what is and what is not allowed, rules for a system how it should be constructed
- design principles: guidelines for constructing systems -- leverage async messaging between services to increase
  performance

Expectations of an architect:

- make architecture decisions
    - instead of making technical decisions (use React.js), instruct development teams (use a reactive-based framework)
- continually analyze the architecture
    - validate decisions made years ago in order to prevent structural decay
- keep current with the latest trends
    - the decisions an architect makes tend to be long-lasting and difficult to change. understanding and following key
      trends helps the architect prepare for the future
- ensure compliance with decisions
    - continually verify that development teams are following the architecture decisions and design principles defined
- diverse exposure and experience
    - an architect should be at least familiar with a variety of technologies, effective architect should be aggressive
      in seeking out opportunities to gain experience in multiple languages, platforms and technologies
- have business domain knowledge
    - without business knowledge, an architect cannot communicate with stakeholders and business users and will quickly
      lose credibility
- possess interpersonal skills
    - interpersonal skills, including teamwork, facilitation, and leadership
    - engineers love to solve technical problems, however G. Weinberg said: "no matter what they tell you, it is always
      a people problem"
    - many architects are excellent technologists, but are ineffective architects because of poor communication skills
- understand and navigate politics
    - have negotiation skills, almost every decision an architect makes will be challenged

> All architectures become iterative because of _unknown unknowns_. Agile just recognizes this and does it sooner.

Iterative process fits the nature of software architecture. Trying to build a modern system such as microservices using
Waterfall will find a great deal of friction.

Nothing remain static. What we need is _evolutionary architecture_ - mutate the solution, evolve new solutions
iteratively. Adopting Agile engineering practices (continuous integration, automated machine provisioning, ...) makes
building resilient architectures easier.

Agile methodologies support changes better than planning-heavy processes because of tight feedback loop.

Laws of Software Architecture:

- Everything in software architecture is a trade-off
- If an architect thinks they have discovered something that isn't a trade-off, more likely they just haven't identified
  the trade-off yet
- Why is more important than how

## Chapter 2: Architectural thinking

4 main aspects of thinking like an architect:

1. understanding the difference between architecture and design
    - architecture vs design
        - architecture: defining architecture characteristics, selecting architecture patterns, creating components
        - design: class diagrams, user interface, code testing and development
    - architects and development teams have to form strong bidirectional relationship, be on the same virtual team
    - where does architecture end and design begin? nowhere
    - architecture and design must be synchronized by tight collaboration
2. wide breadth of technical knowledge
    - developer - significant amount of technical depth
        - specialised in languages, frameworks and tools
    - architect - significant amount of technical breadth
        - broad understanding of technology and how to use it to solve particular problems
3. understanding, analyzing, and reconciling trade-offs between various solutions and technologies
    - thinking like an architect is all about seeing trade-offs in every solution
    - the ultimate answer for architectural questions: _it depends on ..._ (budget, business env, company culture, ...)
    - look at the benefits of a given solution, but also analyze the negatives
    - analyze trade-offs and the ask, what is more important, this decision always depend on the environment
4. understanding the importance of business drivers
    - business drivers are required for the success of the system
    - understanding the domain knowledge and ability to translate those requirements into architecture characteristics

_Frozen Caveman Anti-Pattern_: describes an architect who always reverts to their pet irrational concern for every
architecture. This anti-pattern manifests in architects who have been burned in the past by a poor decision/unexpected
occurrence, making them particularly cautious in the future.

How an architect can remain hands-on coding skills?

- do frequent proof-of-concepts
- whenever possible, write best production-quality code (even when doing POCs) -- POC code often remains in the
  repository and becomes the reference or guiding example
- tackle technical debt stories or architecture stories, freeing the development team up to work on the critical
  function user stories
- work on bug fixes
- create simple command-line tools and analyzers to help the development team with their day-to-day tasks
- do code reviews frequently

## Chapter 3: Modularity

Modularity is an organizing principle. If an architect designs a system without paying attention to how the pieces wire
together, they end up creating a system that presents myriad difficulties.

Developers typically use modules as a way to group related code together. For discussions about architecture, we use
modularity as a general term to denote a related grouping of code: classes, functions, or any other grouping.

_Cohesion_ - refers to what extent the parts of a module should be contained within the same module. It is a measure of
how related the parts are to one another.

_Abstractness_ is the ratio of abstract artifacts to concrete artifacts. It represents a measure of abstractness versus
implementation. A code base with no abstractions vs a code base with too many abstractions.

## Chapter 4: Architecture Characteristics Defined

Architects may collaborate on defining the domain or business requirements, but one key responsibility entails defining,
discovering, and analyzing all the things the software must do that isn't directly related to the domain functionality
-- architectural characteristics.

Operational Architecture Characteristics:

- Availability - how long the system will need to be available
- Continuity - disaster recovery capability
- Performance - stress testing, peak analysis
- Recoverability - how quickly is the system required to be on-line again?
- Reliability - if it fails, will it cost the company large sums of money?
- Robustness - ability to handle error and boundary conditions while running
- Scalability - ability for the system to perform and operate as the number of users/requests increases

Structural Architecture Characteristics

- Configurability - ability for the end users to easily change aspects of the software's configuration
- Extensibility - how important it is to plug new pieces of functionality in
- Installability - ease of system installation on all necessary platforms
- Localization - support for the multiple languages, currencies, measures
- Maintainability - how easy it is to apply changes and enhance the system?
- Portability - does the system need to run on more than one platform?
- Supportability - what level of technical support is needed by the application?
- Upgradeability - ability to quickly upgrade from a previous version

Cross-cutting Architecture Characteristics

- Accessibility - access to all users, including those with disabilities
- Archivability - will the data need to be deleted/archived?
- Authentication - security requirements to ensure users are who they say they are
- Authorization - security requirements to ensure users can access only certain functions within application
- Legal - what legislative constraints is the system operation in?
- Privacy - ability to hide transactions from internal company employees
- Security - does the data need to be encrypted in the database, what type of authentication is needed...?
- Supportability - what level of technical support is needed by the application?
- Usability - level of training required for users to achieve their goals with the app

Any list of architecture characteristics will be an incomplete list. Any software may invent important architectural
characteristics based on unique factors. Many of the terms are imprecise and ambiguous. No complete list of standards
exists.

Applications can support only a few of the architecture characteristics we have listed. Firstly, each of the supported
characteristics requires design effort. Secondly, each architecture characteristic often has an impact on others.
Architects rarely encounter the situation where they are able to design a system and maximize every single architecture
characteristics.

> Never shoot for the best architecture, but rather _the least worst_ architecture.

Too many architecture characteristics lead to generic solutions that are trying to solve every business problem, and
those architectures rarely work because the design becomes unwieldy. Architecture design should be as iterative as
possible.

## Chapter 5: Identifying Architectural Characteristics

Identifying the correct architectural characteristics for a given problem requires an architect to not only understand
the domain problem, but also collaborate with the problem domain stakeholders to determine what is truly important from
a domain perspective.

_Extracting architecture characteristics from domain concerns_: translate domain concerns to identify the right
architectural characteristics. Do not design a generic architecture, focus on short list of characteristics. Too many
characteristics leads to greater and greater complexity. Keep design simple. Instead of prioritizing characteristics,
have the domain stakeholders select the top 3 most important characteristics from the final list.

Translation of domain concerns to architecture characteristics:

- Mergers and acquisition -> Interoperability, scalability, adaptability, extensibility
- Time to market -> Agility, testability, deployability
- User satisfaction -> Performance, availability, fault tolerance, testability, deployability, agility, security
- Competitive advantage -> Agility, testability, deployability, scalability, availability, fault tolerance
- Time and budget -> Simplicity, feasibility

_Extracting architecture characteristics from requirements_: some characteristics come from explicit statements in
requirements.

Architecture Katas - in order te become a great architect you need a practice. The Kata exercise provides architects
with a problem stated in domain terms (description, users, requirements) and additional context. Small teams work 45
minutes on a design, then show results to the other groups, who vote on who came up with the best architecture. Team
members ideally get feedback from the experienced architect abut missed trade-offs and alternative designs.

Explicit characteristics - appear in a requirements' specification, e.g. support for particular number of users.

Implicit characteristics - characteristics aren't specified in requirements documents, yet they make up an important
aspect of the design, e.g. availability - making sure users can access the website, security - no one wants to create
insecure software, ...

Architects must remember: there is no best design in architecture, only a least worst collection of trade-offs.

## Chapter 6: Measuring and Governing Architecture Characteristics

- They aren't physics - many characteristics have vague meanings, the industry has wildly differing perspectives
- Wildly varying definitions - different people may disagree on the definition, without agreeing on a common definition,
  a proper conversation is difficult
- Too composite - many characteristics compromise may others at a smaller scale

Operational measures: obvious direct measurements, like performance -- measure response time. High-level teams don't
just establish hard performance numbers, they base their definitions on statistical analysis.

Structural measures: addressing critical aspects of code structure, like cyclomatic complexity - the measurement for
code complexity, computed by applying graph theory to code.

> Overly complex code represents a code smell. It hurts almost every of the desirable characteristics of code bases
> (modularity, testability, deployability, ...). Yet if teams don't keep an eye on gradually growing complexity,
> that complexity will dominate the code base.

Process measures: some characteristics intersect with software development processes. For example, agility can relate to
the software development process, ease of deployment and testability requires some emphasis on good modularity and
isolation at the architecture level.

Governing architecture characteristics - for example, ensuring software quality within an organization falls under the
heading of architectural governance, because it falls within the scope of architecture, and negligence can lead to
disastrous quality problems.

_Architecture fitness function_ - **any mechanism** that provides an objective integrity assessment of some architecture
characteristic or combination of architecture characteristics. Many tools may be used to implement fitness functions:
metrics, monitors, unit tests, chaos engineering, ...

Rather than a heavyweight governance mechanism, fittness functions provide a mechanism for architects to express
important architectural principles and automatically verify them. Developer know that they shouldn't release insecure
code, but that priority competes with dozens or hundreds of other priorities for busy developers. Tools like the
Security Monkey, and fitness functions generally, allow architects to codify important governance checks into the
substrate of the architecture.

## Chapter 7: Scope of Architecture Characteristics

When evaluating many operational architecture characteristics, an architect must consider dependent components outside
the code base that will impact those characteristics.

_Connascence_ - Two components are connascent is a change in one would require the other to be modified in order to
maintain the overall correctness of the system.

If two services in a microservices architecture share the same class definition of some class, they are statically
connascent. Dynamic connascence: synchronous - caller needs to wait for the response from the callee, asynchronous calls
allow fire-and-forget semantics in event-driven architecture.

Component level coupling isn't the only thing that binds software together. Many business concepts semantically bind
parts of the system together, creating functional cohesion.

_Architecture quantum_ - an independently deployable artifact with high functional cohesion and synchronous connascence.

- independently deployable - all necessary components to function independently from other parts of the architecture (
  e.g. a database - the system will not function without it)
- high functional cohesion - how well the contained code is unified in purpose, meaning - an architecture quantum needs
  to do something purposeful
- synchronous connascence - synchronous call within an application context of between distributed services that form
  this architecture quantum.

## Chapter 8: Component-Based Thinking

Architects typically think in terms of components, the physical manifestation of a module. Typically, the architect
defines, refines, manages, and governs components within an architecture.

Architecture Partitioning - several styles exist, with different sets of trade-offs (layered architecture, modular
monolith).

> Convay's Law: Organizations which design systems ... are constrained to produce designs which are copies of
> the communication structures of these organizations.

This law suggests that when a group of people deigns some technical artifact, the communication structures between the
people end up replicated in the design.

Technical partitioning - organizing components by technical capabilities (presentation, business rules, persistence).

Domain partitioning - modeling by identifying domains/workflows independent and decouples from another. Microservices
are based on this philosophy.

Developer should never take components designed by architects as the last words. All software design benefits from
iteration. Initial design should be viewed as a first draft.

Component identification flow:

- identify initial components
- assign requirements to components
- analyze roles and responsibilities
- analyze architecture characteristics
- restructure components

Finding proper granularity for components is one of most difficult tasks. Too fine-grained design leads to too much
communication between components, too coarse-grained encourage high internal coupling.

Discovering components:

- entity trap - anti-pattern when an architect incorrectly identifies the database relationships, this anti-pattern
  indicates lack of thought about the actual workflows of the application.
- actor-actions approach - a popular way to map requirements to components, identify actors who perform activities with
  the application and the actions those actors may perform.
- event storming - the architect assumes the project will use messages and/or events to communicate between components,
  the team tries to determine which events occur in the system based on requirements and identified roles, and build
  components around those event and message handlers.
- workflow approach - identifies the key roles, the kinds of workflows, and builds components around the identified
  activities

Monolithic vs Distributed Architecture:

- monolithic: a single deployable unit, all functionality of the system that runs in the process, typically connected to
  a single database
- distributed: multiple services running in their onw ecosystem, communicating via network, each service can may have
  its own release cadence and engineering practices

## Chapter 9: Foundations

Architecture styles (a.k.a. architecture patterns) - describe a named relationship of components covering a variety of
architecture characteristics. Style name, similar to design patterns, creates a single name that acts as shorthand
between experienced architects.

Big Ball of Mud - the absence of any discernible architecture structure. The lack of structure makes change increasingly
difficult. Problematic testing, deployment, scalability, performance, ... Mess because of lack of governance around code
quality and structure.

Client/Server - separation of responsibilities - backend-frontend/two-tier/client-server.

Architecture styles can be classified into 2 main types:

- monolithic - single deployment of unit code
    - layered, pipeline, microkernel
- distributed - multiple deployment units connected through network
    - service-based, event-driven, space-based, service-oriented, microservices
    - much more powerful in terms of performance, scalability, and availability, but there are trade-offs

_The Fallacies of Distributed Computing:_

1. The Network is Reliable - fact: networks still remain generally unreliable, this is why things like timeouts and
   circuit breakers exist between services. The more a system relies on the network, the potentially less reliable it
   becomes.
2. Latency is Zero - local call is measured in nanoseconds/microseconds, the same call made through a remote access
   protocol is measured in milliseconds. Do you know what the average round-trip latency is for a RESTful call in your
   prod env?
3. Bandwidth is Infinite - communication between remote services significantly utilizes bandwidth causing networks to
   slow down. Imagine 2000 req/s, 500 kb each = 1 Gb! Ensuring that the minimal amount of data is passed between
   services in a distributed architecture is the best way to address this fallacy.
4. The Network is Secure - the surface area for threats and attacks increases by magnitudes when moving from a
   monolithic to a distributed architecture, despite measures like VPNs, trusted networks and firewalls.
5. The Topology Never Changes - network topology (routers, hubs, switches, firewalls, networks, appliances) CAN change,
   architects must be in constant communication with operations and network administrators to know what is changing and
   when so they can make adjustments.
6. There is Only One Administrator - this fallacy points to the complexity of distributed architecture and the amount of
   coordination that must happen to get everything working correctly. Monoliths do not require this level of
   communication and collaboration due to the single deployment unit characteristics.
7. Transport Cost is Zero - transport cost does not refer to latency, but rather to actual cost in terms of money
   associated with making a simple RESTful call. Distributed architectures cost significantly more than monolithic
   architectures, primarily due to increased needs for additional hardware, servers, gateways, firewalls, subnets,
   proxies, ...
8. The Network is Homogenous - notwork is not made up by one network hardware vendor, not all of this heterogeneous
   hardware vendors play well together.

Other distributed considerations:

- distributed logging - debugging in a distributed architecture is very difficult and time-consuming, logging
  consolidation tools may help.
- distributed transactions - in a monolith it is super easy to perform `commit`/`rollback`, it is much more difficult
  todo the same in a distributed system. Distributed systems rely on eventual consistency - this is one of the
  trade-offs. Transactional SAGAs are one way to manage distributed transactions.
- contract maintenance and versioning - a contract is behaviour and data that is agreed upon by both the client and
  service, maintenance is hard due to decoupled services owned by different teams and departments.

## Chapter 10: Layered Architecture Style

The Layered Architecture (n-tiered) - standard for most applications, because of simplicity, familiarity, and low cost.
The style also falls into several architectural anti-patterns (architecture by implication, accidental architecture).

Most layered architectures consist of 4 standard layers: presentation, business, persistence, and database.

The layered architecture is a technically partitioned architecture (as opposed to domain-partitioned architecture).
Groups of components, rather than being grouped by domain, are grouped by their technical role in the architecture. As a
result, any particular business domain is spread throughout all of the layers of the architecture. A domain-driven
design does not work well with the layered architecture style.

Each layer can be either closed or open.

- closed - a request moves top-down from layer to layer, the request cannot skip any layers
- open - the request can bypass layers (fast-lane reader pattern)

The layers of isolation - changes made in one layer of the architecture generally don't impact/affect components in
other layers. Each layer is independent of the other layers, thereby having little or no knowledge of the inner workings
of other layers in the architecture. Violation of this concept produces very tightly coupled application with layer
interdependencies between components This type of architecture becomes very brittle, difficult and expensive to change.

This architecture makes for a good starting point for most applications whe it is not known yet exactly which
architecture will ultimately be used. Be sure to keep reuse at minimum and keep object hierarchies. A good level of
modularity will help facilitate the move to another architecture style later on.

Watch out for the architecture sinkhole anti-pattern - this anti-pattern occurs when requests move from one layer to
another as simple pass-through processing with no business logic performed within each layer. For example, the
presentation layer responds to a simple request from the user to retrieve basic costumer data.

## Chapter 11: Pipeline Architecture Style

Pipeline (a.k.a. pipes, filters) architecture: _Filter -(Pipe)-> Filter -(Pipe)-> Filter -(Pipe)-> Filter_

- pipes - for the communication channel between filters, each pipe is usually unidirectional and point-to-point.
- filters - self-contained, independent from other filters, stateless, should perform one task only. 4 types of filters
  exist within this architecture style
    - producer - the starting point of a proces, sometimes called the source
    - transformer - accepts input, optionally performs a transformation on data, then forwards it to the outbound pipe,
      also known as "map"
    - tester - accepts inout, tests criteria, then optionally produces output, also known as "reduce"
    - consumer - the termination point for the pipeline flow, persist or display the final result

ETL tools leverage the pipeline architecture for the flow and modification of data from one database to another.

## Chapter 12: Microkernel Architecture Style

The microkernel architecture style (a.k.a plug-in) - a relatively simple monolithic architecture consisting of two
components: a core system and plug-in components.

Core system - the minimal functionality required to run the system. Depending on the size and complexity, the core
system can be implemented as a layered architecture or modular monolith.

Plug-in components - standalone, independent components that contain specialized processing, additional features, and
custom code meant to enhance or extend the core system. Additionally, they can be used to isolate highly volatile code,
creating better maintainability and testability within the application. Plug-in components should have no-dependencies
between them.

Plug-in components do not always have to be point-to-point communication with the core system (REST or messaging can be
used instead). Each plug-in can be a standalone service (or even microservice) - this topology is still only a single
architecture quantum due to monolithic core system.

Plug-in Registry - the core system needs to know about which plug-in modules are available and gow to get them. The
registry contains information about each plug-in (name, data, contract, remote access protocol). The registry can be as
simple as an internal map structure owned by the core system, or as complex as a registry and discovery tool (like
ZooKeeper or Consul).

Examples of usages: Eclipse IDE, JIRA, Jenkins, Internet web browsers, ...

Problems that require different configurations for each location or client match extremely well with this architecture
style. Another example is a product that places a strong emphasis on user customization and feature extensibility.

## Chapter 13: Service-Based Architecture Style

A hybrid of the microservices, one of the most pragmatic architecture styles (flexible, simpler and cheaper than
microservices/even-driven services).

Topology: a distributed macro layered structure consisting of a separately deployed user interface, separately deployed
coarse-grained services (domain services) and a monolithic database. Because the services typically share a single
monolithic database, the number of services within an application context range between 4 and 12.

Base on scalability, fault tolerance, and throughput - multiple instances of a domain service can exist. Multiple
instances require some load-balancing.

Many variants exist within the service-based architecture:

- single monolithic user interface
- domain-based user interface
- service-based user interface

Similarly, you can break apart a single monolithic database, going as far as domain-scoped databases.

Service-based architecture uses a centrally shared database. Because of small number of services, database connections
are not usually an issue. Database changes, can be an issue. If not done properly, a table schema change can impact
every service, making database changes very costly task in terms of effort and coordination.

One way to mitigate the impact and risk of database changes is to logically partition the database and manifest the
logical partitioning through federated shared libraries. Changes to a table within a particular logical domain, impacts
only those services using that shared library.

When making changes to shared tables, lock the common entity objects and restrict change access to only the database
team. This helps control change and emphasizes the significance of changes to the common tables used by all services.

Service based architecture - one of the most pragmatic architecture styles, natural fit when doing DDD, preserves ACID
better than any other distributed architecture, good level of architectural modularity.

## Chapter 14: Event-Driven Architecture Style

A popular distributed asynchronous architecture style used to produce highly scalable and high-performance apps. It can
be used for small applications as well as large, complex ones. Made up of decoupled event processing components that
asynchronously receive and process events. It can be used as a standalone style or embedded within other architecture
style (e.g. event-driven microservices architecture).

2 primary topologies:

- the mediator topology - used when you require control over the workflow of an event process
    - an event mediator - manages and controls the workflow for initiating events that require the coordination of
      multiple event processors, usually there are multiple mediators (associated with a particular domain)
    - if an error occurs (no acknowledgement from on eof event processors), the mediator can take corrective action to
      fix the problem
    - the mediator controls the workflow, it can maintain the event state and manage errors
    - operates on commands (send-email, fulfill-order), rather than on events (email-sent, order-fulfilled)
    - cons: not as highly decoupled as the broker topology, lower scalability, hard to model complex workflows
- the broker topology - used when you require a high level of responsiveness
    - no central event mediator
    - message flow is distributed across the event processor components in a chain-like broadcasting fashion
    - a good practice: for each event processor advertise what it did to the rest of the system, regardless of whether
      any other event processor cares about what that action was
    - operates on events (email-sent, order-fulfilled), rather than on commands (send-email, fulfill-order)
    - cons: challenging error handling - no central monitoring/controlling, not possible to restart a business
      transaction (because actions are taken asynchronously)

ERROR HANDLING: the workflow event pattern - leverages delegation, containment, and repair through the use of a workflow
delegate. On error, the event consumer immediately delegates the error to the workflow processor and moves on. The
workflow processor tries to figure out what is wrong with the message (rules, machine learning, ...), once the message
is repaired it can be sent back to the event processor. In case a very problematic error a human agent can determine
what is wrong with the message and then re-submit.

Data loss (lost messages) - a primary concern when dealing with asynchronous communication. Typical data-loss scenarios:

- the message never makes it to the queue or the broker goes does before the event processor can can retrieve the
  message
    - solution: leverage persistent message queues (guaranteed delivery), message persisted in the broker's database (
      not only in the memory)
- event processor de-queues message and crashes before it can process the message
    - solution: _client acknowledge mode_ - message is not deleted from the broker immediately, but waits for
      acknowledgement
- event processor is unable to persist the message in the database
    - solution: leverage ACID transactions

Broadcast - the capability to broadcast events without knowledge of who is receiving the message and what they do with
it. Broadcasting is perhaps the highest level of decoupling between event processors.

In event-driven architecture, synchronous communication is accomplished through **request-reply** messaging. Each event
channel within request-reply messaging has 2 queues (request + reply queue). 2 primary techniques for implementing
request-reply messaging:

1. [PREFERRED] Correlation ID - a field in the reply message usually set to the request message ID.
2. Temporary queue - dedicated for the specific request, created when the request is made, and deleted when the request
   ends. Does not require Correlation ID. Large message volumes can significantly slow down the message broker and
   impact performance and responsiveness.

- Request-Based - for well-structured, data-driven requests (e.g. retrieving customer profile data).
- Event-Based - for flexible, action-based events that require high level of responsiveness and scale, with complex and
  dynamic processing.

## Chapter 15: Space-Driven Architecture Style

In any high-volume application with a large concurrent load, the database will become a bottleneck, regardless of used
caching technologies.

The space-based architecture style is specifically designed to address problems involving high scalability, elasticity,
and high concurrency issues.

_Tuple space_ - the technique of using multiple parallel processors communicating through shared memory.

High scalability, elasticity, and performance are achieved by removing the central database and leveraging replicated
in-memory data grids. Application data is kept in memory and replicated among all active processing units.

Several architecture components that make up a space-based architecture:

- processing unit: containing the application code
    - single or multiple processing units
    - contains in-memory data grid and replication engine usually implemented using: Hazelcast, Apache Ignite, Oracle
      Coherence
- virtualized middleware: used to manage and coordinate the processing units
    - handles the infrastructure concerns (data sync, request handling)
    - made of:
        - messaging grid - manages input request and session state, determines which active processing components are
          available to receive the requests and forwards to one of those processing units (usually implemented using HA
          Proxy and Nginx)
        - data grid - implemented within the processing units as a replicated cache
        - processing grid - (optional component) manages orchestrated request processing when there are multiple
          processing units involved in a single business request
        - deployment manager - monitors response times and user loads, starts up new processing units when load
          increases, and shuts down when the load decreases
- data pumps: used to synchronously send updated data to the database
    - is a way of sending data to another processor which then updates data in a database
    - always asynchronous, provide eventual consistency
    - when a processing unit receives a request and updates its cache, that processing unit becomes the owner of teh
      update and is responsible for sending that update through the data pump so that the database can be updated
      eventually
    - implemented using messaging; messages usually contain the new data values (diff)
- data writers: used to perform the updates from the data pumps
    - accept messages from a data pump and updates the database with the information contained in the message
- data readers: used to read database data and deliver it to processing units upon startup
    - responsible for reading data from the database and sending it to the processing units via reverse data pump
    - invoked in one of 3 situations:
        - a crash of all processing unit instances of the same named cache
        - a redeployment of all processing units within the same named cache
        - retrieving archive data not contained in the replicated cache

Data collision - occurs when data is updated in one cache instance A, and during replication to another cache instance
B, the same data is updated by that cache B.The local update to B will be overridden by the old data from cache A, cache
A will be overridden by cache B. Data Collision Rate factors: latency, number of instances, cache size.

_Distributed cache_ - better data consistency. _Replicated cache_ - better performance and fault tolerance.

Example usages of space-based architecture: well suited for applications that experience high spikes in user or request
volume and apps that have throughput excess of 10k concurrent users - online concert ticketing systems, online auction
systems.

## Chapter 16: Orchestration-Driven Service-Oriented Architecture

This type appeared in the late 1990s when companies were becoming enterprises and architects were forced to reuse as
much as possible because of expensive software licenses (no open source alternatives).

Reuse - the dominant philosophy in this architecture.

- Business Services - sit at the top of this architecture and provide the entry point. No code, just input, output and
  schema information.
- Enterprise Services - fine-grained, shared implementations - atomic behaviors around particular business domain -
  CreateCustomer, CalculateQuote, ... - collection of reusable assets - unfortunately, the dynamic nature of reality
  defies these attempts.
- Application Services - not all services in the architecture require the same level of granularity, these are one-off,
  single-implementation services, for example an application a company doesn't want to take the time to make a reusable
  service.
- Infrastructure Services - supply the operational concerns - monitoring, logging, auth.
- Orchestration Engine - the heart of this architecture, defines the relationship between the business and enterprise
  services, how they map together, and where transaction boundaries lie. It also acts as an integration hub, allowing
  architects to integrate custom code with package and legacy software systems.

This architecture in practice was mostly a disaster.

When a team builds a system primarily around reuse, they also incur a huge amount of coupling between components. Each
change had a potential huge ripple effect. That in turn led to the need for coordinated deployments, holistic testing
and other drags on engineering efficiency.

This architecture manages to find the disadvantages of both monolithic and distributed architectures!

## Chapter 17: Microservices Architecture

There is no secret group of architects who decide what the next big movement will be. Rather, it turns out that many
architects end up making common decisions.

Microservices differ in this regard - it was popularized by a famous blog entry by Martin Fowled and James Lewis.

Microservices Architecture is heavily inspired by the ideas in DDD - bounded context, decidedly inspired microservices.
Within a bounded context, the internal parts (code, data schemas) are coupled together to produce work, but they are
never coupled to anything outside the bounded context.

Each service is expected to include all necessary parts to operate independently.

Performance is often the negative side effect of the distributed nature of microservices. Network calls take much longer
than method calls. It is advised to avoid transactions across service boundaries, making determining the granularity the
key to success in this architecture.

It is hard to define the right granularity for services in microservices. If there are too many services, a lot of
communication will be required to perform work. The purpose of service boundaries is to capture a domain or workflow.

Guidelines to find the appropriate boundaries:

- purpose - a domain, one significant behaviour on behalf of the overall application
- transactions - often the entities that need to cooperate in a transaction show a good service boundary
- choreography - if excellent domain isolation require extensive communication, you may consider merging services back
  into larger service to avoid communication overhead

Microservices Architecture tries to avoid all kinds of coupling - including shared schemas and databases used as
integration points.

Once a team has built several microservices, they realize that each has common elements that benefit from similarity.
The shared sidecar can be either owned by individual teams or a shared infrastructure team. Once teams know that each
service includes a common sidecar, they can build a _service mesh_ - allowing unified control across the infrastructure
concerns like logging and monitoring.

2 styles of user interfaces:

- monolithic user interface - a single UI that calls through the API layer to satisfy user request
- micro-frontends - each service emits the UI for that service, which the frontend coordinates with the other emitted UI
  components

Microservices architectures typically utilize _protocol-aware heterogeneous interoperability_:

- protocol-aware - each service should know how to call other services
- heterogeneous - each service may be written in a different technology stack, heterogeneous means that microservices
  fully support polyglot environments
- interoperability - describes services calling one another, while architects in microservices try to discourage
  transactional calls, services commonly call other services via the network to collaborate

For asynchronous communication, architects often use events and messages (internally utilizing an event-driven
architecture).

The broker and mediator patterns manifest as choreography and orchestration:

- choreography - no central coordinator exists in this architecture
- orchestration - coordinating calls across several services

Building transactions across service boundaries violates the core decoupling principle of the microservices
architecture. DON'T.

> Don't do transactions in microservices - fix granularity instead.

Exceptions always exist (e.g. 2 different services need vastly different architecture characteristics -> different
boundaries), in such situations - patterns exist to handle transaction orchestration (with serious trade-offs).

SAGA - the mediator calls each part of the transaction, records success/failure, and coordinates results. In case of an
error, the mediator must ensure that no part of the transaction succeeds if one part fails (e.g. send a request to undo

- usually very complex). Typically, implemented by having each request in a `pending` state.

> A few transactions across services is sometimes necessary; if it is the dominant feature of the architecture, mistakes
> were made!

Performance is often an issue in microservices - many network calls, which has high performance overhead. Many patterns
exist to increase performance (data caching and replication).

However, one of the most scalable systems yet have utilized this style to great success, thanks to scalability,
elasticity and evolutionary.

Additional references on microservices:

- Building Microservices
- Microservices vs. Service-Oriented Architecture
- Microservices AntiPatterns

## Chapter 18: Choosing the Appropriate Architecture Style

Choosing an architecture style represents the culmination of analysis and thought about trade-offs for architecture
characteristics, domain considerations, strategic goals, and a host of other things.

Preferred architecture shift over time, driven by:

- observations from the past - rely on experience and observations
- changes in the ecosystem - constant change is a reliable feature of the software development
- new capabilities - architects must keep an eye open to not only new tools but new paradigms
- acceleration - new tools create new engineering practices, which lead to new design and capabilities
- domain changes - the business continues to evolve
- technology changes - as technology evolves, organizations have to keep up with at least some of these changes
- external factors - external factors may force a migration to another option

When choosing an architectural style, an architect must take into account all the various factors that contribute to the
structure for the domain design. Architects should go into the decision comfortable with the following things:

- the domain - good general understanding of the major aspects of the domain
- architecture characteristics that impact structure - architect must discover and elucidate the architecture
  characteristics
- data architecture - architects and DBAs must collaborate on database, schema and other DB-related concerns
- organizational factors - external factors may influence design - cost, company's plans, ...
- knowledge of process, trams, and operational concerns - software development process, interaction with operations and
  the QA influence a design
- domain/architecture isomorphism - some problem domains match the topology of the architecture

Several determinations:

- monolith vs distributed
- where should data live
- synchronous or asynchronous communication between services

General tip:

> Use synchronous by default, asynchronous when necessary

## Chapter 19: Architecture Decisions

Making architecture decisions involves gathering enough relevant information, justifying the decision, documenting the
decision, and effectively communicating the decision to the right stakeholders.

Decision anti-patterns:

- covering your assets - occurs when an architect avoids/defers making architecture decisions out of fear of making the
  wrong choice, 2 ways to overcome:
    - wait until you have enough information to justify and validate your decision, but waiting too long holds up
      development teams
    - continually collaborate with development teams to ensure that the decision can be implemented as expected, quickly
      respond to change
- groundhog day - when people don't know why a decision was made, so it keeps getting discussed over and over, architect
  failed to provide a justification for the decision (technical and business justifications)
- email-driven architecture - where people lose, forget, or don't even know an architecture decision has been made and
  therefore cannot implement that decision, notify impacted people directly in order to avoid this anti-pattern

Architecturally significant decisions are those decisions that affect [OR]:

- the structure - impacts the patterns/styles of architecture being used
- nonfunctional characteristics - architecture characteristics (performance, scalability, ...)
- dependencies - coupling points between components/services within the system
- interfaces - how services and components are accessed and orchestrated
- construction techniques - platforms, frameworks, tools, processes

Architecture Decision Records - ADRs - short text file describing a specific architecture decision. 5 main sections:

- title - numbered sequentially and contains short phrase describing the architecture decisions
- status - one of: proposed (must be approved-by a higher-level decision maker), accepted (approved & ready for
  implementation), suspended (decision changed and superseded by another ADR)
- context - what situation forces me to make this decision, this section also provides a way to document the
  architecture (clear & concise)
- decision - the architecture decision, along with full justification for the decision, advised to use following voice:
  we will do, we will use, ... -- this section allows an architect to place more emphasis on _why_ rather than _how_.
  Understanding why a decision was made is far more important than understanding how something works.
- consequences - the overall impact of an architecture decision, this section forces the architect to think about
  whether those impacts outweigh the benefits of the decision. Another good use is to document the trade-offs' analysis.
- [additional] compliance - how the architecture decision will be measured and governed from a compliance perspective
- [additional] notes - various metadata -- author, approval date, approved by, superseded date, last modified date, ...

Authors' recommendation -- store ADRs in a wiki, rather than on Git.

ADRs can be used as an effective means to document a software architecture.

## Chapter 20: Analyzing Architecture Risk

Every architecture has risk associated with it -- risk involving availability, scalability, data integrity, ... -- by
identifying risks, the architect can address deficiencies and take corrective actions.

The Architecture Risk Matrix - 2D array -- the overall impact and the likelihood, each dimension has 3 ratings (low,
medium, high). When leveraging the risk matrix to qualify the risk, consider the impact dimension first and the
likelihood dimension second.

Risk Assessment - a summarized report of the overall risk of an architecture (the risk matrix can be used to build it).

Risk Storming - a collaborative exercise used to determine architectural risk within a specific dimension (area of risk)
-- unproven technology, performance, scalability, availability, data loss, single points of failure, security. Risk
storming is broken down into 3 primary activities:

1. Identification - each participant individually identifies areas of risk within the architecture, should involve
   analyzing only one particular dimension
2. Consensus - highly collaborative activity with the goal of gaining consensus among all participants
3. Mitigation - involves changes or enhancements to certain areas of the architecture

Risk storming can be used for other aspects of software development -- for example story grooming -- story risk, the
likelihood that the story will not be completed.

## Chapter 21: Diagramming and Presenting Architecture

Effective communication becomes critical to an architect's success. No matter how brilliant an architect's ideas are, if
they can't convince managers to fund them and developers to build them.

Diagramming and presenting are 2 critical soft skills for architects.

Irrational Artifact Attachment - is the proportional relationship between a person's attachment to some artifact and
how long it took to produce.If you spend a lot of time on something , you may have an irrational attachment to that
artifact (proportional to the time invested). Use Agile approach in order to avoid this anti-pattern - create
just-in-time artifacts, use simple tools to create diagrams.

Baseline features of a diagram tool:

- layers - used to link a group of items together logically to enable hiding/showing individual layers. An architect can
  build a diagram where they can hide overwhelming details or to incrementally build pictures for presentations
- stencils/templates - allow to build up a library of common virtual components (basic shapes with a special meaning,
  e.g. microservice stencil)
- magnets - assistance in drawing lines

Diagram Guidelines:

- Titles - all elements of the diagram should have title or are well known to the audience
- Lines - should be thick enough to be seen, if lines indicate information flow use arrows
    - solid lines = synchronous communication
    - dotted lines = asynchronous communication
- Shapes - each architect tends to make their own standard set of shapes, hint: use 3D boxes to indicate deployable
  artifacts and rectangles to indicate containership
- Labels - label each item in a diagram, especially if there is a chance of ambiguity for the readers
- Color - use colors when it helps to distinguish one artifact from the other
- Keys - if shapes are ambiguous, include a key on the diagram clearly indicating what each shape represents

Book recommendation: Presentation Patterns

When preparing a presentation - use different type of transition when changing a topic, use the same transition within a
topic.

When presenting, the presenter has 2 presentation channels: verbal and visual. By placing too much text on the slides
and then saying the same words, the presenter is overloading one information channel and starving the other.

Using animations and transitions in conjunction with incremental builds (reveal information gradually) allows the
presenter to make more compelling, entertaining presentations.

Info-decks - slide decks that are not meant to be projected but rather summarize information graphically, essentially
using a presentation tool as a desktop publishing machine. They contain all the information, are meant to be standalone,
no need for presenter.

Invisibility - a pattern where the presenter inserts a blank slide within a presentation to refocus attention solely on
the speaker (turn of one visual channel).

## Chapter 22: Making Teams Effective

A software architect is also responsible for guiding the development team through the implementation of the
architecture.

Software architect should create and communicate constraints, or the box, in which developers can implement the
architecture. Tight boundaries = frustration, loose boundaries = confusion, appropriate boundaries = effective teams.

3 basic types of architect personalities:

- a control freak:
    - controls every detailed aspect of the software development process
    - too fine-grained and too low-level decisions
    - may restrict the development team to use specific technology, library, naming convention, class design
    - steals art of programming away from the developers
- an armchair architect:
    - hasn't coded in a very long time and does not take the implementation details into account
    - creates loose boundaries, in this scenario, development teams end up taking the role of architect, doing the work
      an architect is supposed to be doing
    - in order to avoid such behaviour, an architect should be involved in the technology being used on the project
- an effective architect:
    - produces the appropriate constraints and boundaries, ensures that the team members are working well together and
      have the right level of guidance on the team
    - requires working closely and collaborating with the team, and gaining respect of the team as well

Elastic Leadership - https://www.elasticleadership.com -- knowing how much control to exert on a given development team,
factors to determine how many teams a software architect can manage at once:

- team familiarity - the better team members know each other, the less control is needed because team members start to
  become self-organizing, the newer the team members, the more control needed to help facilitate collaboration among
  team members and reduce cliques within the team
- team size - the larger the team, the more control is needed, the smaller the team, less control is needed
- overall experience - teams with more junior developers require more control and mentoring whereas teams with more
  senior developers require less control
- project complexity - highly complex projects require the architect to be more available to the team and to assist with
  issues that arise, hence more control is needed on the team
- project duration - the shorter the duration, the lass control is needed, the longer the project, the more control is
  needed

3 factors when considering the most effective team size:

- process loss - (Brook's law) the more people you add to a project, the more ime the project will take, example: unable
  to parallelize work, merge conflicts
- pluralistic ignorance - when everyone agrees to a norm because they think they are missing something obvious, rather
  than speaking up, a person chooses to follow the group (similar to "The Emperor's New Clothes" -- the king is naked),
  an architect should observe body language of all team members and ask each person what they think about the proposed
  solution
- diffusion of responsibility - as team size increases, it has a negative impact on communication

An effective architect not only helps guide the development team through the implementation of the architecture, but
also ensures that the team is healthy, happy, and working together to achieve a common goal.

Checklists work and provide an excellent vehicle for making sure everything is covered and addressed. The key to making
teams effective is knowing when to leverage checklists and when not to. Most effective checklists:

- code completion checklist - if everything in the checklist is completed, then the developer can claim they are
  actually done with the code
- unit and functional testing checklist - contains some of the more unusual and edge-case tests that software developers
  tend to forget to test
- software release checklist - releasing software is perhaps one of the most error-prone aspects of the software
  development life cycle, it helps avoid failed builds, deployments, and it significantly reduces the amount of rish
  associated with releasing software

Many items from the checklists can be automated.

> Don't worry about stating the obvious in a checklist. It's the obvious stuff that's usually skipped or missed.

## Chapter 23: Negotiation and Leadership Skills

Negotiation is one of the most important skills a software architect can have. Effective software architects understand
the politics of the organization, have strong negotiation and facilitation skills, and can overcome disagreements when
they occur to create solutions that all stakeholders agree on.

"We must have zero downtime", "I need these features yesterday", ...:

> Leverage the use of grammar and buzzwords to better understand the situation

Enter the negotiation wit as many arguments as possible:

> Gather as much information as possible _before_ entering into a negotiation

Save this negotiation tactic for last:

> When all else fails, state things in terms of cost and time

Does entire system require 99.999% availability or just some parts?:

> Leverage the "divide and conquer" rule to qualify demands or requirements

Demonstrate your point with a real-life example:

> Always remember that demonstration defeats discussion

> Avoid being too argumentative or letting things get too personal in a negotiation -- calm leadership combined with
> clear and concise reasoning will always win a negotiation

Ivory Tower architecture anti-pattern - Ivory tower architects are ones who simply dictate from on high, telling
development teams what to do without regard to their opinion or concerns. This usually leads to a loss of respect for
the architect and an eventual breakdown of the team dynamics.

> When convincing developers to adopt an architecture decision or to do a specific task, provide a justification rather
> than "dictating from on high"

By providing a reason why something needs to be done, developers will more likely agree with the request. Most of the
time, once a person hears something they disagree with, they stop listening. By stating the reason first, the architect
is sure that the justification will be heard.

> If a developer disagrees with a decision, have them arrive at the solution on their own

Win-win situation: the developer either fail trying and the architect automatically gets buy-in agreement for the
architect's decision or the developer finds a better way to address concerns.

Accidental complexity - we have made a problem hard, architects sometimes do this to prove their worth when things seem
too simple or to guarantee that they are always kept in the loop on discussions and decisions. Introducing accidental
complexity into something that is not complex is one of the best ways to become an ineffective leader as an architect.
An effective way of avoiding accidental complexity is what we call the 4C's of architecture:

- communication
- collaboration
- clarity
- conciseness

Be pragmatic, yet visionary. Visionary - Thinking about or planning the future with imagination or wisdom. Pragmatic -
Dealing with things sensibly and realistically in a way that is based on practical rather than theoretical
considerations.

Bad software architects leverage their title to get people to do what they want from them to do. Effective software
architects get people to do things by not leveraging their title as architect, but rather by leading through example,
not title. Lead by example, not by title.

To lead a team and become an effective leader, a software architect should try to become the go-to person on the team -
the person developers go to for their questions and problems. Another technique to start gaining respect as a leader and
become the go-to person on the team is to host periodic brown-bag lunches to talk about specific technique or
technology.

Too many meetings? Ask for the meeting agenda ahead of time to help quantify if you are really needed at the meeting or
not.

Meetings should be either first thing in the morning, right after lunch, or toward the end of the day, but not during
the day when most developers experience flow state.

> The most important single ingredient is the formula of success is knowing how to get along with people ~ Theodore
> Roosevelt

## Chapter 24: Developing a Career Path

An architect must continue to learn throughout their career. Technology breadth is more important to architects than
depth.

The 20-Minute Rule - devote at least 20 minutes a day to your career as an architect by learning something new or diving
deeper into a specific topic. Spend min. 20 minutes to Google some unfamiliar buzzwords.

Technology Radar: https://www.thoughtworks.com/radar

You can create your won personal technology radar. It helps to formalize thinking about technology and balance opposing
decision criteria.

Architects should choose some technologies and/or skills that are widely in demand and track that demand. But they might
also want to try some technology gambits, like open source or mobile development.

Architects can utilize social media to enhance their technical breadth. Using media like Twitter professionally,
architects should find technologists whose advice they respect. This allows to build a network on new, interesting
technologies to assess and keep up with the rapid changes in the technology world.

## Self-Assessment Questions

[Chapter 1: Introduction](#chapter-1-introduction)

1. What are the 4 dimensions that define software architecture?

Knowledge of the architecture structure, architecture characteristics, architecture decisions, and design principles.

2. What is the difference between an architecture decision and a design principle?

Decisions: what is and what is not allowed, rules for a system how it should be constructed. Design principles:
guidelines for constructing systems.

3. List the eight core expectations of a software architect.

Make architecture decisions. Continually analyze the architecture. Keep current with the latest trends. Ensure
compliance with decisions. Diverse exposure and experience. Have business domain knowledge. Posses interpersonal skills.
Understand and navigate politics.

4. What is the First Law of Software Architecture.

Everything in software architecture is a trade-off.

[Chapter 2: Architectural thinking](#chapter-2-architectural-thinking)

1. Describe the traditional approach of architecture versus development and explain why that approach no longer works.

In a traditional model the architect is disconnected from the development teams, and as such the architecture rarely
provides what it was originally set out to do. Architect defines architecture characteristics, selects architecture
patterns and styles, then these artifacts are handed off to the development teams.

Boundaries between architects and developers must be broken down. Unlike the old-school waterfall approaches to static
and rigid software architecture, the architecture of today's systems changes and evolves every iteration. A tight
collaboration is essential for the success.

2. List the three levels of knowledge in the knowledge triangle and provide an example of each.

Stuff you know: Python

Stuff you know you don't know: Deep Learning

Stuff you don't know you don't know: 🤷‍

3. Why is it more important for an architect to focus on technical breadth rather than technical depth?

Architects must make decisions that match capabilities to technical constraints, a broad understanding of a wide variety
of solutions is valuable.

4. What are some of the ways of maintaining your technical depth and remaining hands-on as an architect?

- do frequent proof-of-concepts
- whenever possible, write best production-quality code (even when doing POCs) -- POC code often remains in the
  repository and becomes the reference or guiding example
- tackle technical debt stories or architecture stories, freeing the development team up to work on the critical
  function user stories
- work on bug fixes
- create simple command-line tools and analyzers to help the development team with their day-to-day tasks
- do code reviews frequently

[Chapter 3: Modularity](#chapter-3-modularity)

1. What is meant by the term _connascence_?

Two components mare connascent if a change in one would require the other to be modified in order to maintain teh
overall correctness of the system.

Connascence allows us to go beyond the binary of "coupled" and "not coupled", serving as a tool to measure coupling and
describe how bad it is under different levels and kinds.

2. What is the difference between static and dynamic connascence?

Static connascence refers to source-code-level coupling - name (multiple entities must agree on the name), type (
multiple entities must agree on the type), meaning (multiple entities must agree on the meaning of particular values),
position (multiple entities must agree on the order of the values), algorithm (multiple entities must agree on a
particular algorithm).

Dynamic connascence analyzes calls at runtime - execution (order of execution), timing (timing of the execution of
multiple components), values (several values relate to one another), identity (several values relate to one another and
must change together).

3. What does the connascence of type mean? Is it static or dynamic connascence?

[STATIC] Multiple components must agree on the type of entity.

4. What is the strongest form of connascence?

Identity. Multiple components must reference the same entity. For example when 2 independent components must share and
update a common data source.

5. What is the weakest form of connascence?

Name. Multiple components must agree on the name.

6. Which is preferred within code base -- static or dynamic connascence?

Static. Architects have a harder time determining connascence because we lack tools to analyze runtime calls as
effectively as we can analyze the call graph.

[Chapter 4: Architecture Characteristics Defined](#chapter-4-architecture-characteristics-defined)

1. What three criteria must an attribute meet to be considered an architecture characteristic?

- specifies a non-domain design consideration
- influences some structural aspect of the domain
- is critical or important to application success

2. What is the difference between an implicit characteristic and an explicit one? Provide an example of each.

Implicit - appears in requirements, necessary for project success. Domain knowledge required to uncover such
characteristics.

Explicit - characteristic listed in the requirements.

3. Provide an example of an operational characteristic.

Availability, Continuity, Performance, Reliability, Recoverability, Scalability, ...

4. Provide an example of a structural characteristic.

Configurability, Extensibility, Maintainability, ...

5. Provide an example of a cross-cutting characteristic.

Accessibility, Authentication, Authorization, Legal, Security, Privacy, ...

6. Which architecture characteristic is more important to strive for -- availability or performance?

The ultimate answer for architectural questions: _it depends on ...

[Chapter 5: Identifying Architectural Characteristics](#chapter-5-identifying-architectural-characteristics)

1. Give a reason why it is a good practice to limit the number of characteristics an architecture should support.

Over-specifying architecture characteristics may kill the project. Example: The Vasa - a Swedish warship, it was
supposed to be magnificent, turned out to be too heavy, too complicated.

Keep the design simple.

2. True or false: most architecture characteristics come from business requirements and user stories

True.

3. If a business stakeholders states that time-to-market is the most important business concern, which architecture
   characteristic would the architecture need to support?

Agility, testability, deployability

4. What is the difference between scalability and elasticity?

Scalability - the ability to handle a large number of concurrent users without serious performance degradation.

Elasticity - the ability to handle bursts of requests.

5. You find out that your company is about to undergo several major acquisitions to significantly increase its customer
   base. Which architectural characteristics should you be worried about?

Interoperability, scalability, adaptability, extensibility.

[Chapter 6: Measuring and Governing Architecture Characteristics](#chapter-6-measuring-and-governing-architecture-characteristics)

1. Why is cyclomatic complexity such an important metric to analyze for architecture?

Overly complex code represents a code smell - it harms virtually every one of the desirable characteristics.

2. What is an architecture fitness function? How can they be used to analyze an architecture?

Any mechanism that provides an objective integrity assessment of some architecture characteristic or combination of
architecture characteristics. Many tools may be used to implement fitness functions: metrics, monitors, unit tests,
chaos engineering, ...

3. Provide an example of an architecture fitness function to measure the scalability of an architecture?

Code automatic scalability tests and compare results.

4. What is the most important criteria for an architecture characteristic to allow architects and developers to create
   fitness functions?

Architects must ensure that developers understand the purpose of the fitness function before imposing it on them.

[Chapter 7: Scope of Architecture Characteristics](#chapter-7-scope-of-architecture-characteristics)

1. What is an architectural quantum, and why is it important to architecture?

The architectural quantum is the smallest possible item that needs to be deployed in order to run an application.

3. Assume a system consisting of a single user interface with four independently deployed services, each containing its
   own separate database. Would this system have a single quantum or four quanta? Why?

4 because each service can be deployed separately.

4. Assume a system with an administration portion managing static reference data (such as the product catalog, and
   warehouse information) and a customer-facing portion managing the placement of orders. How many quanta should this
   system be and why? If you envision multiple quanta, could the admin quantum and customer-facing quantum share a
   database? If so, in which quantum would the database need to reside?

2 quantas - ordering and a warehouse management, separate databases. 
