[go back](https://github.com/pkardas/learning)

# Abbreviations

- [SOLID](#solid)
- [DRY - Don't Repeat Yourself](#dry---dont-repeat-yourself)
- [KISS - Keep It Simple, Stupid](#kiss---keep-it-simple-stupid)
- [ACID](#acid)
- [BASE](#base)
- [CAP](#cap)
- [NF](#nf)

## SOLID

### SRP - Single Responsibility Principle

A class should have only one reason to change, so in order to reduce reasons for modifications - one class should have
one responsibility. It is a bad practise to create classes doing everything.

Why is it so important that class has only one reason to change? If class have more than one responsibility they become
coupled and this might lead to surprising consequences like one change breaks another functionality.

You can avoid these problems by asking a simple question before you make any changes: What is the responsibility of your
class / component / micro-service? If your answer includes the word “and”, you’re most likely breaking the single
responsibility principle.

### OCP - Open-Closed Principle

Classes, modules, functions, etc. should be open to extension but closed to modification.

Code should be extensible and adaptable to new requirements. In other words, we should be able to add new system
functionality without having to modify the existing code. We should add functionality only by writing new code.

If we want to add a new thing to the application and we have to modify the "old", existing code to achieve this, it is
quite likely that it was not written in the best way. Ideally, new behaviors are simply added.

### LSP - Liskov Substitution Principle

This rule deals with the correct use of inheritance and states that wherever we pass an object of a base class, we
should be able to pass an object of a class inheriting from that class.

Example of violation:

```python
class A:
    def foo() -> str:
        return "foo"


class B(A):
    def foo(bar: str) -> str:
        return f"foo {bar}"
```

B is not taking the same arguments, meaning A and B are not compatible. A can not be used instead of B, and B can not be
used instead of A.

### ISP - Interface Segregation Principle

Clients should not be forced to depend upon interfaces that they do not use. ISP splits interfaces that are very large
into smaller and more specific ones so that clients will only have to know about the methods that are of interest to
them.

Example of violation:

```python
class Shape:
    def area() -> float:
        raise NotImplementedError

    def volume() -> float():
        raise NotImplementedError
```

2D triangle does not have volume, hence it would need to implement interface that is not needed. In order to solve this,
there should be multiple interfaces: Shape and 3DShape.

### DIP - Dependency Inversion Principle

High-level modules, which provide complex logic, should be easily reusable and unaffected by changes in low-level
modules, which provide utility features. To achieve that, you need to introduce an abstraction that decouples the
high-level and low-level modules from each other.

> Entities must depend on abstractions, not on concretions. It states that the high-level module must not depend on the low-level module, but they should depend on abstractions.

For example password reminder should not have knowledge about database provider (low level information).

## DRY - Don't Repeat Yourself

"Every piece of knowledge must have a single, unambiguous, authoritative representation within a system". When the DRY
principle is applied successfully, a modification of any single element of a system does not require a change in other
logically unrelated elements.

## KISS - Keep It Simple, Stupid

The KISS principle states that most systems work best if they are kept simple rather than made complicated; therefore,
simplicity should be a key goal in design, and unnecessary complexity should be avoided.

## ACID

### Atomicity

Each transaction is either properly carried out or the process halts and the database reverts back to the state before
the transaction started. This ensures that all data in the database is valid.

### Consistency

A processed transaction will never endanger the structural integrity of the database. Database is always in consistent
state.

### Isolation

Transactions cannot compromise the integrity of other transactions by interacting with them while they are still in
progress.

### Durability

The data related to the completed transaction will persist even in the cases of network or power outages. If a
transaction fails, it will not impact the manipulated data.

## BASE

### Basically Available

Ensure availability of data by spreading and replicating it across the nodes of the database cluster - this is not done
immediately.

### Soft State

Due to the lack of immediate consistency, data values may change over time. The state of the system could change over
time, so even during times without input there may be changes going on due to ‘eventual consistency,’ thus the state of
the system is always ‘soft.’

### Eventually Consistent

The system will *eventually* become consistent once it stops receiving input. The data will propagate to everywhere it
should sooner or later, but the system will continue to receive input and is not checking the consistency of every
transaction before it moves onto the next one.

## CAP

In theoretical computer science, the CAP theorem states that it is impossible for a distributed data store to
simultaneously provide more than two out of the following three guarantees:

### Consistency

Every read receives the most recent write or an error. Refers to whether a system operates fully or not. Does the system
reliably follow the established rules within its programming according to those defined rules? Do all nodes within a
cluster see all the data they are supposed to? This is the same idea presented in ACID.

### Availability

Every request receives a (non-error) response, without the guarantee that it contains the most recent write. Is the
given service or system available when requested? Does each request get a response outside of failure or success?

### Partition Tolerance

Represents the fact that a given system continues to operate even under circumstances of data loss or system failure. A
single node failure should not cause the entire system to collapse.

## NF

Database normalisation is the process of structuring a database, usually a relational database, in accordance with a
series of so-called normal forms in order to reduce data redundancy and improve data integrity.

### 1NF

To satisfy 1NF, the values in each column of a table must be atomic.

### 2NF

Must be in 1NF + single column primary key (no composite keys).

### 3NF

Must be in 2NF + no transitive functional dependencies.

Transitive Functional Dependencies - when changing a non-key column, might cause any of the other non-key columns to
change. For example:

![3nf-violation](../_images/3nf-violation.png)
