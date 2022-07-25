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

Nothing remain static. WHat we need is _evolutionary architecture_ - mutate the solution, evolve new solutions
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
