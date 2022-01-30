[go back](https://github.com/pkardas/learning)

# Architecture Patterns with Python: Enabling Test-Driven Development, Domain-Driven Design, and Event-Driven Microservices

Book by Harry Percival and Bob Gregory

- [Introduction](#introduction)
- [Chapter 1: Domain Modeling](#chapter-1-domain-modeling)

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
