[go back](https://github.com/pkardas/learning)

# Architecture Patterns with Python: Enabling Test-Driven Development, Domain-Driven Design, and Event-Driven Microservices

Book by Harry Percival and Bob Gregory

- [Introduction](#introduction)
- [Chapter 1: Domain Modeling](#chapter-1-domain-modeling)
- [Chapter 2: Repository Pattern](#chapter-2-repository-pattern)
- [Chapter 3: On Coupling and Abstractions](#chapter-3-on-coupling-and-abstractions)
- [Chapter 4: FlaskAPI and Service Layer](#chapter-4-flaskapi-and-service-layer)

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
