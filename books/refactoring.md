[go back](https://github.com/pkardas/learning)

# Refactofing: Improving the Design of Existing Code

Book by Martin Fowler (Second Edition)

[TOC]

## Chapter 1: Refactoring: A First Example

A poorly designed system is hard to change - because it is hard to figure out what to change and hoe these changes will interact with existing code. 

> When you have to add a feature to a program but the code is not structured in a convenient way, first refactor the program to make it easy to add the feature, then add the feature.

Before making any changes, start with self-checking tests (assertions checked by testing framework). Tests can be considered as bug detectors, they should catch any change that introduces bugs.

Refactoring changes the programs in small steps, so if you make a mistake, it is easy to find where the bug is. Author suggests committing after each successful refactoring, so it is easier get back to a working state, then he squashes changes into more significant commits before pushing changes to the remote repository.

When refactoring a long functions, mentally try to identify points that separate different parts of the overall behaviour (decomposition). Extracting a function is a common refactoring technique. 

> Any fool can write code that a computer can understand. Good programmers write code that humans can understand.

Other techniques discussed also later: Replace Temp with Query, Inline Variable, Change Function Declaration, Split Loop, Slide Statements.

Think of the best name at the moment and rename it later. Breaking large functions into smaller, only adds value if the names are good.

> Programmers are poor judges of how code actually performs. Many of our intuitions are broken by clever compilers, modern caching techniques, .... The performance of software usually depends on just a few parts of the code, and changes anywhere else don't make an appreciable difference.

ANYHOW, if refactoring introduces performance slow-downs, finish refactoring first and then do performance tuning.

Mutable data quickly becomes something rotten.

> Always leave the code base healthier than when you found it. It will never be perfect, but it should be better.

> A true test of good code is how easy it is to change it. Code should be obvious.

When doing refactoring, take small steps, each step should leave code in a working state that compiles and passes its tests.

## Chapter 2: Principles in Refactoring

Refactoring (noun) - a change made to the internal structure of software to make it easier to understand and cheaper to modify without changing its observable behaviour.

Refactoring (verb) - to restructure software by applying a series of refactorings without changing its observable behaviour.

When doing refactoring, code should not spend much time in a broken state, meaning it allows to stop at any moment even if you haven't finished. If someone says their code was broken for couple of days while they are refactoring, you can be pretty sure they were not refactoring. 

Two Hats - when developing new functionalities - do not change existing code, when refactoring - do not add new functionalities. Swap hats: refactor, add functionality, refactor, ...

Why should we refactor?

- software design improvement - changes are made to achieve short-term goals, because of that, code looses its structure, regular refactoring help keep the code in shape. Important aspect of refactoring is eliminating duplicated code.
- makes software easier to understand - think about future developers, decrease time needed to make a change. You don't have to remember every aspect of code, make it easy to understand and decrease load on your brain.
- helps in finding bugs - clarify the structure, certain assumptions.
- helps programming faster - adding new features might be difficult in a system full of patches and patches for patches, clear structure allows to add new capabilities faster. Good design allows to quickly find place where a change needs to be made. Also if code is clear, it is less likely to introduce a bug. Code base should be a platform for building new features for its domain.

> The Rule of Three - The first time you do something, you just do it. The second time you do something similar, you wince at the duplication, but you do the duplicate anyway. The third time you do something similar, you refactor.

When should we refactoring?

- preparatory refactoring - building a foundation for a new feature. 

  - > It is like you want to go 100 km east but instead of traipsing through the woods, you drive 20 kms north to the highway and the you are going 3x the speed you could have if you just went straight there.

- comprehension refactoring - making code easier to understand. Move understanding of a subject from head to code itself.

- litter-pickup refactoring - make small changes around place you are currently viewing - Boy Scout Rule.

- planned and opportunistic refactoring - refactoring should happen when doing other things, planned refactorings are usually required in teams that neglected refactoring.

- long-term refactoring - refactoring may take weeks because of new library or pull some section of code out into a component that can be shared between teams - even in such cases refactoring should be performed in small steps.

- refactoring in a code review - code reviews help spread knowledge, through a development team. Code may look clear to me but not for my team. Code reviews give the opportunity for more people to suggest useful ideas. 

Sometimes it easier to rewrite than refactor. The decision to refactor or rewrite requires good judgement and experience. 

However, there are couple of problems associated to refactoring:

- some people see refactoring as something that is slowing down development (which is not really true), this should be explained - the economic benefits of refactoring should always be the driving factor, we refactor because it makes us faster to add features and fix bugs.
- merge conflicts may be painful, especially in a team of multiple full-time developers, suggested approach is to use CI - Continuous Integration - each team member integrates with mainline at least once per day.
- to perform refactoring correctly you need to have good tests, code needs to be self-testing, without self-testing code refactoring carries high risk of introducing bugs 
- refactoring legacy code is hard, but is a fantastic tool to help understand a legacy system. Legacy code is often missing tests, adding tests for legacy code is difficult because it wasn't designed with testing in mind.
- some time ago database refactoring was considered a problem era, currently we have migrations which are making database refactoring possible

Refactoring changed how people think about architecture (previously: completed before any development, now: changed iteratively). YAGNI does not mean you need to neglect all architectural thinking. 


