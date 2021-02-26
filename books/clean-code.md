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

