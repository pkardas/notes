[go back](https://github.com/pkardas/learning)

# Code Complete: A Practical Handbook of Software Construction

Book by Steve McConnell

- [Chapter 1: Software Construction](#chapter-1-software-construction)
- [Chapter 2: Metaphors for a Richer Understanding of Software Development](#chapter-2-metaphors-for-a-richer-understanding-of-software-development)
- [Chapter 8: Defensive Programming](#chapter-8-defensive-programming)
- [Chapter 20: The Software-Quality Landscape](#chapter-20-the-software-quality-landscape)
- [Chapter 21: Collaborative Construction](#chapter-21-collaborative-construction)
- [Chapter 22: Developer Testing](#chapter-22-developer-testing)
- [Chapter 24: Refactoring](#chapter-24-refactoring)
- [Chapter 25: Code-Tuning Strategies](#chapter-25-code-tuning-strategies)
- [Chapter 32: Self-Documenting Code](#chapter-32-self-documenting-code)
- [Chapter 33: Personal Character](#chapter-33-personal-character)
- [Chapter 34: Themes in Software Craftsmanship](#chapter-34-themes-in-software-craftsmanship)

## Chapter 1: Software Construction

Construction - process of building (planning, designing, checking the work). Construction is mostly coding and debugging
but also involves designing, planning, unit testing, ... Centre of the software development process. The only activity
that is guaranteed to be done (planning might be imperfect, etc.).

## Chapter 2: Metaphors for a Richer Understanding of Software Development

Metaphors contribute to a greater understanding of software-development issues - paper writing metaphor, farming
metaphor, etc...

## Chapter 8: Defensive Programming

Protecting yourself from "cruel world of incorrect data". Use assertions to document assumptions made in the code.

Guidelines:

- use assertions for conditions that should never occur, this is not error checking code. On error program should take
  corrective actions, on assertion fail source code should be updated.
- no executable code in asserts:
    - bad: `assert foo(), ...`
    - good: `result = foo(); assert result, ...`
- use asserts to document and verify preconditions (before executing the routine) and post conditions (after executing
  the routine)
- for high robustness: failed assertions should be handled anyway

Error handling:

- return neutral value - 0, empty string, ...
- substitute the next piece of valid data - for example when processing stream of data from the sensor (e.g.
  temperature)
  , you may want to skip the missing value and wait for another
- return the same answer as the previous time - some data might not change in time dramatically, so it is okay to return
  the last correct value
- substitute the closest legal value - for example reversing car does not show negative speed value but instead shows
  0 (the closest legal value)
- log a warning message on incorrect data
- return error code - report error has been encountered and trust some other routine higher up will handle the error
- call centralised error-processing routine, disadvantage is that entire program coupled with the mechanism
- display error message to the user, warning: don't share too much with the user, attacker may use this information
- shut down - useful in safety-critical applications

While handling errors you need to choose between robustness (do something to keep the software alive) and correctness (
ensuring the data is always correct). Once approach is selected it should be coherent across the system.

Exceptions:

- they eliminate the possibility to go unnoticed
- throw only for truly exceptional situations - for situations that can not be addressed
- if exception can be handled locally - handle locally
- avoid exceptions in constructors, because if exception happens there, destruction might not be called - resource leak!
- include all the information that led to the exception
- avoid empty catch blocks
- standardise project's use of exceptions

Barricades:

- similar to having isolated compartments in the hull of a ship, damaged parts are isolated
- use validation classes that are responsible for cleaning the data
- assume data is unsafe and you need to sanitise it

*Offensive programming* - exceptional cases should be handled in a way that makes them obvious during development and
recoverable when production code is running. During development, you want errors to be as visible as possible but during
production it should not be observable.

## Chapter 20: The Software-Quality Landscape

There are many quality metrics: correctness, usability, efficiency, reliability, integrity, adaptivity, accuracy,
robustness - these are metrics important to the user, for a programmer more important metrics are: maintainability,
flexibility, portability, reusability, readability, testability, understandability.

*Techniques for Improving Software Quality*: set up software quality objectives, perform quality assurance activities,
prototyping.

Defect-detection techniques: design reviews, code reviews, prototyping, unit tests, integration tests, regression tests,
... even all of them combined will not detect all the issues.

> Most studies have found that inspections are cheaper than testing. A study at the Software Engineering Laboratory 
> found that code reading detected about 80% more faults per hour than testing.

Cost of detection is only one part. There is also cost of fixing the issues. The longer defect remains in the system,
the more expensive it becomes to remove.

Recommended combination: Formal inspections of all requirements, architecture, design -> Modeling / prototyping -> Code
reading -> Testing.

Remember: Improving quality reduces development cost.

## Chapter 21: Collaborative Construction

> IBM found that each hour of inspection prevented about 100 hours or related work (testing and defect correction)

> Reviews cut the errors by over 80%

> Reviews create a venue for more experienced and less experienced programmers to communicate about technical issues.

Collective ownership - code is owned by the group rather than by the individuals and can be accessed and modified by
various members.

Guide on pair programming:

- it will not be effective if you argue on styling conventions
- don't let it turn into watching - person without the keyboard should be an active participant
- sometimes it is better to discuss something on the whiteboard and then go programming solo
- rotate pairs
- match other's pace, the fast learner needs to slow down
- don't force people who don't like each other to pair
- no pairing between newbies

Nice idea: for discussing the design everyone should come with a prepared list of potential issues. It is good to assign
perspectives - maintainer, coder, user, designer. Author in such discussion should play minor role, should only present
the overview. Reviewer can be anyone outside author - tester, developer. Management should not be present at the
meeting, however should be briefed with the results after the discussion. Design review can not be used for performance
appraisals. Group should be focused on identifying defects. Goal of this meeting is not to explore alternatives ar
debate who is right and who is wrong.

> NASA's Software Engineering Laboratory found that code reading detected about 3.3 defects per hour of effort. Testing
> detected 1.8 errors per hour.

## Chapter 22: Developer Testing

> You must hope to find errors in your code. Such hope might seem like an unnatural act, but you should hope that it's
> you who finds the errors and not someone else.

Why TDD:

- same effort to write test cases before and after
- you detect defects earlier, and you can correct them more easily
- forces you to think a little about the requirements and design before writing code
- exposes requirements problems sooner

Developers tend to write *clean tests* rather than test for all the ways code breaks. Developer's testing isn't
sufficient to provide adequate quality assurance.

General Principle of Software Quality: improving quality improves the development schedule and reduces development cost.

## Chapter 24: Refactoring

The Cardinal Rule of Software Evolution: Evolution should improve the internal quality of the program.

Signs / smells that indicate refactoring is needed:

- code duplication - you need to do parallel changes
- too long routine
- too long loop or too deeply nested
- poor class cohesion - if a class takes ownership for many unrelated responsibilities
- too many parameters
- changes require parallel modifications to multiple classes
- related data not organised into classes
- overloaded primitive data type
- class doesn't do much - sometimes the result of refactoring is that an old class doesn't have much to do
- trap data - one routine just passes data to another
- one class knows too much about the other
- poor names
- public data members - in general bad idea
- subclass uses only a small percentage of its parent routines
- comments should not be used to explain bad code - "don't comment bad code, rewrite it"
- usage of setup code before routine call
- code that "seems like it might be needed one day" - programmers are rather bad at guessing what functionality might be
  needed someday, *design ahead* introduces unnecessary complexity

Data-Lever Refactoring:

- replace magic number with a named constant
- give a variable informative name
- inline expressions
- replace expression with a routine
- convert data primitive to a class
- encapsulate returned collection

Statement-Level Refactoring:

- decompose boolean expression - use variables that help document the meaning of the expression
- move boolean expression into a well-named function
- return as soon as you know the return value

Routine-Level Refactoring:

- Inline simple routines
- Convert long routine into a class
- Separate query operations from modification operations
- Combine similar routines by parametrizing themIf routine depends on the parameter passed in - consider splitting the
  routine
- Pass a whole object instead of specific fields, however if you are creating an object just to pass it to a routine,
  consider changing the routine to take only specific fields
- Routine should return the most specific object (mostly applicable to iterators, collections, ...)

Class Implementation Refactoring:

- Extract specialised code into a subclass - if class has code that is used by only a subset of its instances
- Combine similar code into a superclass - if at least 2 classes have similar code

Class Interface Refactoring:

- Eliminate classes not doing too much
- Hide a delegate - A calling B, A calling C, when really class A should call B and class B should call class C
- Or remove middleman, remove B and make A call C directly
- Hide routines that are not intended to be used outside the class
- Encapsulate unused routines - if you use only small portion of class's interface

Refactoring might cause a lot of harm if misused:

- refactoring should be small
- one refactoring at a time
- make a list of needed steps
- make a parking lot - in the middle of refactoring you might think about another refactoring, and another, and so on,
  for changes that aren't required immediately save a list of TODO changes
- check IDE / compiler / other tool's errors
- refactored code should be retested, programmer should also add more test cases
- be careful about small refactoring because they tend to introduce more bugs than big refactoring
- adjust approach basing on the risk of the refactoring - some changes are more dangerous than the other

Refactoring refers to making a changes in working code and do not affect the program's behaviour. Programmers who are
tweaking broken code aren't refactoring - they are hacking.

There are many strategies on where refactoring should be started. For example, whenever you are adding a routine you
should refactor it's neighbour, or when you are adding a class, or you should refactor error-prone modules, the most
complex modules, etc.

## Chapter 25: Code-Tuning Strategies

Code tuning is one way of improving a program's performance. You can find other ways to improve performance - faster and
without harm to the code.

> More computing sins are committed in the name of efficiency (without necessarily achieving it) than for any other 
> single reason - including blind stupidity ~ Wulf

Efficiency can be seen from many viewpoints:

- requirements

TRW required sub-second response time - this led to highly complex design and cost ~100M $, analysis determined, users
would be satisfied with 4 seconds responses 90% of time, modifying the response time requirements reduced cost by ~70M
$.

Before you invest time solving a performance problem, make sure you are solving a problem that needs to be solved.

- design

Sometimes program design make it difficult to write high-performance system, others make it hard not to.

- class and routine design

On this level algorithms and data structures matter.

- OS interactions

You might not be aware the compiler generated code using heavy OS calls.

- code compilation

Good compilers, turn good high-level language code into optimised machine code.

- hardware

Sometimes cheapest and the beast way to improve a program's performance is to buy a new hardware.

- code tuning

Small-scale changes that affect a single class, routine or just few lines of code, that make it run mode efficiently.

Some sources say, you can multiply improvements on each of the six levels, achieving performance improvement of a
million-fold.

Code tuning is not the most effective way to improve performance! Writing micro-efficient code does not prove you are
cool. Efficient code isn't necessarily better.

The Pareto Principle: Also known as 80/20 rule, you can get 80% of the result with 20% of effort.

Working toward perfection might prevent completion. Complete it first, and then perfect it. The part that needs to be
perfect is usually small.

False statement: Reducing the lines of code in a high level-language improves the speed or size of the resulting machine
code.:

```
# This is slower:
for i = 1 to 10
	a[i] = i

# This is faster:
a[1] = 1
a[2] = 2
...
a[10] = 10
```

It is also impossible to identify performance bottlenecks before program is working completely, hence "You should
optimise as you go" is false. Also, premature optimisation is the root of all evil, because you are missing perspective.

Compilers are really powerful, however they are better in optimising straightforward code than they are at optimising
tricky code. So, design application properly, write clear code and compiler will do the rest :)

Sources of inefficiency:

- I/O operations - if possible: store data in the memory
- paging - an operation that causes the OS to swap pages of memory is much slower than operation that works on only one
  page of memory.
- system calls - calls to system routines are expensive (context switch, saving app state, recovering kernel state),
  avoid using system calls, write your own routines using small part of the functionality offered by a system routine,
  work with system vendor to improve performance
- interpreted languages - :(
- errors - errors in code can be another source of performance problems

Experience doesn't help with optimisation. A person's experience might have come from an old machine, language or
compiler. You can never be sure about the effect of an optimisation until you measure the effect.

## Chapter 32: Self-Documenting Code

Unit development folder - informal document that contains notes used by a developer during construction - main purpose
is to provide a trail of design decisions that aren't documented elsewhere.

Detailed-design document - low-level design document, describes the class-level or routine-level design decisions.

Internal documentation (within the program) is the most detailed kind of documentation. The main contributor to
code-level documentation isn't comments, but good programming style, good variable names, clear layout and minimisation
of control-flow and data-structure complexity,

> **Good comments don't repeat the code or explain it. They clarify its intent. Comments should explain, at a higher 
> level of abstraction than the code, what you are trying to do.**

Kinds of comments:

- repeat of the code - comment gives no additional information
- explanation of the code - code is so complicated it needs to be explained, make code better instead of adding comments
- **summary of the code** - very useful when someone other than the code's original author tries to modify the code
- **description of the codes' intent** - IBM study says "understanding programmer's intent is the most difficult
  problem"
- **information that cannot be expressed by code itself** - for example copyright notice, notes about design, references
  to requirements

3 types of acceptable comments were highlighted above.

Effective commenting shouldn't be time-consuming. Guidelines for effective commenting:

- if commenting style is too fancy it very likely becomes annoying to maintain
- write pseudocode in comments
- performance is not a good reason for avoiding commenting (in some languages commenting slows down execution /
  compilation) - usually solution for this is to pass code through tool striping comments before release

End-line comments pose several problems and should be avoided - hard to write meaningful comment in one line, not much
space on the right side of the screen.

The code itself is always the first documentation you should check. If the code is not good enough, look for comments.

Comments should avoid abbreviations. Comments should justify violations of good programming style. Don't comment tricky
code, rewrite it. If something is tricky for you, for others it might be incomprehensible.

> Make your code so good that you don't need comments, and then comment it to make it even better.

Commenting data declarations:

- comment the units
- comment the range of allowable numeric values
- use enumerated types to express coded meanings
- comment limitations of input data, use assertions
- if variable is used as bit field, explain every bit
- if you have comments that refer to a specific variable, make sure the comment stays updated after variable name change

Keep comments close to the code they describe. Describe the design approaches, limitations, usage assumptions and so on.
Do not document implementation details in the interface.

## Chapter 33: Personal Character

The best programmers are the people who realise how small their brains are. The purpose of many good programming
practices is to reduce the load on your grey cells:

- decomposing - make a system simpler to understand
- reviews, inspections and tests - our intellectual capacity is limited, so we augment it with someone's else
- short routines reduce the load on our brains
- writing programs in terms of the problem domain rather than in terms of low level implementation details reduces
  mental workload
- conventions free brain from the relatively mundane aspects of programming

How to exercise curiosity and make a learning a priority?

- If your workload consists entirely on short-term assignments that don't develop your skills, be dissatisfied. Half of
  what you need to know will be outdated in three years. You are not learning, you are turning into a dinosaur. If you
  can't learn at your job, find a new one.
- Experiment if you don't understand something. Learn to make mistakes, learn from the each. Making a mistake is no sin.
  Failing to learn from mistake is.
- Read about problem-solving, don't reinvent the wheel.
- Study the work of the great programmers, it is not about reading 500-long source code but for example about high-level
  design.
- Read books, one book is more than most programmers read each year.
- Affiliate with other professionals
- Set up a professional development plan

Mature programmers are honest, which means: you refuse to pretend you are an expert when you are not, you admit your
mistakes, you provide realistic estimates, you understand your program.

Writing readable code is part of being a team player. As a readability guideline, keep the person who has to modify your
code in mind. Programming is communicating with another programmer first and communicating with the computer second.

To stay valuable, you have to stay current. For young hungry programmers, this is an advantage. Older programmers
sometimes feel they have already earned their stripes and resent having to improve themselves year after year.

Good habits matter because most of what you do as a programmer you do without consciously thinking about it.

## Chapter 34: Themes in Software Craftsmanship

There are many intellectual tools for handling computer science complexity:

- dividing a system into subsystems at the architecture level so that brain can focus on smaller amount of the system at
  one time
- carefully interface definition
- preserving the abstraction representing by the interface so that brain doesn't have to remember arbitrary details
- avoid global data
- avoid deep inheritance hierarchy
- carefully define error handling strategy
- prevent monster classes creation
- keep functions short
- use self-explanatory names
- minimise number of parameters passed to the routine
- use conventions

Points above are used to decrease usage of mental resources you need to use in order to understand the code.

Abstraction is a particularly powerful tool for managing complexity. Fred Brooks said that the biggest single gain ever
made in computer science was in the jump from machine language to higher-level languages. It freed programmers from
worrying about detailed quirks of individual pieces of the hardware and allowed them to focus on programming.

Reducing complexity is arguably the most important key to being and effective programmer.

Collective ability isn't simply the sum of the team members' individual skills. The way people work together determines
if abilities sum up or subtract from each other.

In real word, requirements are never stable -in order to build software more flexibly - use incremental approach, plan
to develop program in several iterations.

Write readable code because it helps other people to read the code. Computer doesn't care if code is readable. A
professional programmer writes readable code. Even if you think you are the only one who will read your code, in
reality, chances are good that someone else will need to modify your code. One study found that 10 generations of
maintenance programmers work on an average program before it gets rewritten.

If your language doesn't support some mechanisms do not hesitate and implement them (e.g. missing `assert`) on your own.

At the highest level, you shouldn't have any idea how the data is stored. Suggested levels of abstraction:

4. High level problem domain terms

3. low level problem domain terms

2. low level implementation structures

1. programming language structures and tools

0. operating system operations and machine instructions
