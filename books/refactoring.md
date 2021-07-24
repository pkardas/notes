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

