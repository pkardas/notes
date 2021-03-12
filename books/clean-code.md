[go back](https://github.com/pkardas/learning)

## Clean Code: A Handbook of Agile Software Craftsmanship
Book by Robert Cecil Martin

[TOC]

#### Chapter 1: Clean Code

- ugly code is expensive
- take your time to write a good code
- bad code programmer's fault, not PO's, manager's or anyone's else
- bad code is like a building with broken windows - people see ugly building and stop caring
- code like a prose, code should look like you care
- make the language look like it was made of the problem
- code rot quickly

#### Chapter 2: Meaningful names

Variable name should answer all the questions. It should tell why it exists. If a name requires a comment it does not reveal its content. Names should be pronounceable. One letter variables are hard to `grep` in the code - should be ONLY as local variables inside short methods. The length of a name should correspond to the size of its scope. Avoid encodings. 

>  Difference between a smart programmer and a professional programmer is that professional programmer understands that **clarity is a king**.

Don't be funny 😔 People tend to forget jokes, so people will forget true meaning of a variable. Choose clarity over entertainment. Do not use slang or culture-dependant names.

Pick one word per concept, eg. `get` instead of `fetch`, `retrieve`, ...

#### Chapter 3: Functions

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

#### Chapter 4: Comments

Comments are usually bad, they mean you failed to express yourself in code. IMO: Best comments are the ones that are explaining why things were done in a particular way. 

Don't put historical discussions or irrelevant details into the comments.