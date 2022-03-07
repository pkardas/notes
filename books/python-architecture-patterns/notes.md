[go back](https://github.com/pkardas/learning)

# Architecture Patterns with Python: Enabling Test-Driven Development, Domain-Driven Design, and Event-Driven Microservices

Book by Harry Percival and Bob Gregory

- [Introduction](#introduction)
- [Chapter 1: Domain Modeling](#chapter-1-domain-modeling)
- [Chapter 2: Repository Pattern](#chapter-2-repository-pattern)
- [Chapter 3: On Coupling and Abstractions](#chapter-3-on-coupling-and-abstractions)
- [Chapter 4: FlaskAPI and Service Layer](#chapter-4-flaskapi-and-service-layer)
- [Chapter 5: TDD in High Gear and Low Gear](#chapter-5-tdd-in-high-gear-and-low-gear)
- [Chapter 6: Unit of Work Pattern](#chapter-6-unit-of-work-pattern)
- [Chapter 7: Aggregates and Consistency Boundaries](#chapter-7-aggregates-and-consistency-boundaries)
- [Chapter 8: Events and the Message Bus](#chapter-8-events-and-the-message-bus)
- [Chapter 9: Going to Town the Message Bus](#chapter-9-going-to-town-the-message-bus)
- [Chapter 10: Commands and Command Handler](#chapter-10-commands-and-command-handler)
- [Chapter 11: Event-Driven Architecture: Using Events to Integrate Microservices](#chapter-11-event-driven-architecture-using-events-to-integrate-microservices)
- [Chapter 12: Command-Query Responsibility Segregation (CQRS)](#chapter-12-command-query-responsibility-segregation-cqrs)
- [Chapter 13: Dependency Injection (and Bootstrapping)](#chapter-13-dependency-injection-and-bootstrapping)

## Introduction

Software systems tend toward chaos. When we first start building a new system, we have grand ideas that our code will be
clean and well-ordered, but iver time we find that it gathers cruft and edge cases and ends up a confusing morass of
manager classes and util modules.

Fortunately, the techniques to avoid creating a big ball of mud aren't complex.

Encapsulation covers two closely related ideas: simplifying behavior and hiding data. We encapsulate behavior by
identifying a task that needs to be done in our code and giving that task a well-defined object or function. We call
that object ro function an abstraction.

Encapsulating behavior by using abstractions is a powerful tool for making code more expressive, more testable, and
easier to maintain.

Encapsulation and abstraction help us by hiding details and protecting the consistency of our data, but wee= need to pay
attention to the interactions between our objects and functions. When one function, module or object uses another, we
say that the one depends on the other. Those dependencies form a kind of network or graph. For example: Presentation
Layer -> Business Logic -> Database Layer.

Layered architecture is the most common pattern for building business software.

The Dependency Inversion Principle:

1. High-level modules should not depend on low-level modules. Both should depend on abstractions.
2. Abstractions should not depend on details. Instead, details should depend on abstractions.

High-level modules are the code that your organization really cares about. The high-level modules of a software system
are the functions, classes, and packages that deal with our real-world concepts. By contract, low-level modules are the
code that your organization doesn't care about. If payroll runs on time, your business is unlikely to care whether that
is a coron job or a transient function running on Kubernetes.

> All problems in computer science can be solved by adding another level of indirection ~ David Wheeler.

We don't want business logic changes to slow down because they arte closely coupled to low-level infrastructure details.
Adding an abstraction between them allows the two to change independently of each other.

## Chapter 1: Domain Modeling

The _domain_ is a fancy word of saying _the problem you are trying to solve_. A _model_ is a map of a process or
phenomenon that captures a useful property.

In a nutshell, DDD says that the most important thing about software is that it provides a useful model of a problem. If
we get that model right, our software delivers value and makes new things possible.

When we hear our business stakeholders using unfamiliar words, or using terms in a specific way, we should listen to
understand the deeper meaning and encode their hard-won experience into our software.

Choose memorable identifiers for our objects so that the examples are easier to talk about.

Whenever we have a business concept that has data but has no identity, we often choose to represent it using the Value
Object pattern. A value object is any domain object that is uniquely identified as by the data it holds, we usually make
them immutable. Named tuples and frozen data classes are a great tool for this.

Entities, unlike values, have identity equality. We can change their values, and they are still recognizably the same
thing. Batches, in our example, are entities. We can allocate lines to a batch, or change the date that we expect it to
arrive, and it will still be the same entity.

We usually make this explicit in code by implementing equality operators on entities.

For value objects, the hash should be based on all attributes, and we should ensure that the objects are immutable. For
entities, the simplest option is to say that the hash is None, meaning that the object is not hashable and cannot, for
example be used in a set. If for some reason you decide to use set or dict operations with entities, the hash should be
based on the attributes, that defines the entity's unique identity over time.

Exceptions can express domain concepts too.

## Chapter 2: Repository Pattern

Repository Pattern - a simplifying abstraction over data storage, allowing us to decouple our model layer from the data
layer. This simplifying abstraction makes our system more testable by hiding the complexities of the database. It hides
the boring details of data access by pretending that all of our data is in memory. This pattern is very common in DDD.

Layered architecture is a common approach to structuring a system that has a UI, some logic, and a database.

Onion architecture - model being inside, and dependencies flowing inward to it.

ORM gives us persistence ignorance - fancy model doesn't need to know anything about how data is loaded or persisted.
Using and ORM is already an example of the DIP. Instead of depending on hardcoded SQL, we depend on abstraction - the
ORM.

The simplest repository has just two methods:

- add - to put a new item in the repository
- get - to return a previously added item.

One of the biggest benefits of the Repository pattern is the possibility to build a fake repository.

> Building fakes for your abstractions is an excellent way to get design feedback: if it's hard to fake, the abstraction
> is probably too complicated.

Simple CRUD wrapper around a database, don't need a domain model or a repository.

Repository Pattern Recap:

- Apply dependency inversion to your ORM - Domain model should be free of infrastructure concerns, so your ORM should
  import your model, and not the other way around.
- The Repository pattern is a simple abstraction around permanent storage - The repository gives you the illusion of a
  collection of in-memory objects. It makes it easy to create a FakeRepository for testing and to swap fundamental
  details of your infrastructure without disrupting your code application.

## Chapter 3: On Coupling and Abstractions

When we are unable to change component A for fear of breaking component B, we say that the components have become
coupled. Globally, coupling increases the risk and the cost of changing our code, sometimes to the point where we feel
unable to make any changes at all.

We can reduce the degree of coupling within a system by abstracting away the details.

According to authors it is better to use fake resources instead of mocks:

- Mocks are used to verify how something gets used, they have methods like `assert_called_once_with`. They are
  associated with London-school TDD.
- Fakes are working implementations of the thing they are replacing, but they are designed for use only in tests. They
  wouldn't work in real life. You can use them to make assertions about the end state of a system rather than the
  behaviours along the way, so they are associated with classic-style TDD.

TDD is a design practice first and a testing practice second. The tests act as a record of our design choices and serve
to explain the system to use when we return to the code after a long absence.

Tests that use too many mocks get overwhelmed with setup code that hides the story we care about.

Links:

- [YOW! Conference 2017 - Steve Freeman - Test Driven Development: That’s Not What We Meant](https://www.youtube.com/watch?v=B48Exq57Zg8)
- [Edwin Jung - Mocking and Patching Pitfalls](https://www.youtube.com/watch?v=Ldlz4V-UCFw)

## Chapter 4: FlaskAPI and Service Layer

Service Layer - extract logic from the endpoint, because it might be doing too much - validating input, handling errors,
committing.

Our high-level module, the service layer, depends on the repository abstraction. And the details of the implementation
for our specific choice of persistent storage also depend on the same abstraction.

The responsibilities of the ~~Flask~~ FastAPI app are just standard web stuff - per-request session management, parsing
information out of POST parameters, response status codes and JSON. All the orchestration logic is in the use
case/service layer, and the domain logic stays in the domain.

Application service - its job is to handle requests from the outside world and to orchestrate an operation. Drives the
application by following a bunch of simple steps:

- Get some data from the database
- Update the domain model
- Persist any changes

This is the kind of boring work that has to happen for every operation in your system, and keeping it separate from
business logic helps to keep things tidy.

Domain service - this is the name for a piece of logic that belongs in the domain model but doesn't sit naturally inside
a stateful entity or value object.

## Chapter 5: TDD in High Gear and Low Gear

Once you implement domain modeling and the service layer, you really actually can get to a stage where unit tests
outnumber integration and end-to-end tests by an order of magnitude.

Tests are supposed to help us change our system fearlessly, but often we see teams writing too many tests against their
domain model. This causes problems when they come to change their codebase and find that they need to update tens or
even hundreds of unit tests.

The service layer forms an API for our system that we can drive in multiple ways. Testing against this API reduces the
amount of code that we need to change when we refactor our domain model.If we restrict ourselves to testing only against
the service layer, we will not have any tests that directly interact with "private" methods or attributes on our model
objects, which leaves us freer to refactor them.

Most of the time, when we are adding a new feature or fixing a bug, we don't need to make extensive changes to the
domain mode. IN these cases, we prefer to write tests against service because of the lower coupling and higher coverage.

WHen starting a new project or when hitting a particularly gnarly problem, we will drop back down to writing tests
against the domain model, so we get better feedback and executable documentation of our intent.

Metaphor of shifting gears - when starting a journey, the bicycle needs to be in a low hear, so it can overcome inertia.
Once we are off and running, we can go faster and more efficiently by changing into a high gear. But if we suddenly
encounter a steep hill or are forced to slow down by a hazard, we again drop to a low gear until we can pick up speed
again.

Rules of Thumb for Different Types fo Test:

1. Aim for one end-to-end test per feature - the objective is to demonstrate that the feature works, and that all the
   moving parts are glued together.
2. Write the bulk of your tests against the service layer - these end-to-end tests offer a good trade-off between
   coverage, runtime, and efficiency.
3. Maintain a small core of tests written against your domain model - these tests have highly focused coverage and are
   more brittle, but they have the highest feedback. Don't be afraid to delete these tests if the functionality is later
   covered by tests at the service layer.
4. Error handling counts as a feature - ideally, your application will be structured such that all errors bubble up to
   your entrypoints are handled in the same way. This means you need to test ony the happy path for each feature, and to
   reserve one end-to-end test for all unhappy paths.

Express your service layer in terms of primitives rather than domain objects.

## Chapter 6: Unit of Work Pattern

If the Repository pattern is our abstraction over persistent storage, the Unit of Work pattern is our abstraction over
the idea of atomic operations. It will allow us to decouple our service layer from the data layer.

Unit of Work acts as a single entrypoint to our persistent storage, and it keeps track of what objects were loaded and
of the latest state.

Unit of Work and Repository classes are collaborators.

> Don't mock what you don't own

Rule of thumb that forces us to build these simple abstractions over messy subsystems. This encourages us to think
carefully about or designs.

It is better to require explicit commit, so we can choose when to flush state. The default behaviour is to not change
anything, this makes software safe by default. There is one code path that leads to changes in the system: total success
and an explicit commit. Any other code path, any exception, any early exit from the UoW's scope leads to safe state.

You should always feel free to throw away tests if you think they are not going to add value longer term.

SQLAlchemy already uses a Unit Of Work in the shape of Session object (track changes to the entity, and when the session
is flushed, all your changes are persisted together). Then, why bother? The Session API is very rich, Unit Of Work can
simplify the session to its essential core: start, commit or throw away. Besides, our Unit Of Work can access Repository
object.

Unit of Work Pattern Recap:

- _The Unit of Work Pattern is an abstraction around data integrity_ - It helps to enforce the consistency of our domain
  model, and improves performance, by letting us perform a single flush operation at the end of an operation.
- _It works closely with the Repository Pattern and Service Layer patterns_ - The Unit of Work pattern completes our
  abstractions over data access by representing atomic updates. Each of our service-layer use cases runs in a single
  unit of work that succeeds of rails as a block.
- _This is a lovely case for a context manager_ - Context managers are an idiomatic way of defining scope in Python. We
  can use a context manager to automatically roll back our work at the end of a request, which means the system is safe
  by default.
- _SQLAlchemy already implements this pattern_ - We introduce an even simpler abstraction over the SQLAlchemy Session
  object in order to "narrow" the interface between the ORM and our code. This helps keep us loosely coupled.

## Chapter 7: Aggregates and Consistency Boundaries

Constraint is a rule that restricts the possible states of our model can get into, while an invariant is defined a
little more precisely as a condition that is always true.

The Aggregate pattern - a design pattern from the DDD community that helps us to solve concurrency issues. An aggregate
is just a domain object that contains other domain objects and lets us treat the whole collection as a single unit.

> An aggregate is a cluster of associated objects that we treat as a unit for the purpose of data changes.

We have to choose right granularity for our aggregate. Candidates: Shipment, Cart, Stock, Product.

Bounded contexts were invented as a reaction against attempts to capture entire businesses into a single model.
Attributes needed in one context are irrelevant in another. Concepts with the same name can have entirely different
meanings in different contexts. It is better to have several models, draw boundaries around each context, and handle the
translation between different contexts explicitly.

This concept translates very well to the world of microservices, where each microservice is free to have its own concept
of "customer" and its own rules for translating that to and from other microservices it integrates with.

Aggregates should be the only way to get to out model.

The Aggregate pattern is designed to help manage some technical constraints around consistency and performance.

Version numbers are just one way to implement optimistic* locking. Optimistic - our default assumption is that
everything will be fine when two users want to make changes to the database. We think it will be unlikely that they will
conflict each other. We let them go ahead and just make sure we have a way to notice if there is a problem.

Pessimistic - works under the assumption that two users are to cause conflicts, and we want to prevent conflicts in all
cases, so we lock everything just to be safe. In our example, that would mean locking the whole `batches` table or using
`SELECT FOR UPDATE`. With pessimistic locking, you don't need to think about handling failures because the database will
prevent them.

The usual way to handle a failure is to retry the operation from the beginning.

Aggregates and Consistency Boundaries Recap:

- _Aggregates are your entrypoints into the domain model_ - By restricting the number of ways that things can be
  changed, we make the system easier to reason about.
- _Aggregates are in charge of a consistency boundaries_ - An aggregate's job is to be able to manage our business rules
  about invariants as they apply to a group of related objects. It is the aggregate's job to check that the objects
  within its remit are consistent with each other and with our rules, and to reject changes that would break the rules.
- Aggregates and concurrency issues go together - When thinking about implementing these consistency checks, we end up
  thinking about transactions and locks. Choosing the right aggregate is about performance as well as conceptual
  organization fo your domain.

## Chapter 8: Events and the Message Bus

Reporting, permissions and workflows touching zillions of objects make a mess of our codebase.

> Rule of thumb: if you can't describe what your function does without using words like "then" or "and", you might be
> violating the SRP.

A message bus gives us a nice way to separate responsibilities when we have to take multiple actions in response to a
request.

Domain Events and the Message Bus Recap:

- _Events can help with the single responsibility principle_ - Code gets tangled up when we mix multiple concerns in one
  place. Events can help us to keep things tidy by separating primary use cases from secondary ones. We also use events
  for communicating between aggregates so that we don't need to run long-running transactions that lock against multiple
  tables.
- _A message bus routes messages to handlers_ - You can think of a message bus as a dict that maps from events to their
  consumers. It doesn't "know" anything bout the meaning of events; it is just a piece of dumb infrastructure for
  getting messages around the system.
- _Option 1: Service layer raises events and passes them to message bus_ - The simplest way to start using events is
  your system is to raise them from handlers by calling `bus.handle(event)` after you commit your unit of work.
- _Option 2: Domain model raises events, service layer passes them to message bus_ - The logic about when to raise an
  event really should live with the model, so we can improve our system's design and testability by raising events from
  the domain model. It is easy for our handlers to collect events off the model objects after commit and pass them to
  the bus.
- _Option 3: UoW collects events from aggregates and passes the to message bus_ - Adding `bus.handle(aggregate.events)`
  to every handler is annoying, so we can tidy up by making our unit of work responsible for raising events that were
  raised by loaded objects. This is the most complex design and might rely on ORM magic, but it is clean and easy to use
  once set up.

## Chapter 9: Going to Town the Message Bus

If we rethink our API calls as capturing events, the service-layer functions can be event handlers too, and we no longer
need to make a distinction between internal and external event handlers.

Multiple database transactions can cause integrity issues. Something could happen that means the first transaction
completes but the second one does not.

Events are simple dataclasses that define the data structures for inputs and internal messages within our system. This
is quite powerful from a DDD standpoint, since events often translate very well into business language.

Handlers are the way we react to the events. They can call down to our model or call out to external services. We can
define multiple handlers for a single event if we want to. Handlers can also raise other events. This allows us to be
very granular about what a handler does and really stick to the SRP.

## Chapter 10: Commands and Command Handler

Commands are a type of message - instructions sent by one part of a system to another. We usually represent commands
with dumb data structures and can handle them in much the same way as events. Commands are sent by one actor to another
specific actor with the expectation that a particular thing will happen as a result. When we post a form to an API
handler, we are sending a command. We name commands with imperative mood verb phrases like "allocate stock" or "delay
shipment".

Events are broadcast by an actor to all interested listeners. We often use events to spread the knowledge about
successful commands. We name events with past-tense verb phrases like "order allocated to stock" or "shipment delayed".

How to mitigate problems caused by the lost messages? The system might be left in an inconsistent state. In our
allocation service we have already taken steps to prevent that from happening. We have carefully identified aggregates
that act as consistency boundaries, and whe have introduced a UoW that manages the atomic success or failure of an
update to an aggregate.

When a user wants to make the system do something, we represent their request as a command. That command should modify a
single aggregate and either succeed or fail in totality. Any other bookkeeping, cleanup and notification we need to do
can happen via an event. We don't require the event handlers to succeed in order for the command to be successful.

We raise events about an aggregate after we persist our state to the database. It is OK for events to fail independently
from the commands that raised them.

Tenacity is a Python library that implements common patterns for retrying.

## Chapter 11: Event-Driven Architecture: Using Events to Integrate Microservices

Often, first instinct when migrating an existing application to microservices, is to split system into _nouns_.

Style of architecture, where we create a microservice per database table and treat out HTTP APIa as CRUD interfaces to
anemic models, is the most common initial way for people to approach service-oriented design. This works fine for
systems that are very simple, but it can quickly degrade into a distributed ball of mud.

WHen two things have to be changed together, we say that they are coupled. We can never completely avoid coupling,
except by having our software not talk to any other software. What we want is to avoid inappropriate coupling.

How do we get appropriate coupling? We should think in terms of verbs, not nouns. Our domain model is about modeling a
business process. It is not a static data about a thing, it is a model of a verb.

Instead of thinking about a system for orders and a system for batches, we think about a system for allocating and
ordering.

Microservices should be consistency boundaries. That means we don't need to rely on synchronous calls. Each service
accepts commands from the outside world and raises events to record the result. Other services can listen to those
events to trigger the next steps in the workflow.

Things can fail independently, it is easier to handle degraded behavior - we can still take orders if the allocation
service is having a bad day. Secondly, we are reducing the strength of coupling between our systems. If we need to
change the order of operations or to introduce new steps in the process, we can do that locally.

Events can come from the outside, but they can also be published externally.

> Event notification is nice because it implies a low level of coupling, and is pretty simple to set up. It can become
> problematic, however, if there really is a logical flow that runs over various event notifications. It can be hard to
> see such flow as it is not explicit in any program text. This can make it hard to debug and modify.

~ Martin Fowler.

## Chapter 12: Command-Query Responsibility Segregation (CQRS)

Reads (queries) and writes (commands) are different, so they should be treated differently.

Most users are not going to buy your product, they are just viewers. We can make reads eventually consistent in order to
make them perform better.

All distributed systems are inconsistent. As soon as you have a web server and two customers, you have the potential for
stale data.No matter what we do, we are always going to find that our software systems are inconsistent with reality,
and so we will always need business process to cope with these edge cases. It is OK to trade performance for consistency
on the read side, because stale data is essentially unavoidable.

READS: Simple read, highly cacheable, can be stale.

WRITE: Complex business logic, uncacheable, must be transactionally consistent.

Post/Redirect/Get Pattern - In this technique, a web endpoint accepts an HTTP POST and responds with a redirect to see
the result. For example, we might accept a POST to /batches to create a new batch and redirect user to /batches/123 to
see their newly created batch. This approach fixes the problems that arise whe users refresh the results page in their
browser. It can lead to our users double-submitting data and thus buying two sofas when they needed only one. This
technique is a simple example of CQS. In CQS we follow one simple rule - functions should either modify state or answer
questions. We can apply the same design by returning 201 Created or 202 Accepted, with a Location header containing the
URI of our new resources.

ORM can expose us to performance problems. SELECT N+1 Problem is a common performance problem with ORMs - when
retrieving a list of objects, your ORM will often perform an initial query to get all IDs of the objects it needs, and
then issue individual queries for each object to retrieve their attributes. This is especially likely if there are any
foreign-key relationships on your objects.

Even with well-tuned indexes, a relational database uses a lot of CPU to perform joins. The fastest queries will always
be `SELECT * FROM table WHERE condition`. More than raw speed, this approach buys us scale. Read-only stores can be
horizontally scaled out.

Read model can be implemented using Redis.

As domain model becomes richer and more complex, a simplified read model become compelling.

## Chapter 13: Dependency Injection (and Bootstrapping)

Mocks tightly couple us to the implementation. By choosing to monkeypatch `email.send_mail`, we are tied to
doing `import email`, and if we ever want to do `from email import send_mail`, we will have to change all our mocks.

Declaring explicit dependencies is unnecessary, and using them would make our application code marginally more complex.
But in return we would get tests that are easier to write and manage.

> Explicit is better than implicit.

Putting all the responsibility for passing dependencies to the right handler onto the message bus feels like a violation
of the SRP. Instead, we will reach for a pattern called Composition Root (a bootstrap script), and we will do a bit of "
manual DI" (dependency inversion without a framework).

Setting up dependency injection is just one of many typical setup activities that you need to do when starting your app.
Putting this all together into a bootstrap script is often a good idea.

The bootstrap is also good as a place to provide sensible default configuration for your adapters, and as a single place
to override those adapters with fakes for your tests.
