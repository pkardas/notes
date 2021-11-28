[go back](https://github.com/pkardas/learning)

# Clean Code: A Handbook of Agile Software Craftsmanship

Book by Robert Cecil Martin

- [Chapter 1: Clean Code](#chapter-1-clean-code)
- [Chapter 2: Meaningful names](#chapter-2-meaningful-names)
- [Chapter 3: Functions](#chapter-3-functions)
- [Chapter 4: Comments](#chapter-4-comments)
- [Chapter 5: Formatting](#chapter-5-formatting)
- [Chapter 6: Objects and Data Structures](#chapter-6-objects-and-data-structures)
- [Chapter 7: Error Handling](#chapter-7-error-handling)
- [Chapter 8: Boundaries](#chapter-8-boundaries)
- [Chapter 9: Unit Tests](#chapter-9-unit-tests)
- [Chapter 10: Classes](#chapter-10-classes)
- [Chapter 11: Systems](#chapter-11-systems)
- [Chapter 12: Emergence](#chapter-12-emergence)
- [Chapter 13: Concurrency](#chapter-13-concurrency)
- [Chapter 17: Smells and Heuristics](#chapter-17-smells-and-heuristics)

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

Clean tests follow 5 rules - FIRST:

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

## Chapter 11: Systems

It is a myth we can get the systems "right the first time". Instead we should implement only today's stories, then refactor and expand the system to implement new stories tomorrow. This is the essence of iterative and incremental agility. 

Use the simplest thing that can possibly work.

## Chapter 12: Emergence

According to Kent, a design is simple if it follows these rules:

- runs all tests - system needs to be testable - if this can not be achieved, system should not be released, all tests need to pass
- contains no duplication
- expresses the intent of the programmer - the clearer the code, the less time others will have to spend understanding it (small functions and classes, good names)
- minimises the number of classes and methods - least important rule, above rules are more important, however overall goal should be to keep system small

Can set of practices replace experience? No. On the other hand, practices are a crystallised form of the many decades of experience of many authors.

## Chapter 13: Concurrency

Concurrency is a decoupling strategy. It helps to decouple what gets done from when it gets done. In single-threaded apps wheat and when are strongly coupled. 

Concurrency Defence Principles:

- Single Responsibility Principle - concurrency-related code should be kept separately from other code
- limit the access to any data that may be shared
- a good way of avoiding shared data is to avoid sharing data in the first place
- use copy of data , collect results from multiple threads and merge results
- threads should be as independent as possible

Java supports thread-safe collections, eg. ConcurrentHashMap, there are also other classes to support advanced concurrency: ReentrantLock - a lock that can be acquired and released, Semaphore - a classic lock with count, CountDownLatch - a lock that waits for a number of events before releasing all threads waiting on it.

Couple of behaviours:

- Bound Resources - resources of a fixed size or number used in a concurrent environment, eg. database connection
- Mutual Exclusion - only one thread can access shared data or a shared resource at a time
- Starvation - thread(s) prohibited from proceeding fro an excessively long time or forever
- Deadlock - two or more threads waiting for each other to finish
- Livelock - threads in lockstep, each trying to do work but finding another "in the way", threads continue trying to make progress but are unable

Execution models:

- producer - consumer - one or more threads create some work and place it in a queue, one or more consumer threads acquire that work from queue and complete it
- readers - writers - writers wait until there is no readers before allowing the writer to perform an update, if there are continuous readers, writers will starve
- dining philosophers - a hungry philosopher needs 2 forks before accessing the food, after consumption releases forks and waits until he is hungry again. There are number of solutions to this problem. 

`synchronised` keyword introduces a lock in Java. Locks are expensive so use them carefully, also such sections should be small.

Graceful shutdown is hard to get correct. Think about it early and get it working early.

General tips:

- get your non-threaded code working first
- make threaded-based code pluggable (one thread, n threads, ...)
- run with more threads than processors

## Chapter 17: Smells and Heuristics

Comments:

- Metadata should not appear in the comment (author, modification date). Comments should be reserved for technical notes only.
- Do not write comments that will become obsolete.
- Do not paraphrase code.
- Be brief and correct.
- Instead of commenting-out code - delete it.

Environment:

- You should be able to check out system with one simple command.
- You should be able to run all unit tests with just one command.

Functions:

- Functions should have a small number of arguments, no argument is best. More than 3 arguments is very questionable and should be avoided.
- Output arguments are counterintuitive readers expect arguments to be inputs, not outputs. If function must change state of something, have it change the state of the object it is called on.
- Flag arguments should be avoided (boolean flags) - they loudly declare function is doing multiple things.
- Methods that are never called should be removed. Dead code is wasteful.

General:

- The ideal source files should contain one, and only one language (for example Java + JavaScript snippets + English comments).
- Function / Class should implement the behaviours that another programmer could reasonably expect.
- Check every boundary condition.
- No duplication, perhaps the most important rule. Duplicated code means a missed opportunity for abstraction. Codd Normals Forms are a strategy for eliminating duplication.
- It is important to create abstractions that separate higher level general concepts from lower level detailed concepts.
- High level concepts should be independent from low level derivatives.
- A well-defined interface does not offer very many functions to depend upon, so coupling is low. Good software engineers learn to limit what they expose at the interfaces of their classes and modules.  
- Get rid of dead code - code that is never executed.
- Variables and functions should be defined close to where they are used.
- Use consistent naming.
- Keep source code organised and free of clutter.
- Things that don't depend upon each other should not be artificially coupled.
- Feature envy - the methods of a class should be interested in the variables and functions of the class they belong to, and not the variables and functions of other classes.
- Code should be expressive as possible.
- Code should be placed where a reader would naturally expect it to be (the principle of least surprise).
- Think if function should be static or not.
- Variables should have meaningful names, also use intermediate variables when performing difficult calculations. 
- Function names should say what they do, if you can't understand what function does by reading the call - change the name.
- Polymorphism is preferred over if / else or switch / case statements.
- Follow code standards.
- Replace magic numbers with named constants.
- Be precise, use appropriate data structures.
- Encapsulate conditions - boolean logic is hard to understand without having to see it in the context, extract the functions that explain the intent of the conditional.
- Avoid negative conditions - harder to understand.
- Functions should do one thing.
- Encapsulate boundary conditions.
- The statements within a function should all be written at the same level of abstraction.
- Keep configurable data at high levels.
- Law of Demeter - we don't want a single module to know much about its collaborators.

Names:

- Choose descriptive names. Names in software are 90% of what makes software readable.
- Choose names at the appropriate level of abstraction. Don't pick names that communicate implementation details.
- Use standard nomenclature where possible.
- Use unambiguous names.
- Names should describe side effects.

Tests:

- Use coverage tool.
- Don't skip trivial tests.
- Test boundary conditions.
- Tests should be fast.
