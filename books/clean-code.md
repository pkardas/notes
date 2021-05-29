[go back](https://github.com/pkardas/learning)

# Clean Code: A Handbook of Agile Software Craftsmanship
Book by Robert Cecil Martin

[TOC]

## Chapter 1: Clean Code

- ugly code is expensive
- take your time to write a good code
- bad code programmer's fault, not PO's, manager's or anyone's else
- bad code is like a building with broken windows - people see ugly building and stop caring
- code like a prose, code should look like you care
- make the language look like it was made of the problem
- code rot quickly

## Chapter 2: Meaningful names

Variable name should answer all the questions. It should tell why it exists. If a name requires a comment it does not reveal its content. Names should be pronounceable. One letter variables are hard to `grep` in the code - should be ONLY as local variables inside short methods. The length of a name should correspond to the size of its scope. Avoid encodings. 

>  Difference between a smart programmer and a professional programmer is that professional programmer understands that **clarity is a king**.

Don't be funny 😔 People tend to forget jokes, so people will forget true meaning of a variable. Choose clarity over entertainment. Do not use slang or culture-dependant names.

Pick one word per concept, eg. `get` instead of `fetch`, `retrieve`, ...

## Chapter 3: Functions

Functions are the first line of organisation in any program. Functions should be small. No more than 2-3 indents.

> Functions should do one thing. They should do it well. The should do it only.

The reason we write functions is to decompose a larger concept. A function should not mix the levels of abstractions. 

> You know you are working on clean code when each routine turns out to be pretty much what you expected.

Don't be afraid to make a name long. The more function arguments the worse - difficulties with testing.

Passing a boolean flag to a function is extremely ugly. Grouping arguments into objects seems like cheating but it is not. 

Functions should have no side effects

*Command Query Separation* - functions should either do something or answer something, but not both.

Exceptions are preferred than error codes. Suggestion to extract exception handling to separate function. 

*Don't repeat yourself* - duplication may be the root of all evil in software. Database norms formed to eliminate duplication in data, OOP concentrates the code, etc.

> Writing software is like any other kind of writing. When you write a paper or article, you get your thoughts down first, then you massage it until it **reads well**.

> The art of programming is, and always has been, the art of language design.

## Chapter 4: Comments

Comments are usually bad, they mean you failed to express yourself in code. IMO: Best comments are the ones that are explaining why things were done in a particular way. 

Don't put historical discussions or irrelevant details into the comments.

## Chapter 5: Formatting

Code formatting is important. Visual design of the code is important. Variable should be declared "in well-known for everybody place". Functions should show natural flow -> top-down. 

Horizontal formatting? Python got you covered :D

Another matter is alignment, eg. of test cases in parametrised tests. However variables declarations ins an overkill.

However, a team should agree upon a single formatting style.

## Chapter 6: Objects and Data Structures

Hiding implementation is about abstractions. 

The Law of Demeter - a module should not know about the innards of the objects it manipulates. Class *C* has a method *f*, method *f* should call the methods of: *C*, object created by *f*, object passed as an argument to *f* or object held in an instance variable of *C*.

Train wreck: `ctxt.getOptions().getScratchDir().getAbsolutePath()` - a bunch of couples train cars. Does it violate The Law of Demeter? `ctxt` contains options, which contain a scratch directory, which has absolute path - a lot of knowledge.However in this case this law does nto apply because these are data structures with no behaviour. It would be good to hide the structure of `ctxt`, eg.: `ctxt.getScratchDirectoryOption().getAbsolutePath()`.

Data Transfer Objects - a class with public variables and no functions, eg. for communicating with the database.

Objects - expose behaviour and hide data, data structures - expose data and have no significant behaviour.

## Chapter 7: Error Handling

Error handling is important, but if it obscures logic, it is wrong. Exceptions are preferred over return codes - return codes can clutter the caller with unnecessary code.

`try` blocks are like transactions, `catch` has to leave the program into a consistent state.

Error messages need to be informative - mention the operation that failed and the type of failure.

It might be a good idea to wrap library's error with your own exceptions - this makes library easily replaceable. 

## Chapter 8: Boundaries

How to keep boundaries of our system clean - eg. when using external libraries:

- when working with collections, wrap them with object and provide only required functionalities.
- write learning tests - write tests to explore and understand API
- our code shouldn't know too many details about 3rd-party library
- use ADAPTER interface - converted from our perfect interface to the provided interface

## Chapter 9: Unit Tests

The Three Laws of TDD:

- You may not write production code until you have written a failing unit test
- You may not write more of unit code than is sufficient to fail, and not compiling is failing
- You may not write more production code than is sufficient to pass the currently failing test

Test code is just as important as production code. It is not second-class citizen. It must be  kept as clean as production code.

The Build-Operate-Check pattern - each test is split into three parts:

1. build up the test data
2. operate on test data
3. check that the operation yielded the expected results

Test code must be: simple, succinct, expressive, however it doesn't need to be as efficient as production code.

One test should test a single concept.

Clean tests follow 5 fules - FIRST:

- F - Fast - tests should be fast, they should run quickly, if they don't you won't  want to run them frequently.
- I - Independent - Tests should not depend on each other, one test should not set up conditions for the next test
- R - Repeatable - Tests should be repeatable in any environment (office, home, train without network), if they are not you will have an excuse for why they fail
- S - Self-Validating - Tests should not have a boolean output, they should either fail or pass
- T - Timely - Tests need to be written in a timely fashion, should be written just before the production code

## Chapter 10: Classes

Classes should be small. The second rule is that they should be smaller than that. Naming is most probably the best way of determining class size. If we cannot derive a concise name for a class, then it is likely too large. 

The Single Responsibility Principle - a class or module should have one, and only one reason to change.

Cohesion - classes should have a small number of instance variables. Each of class' methods should manipulate one or more of those variables. 

Open-Closed Principle - class should be open for extensions but closed for modifications.

Dependency Inversion Principle - our classes should depend upon abstractions, not on concrete details.

