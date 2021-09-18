[go back](https://github.com/pkardas/learning)

# Refactoring: Improving the Design of Existing Code

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

In order to be fully agile, team has to be capable and enthusiastic refactorers. The first foundation for refactoring is self-testing code, the second is CI.

Good programmers know that they rarely write clean code the first time around. 

IDEs use the syntax tree to analyse and refactor code (eg. changing variable name is on syntax tree level, not on text level), this makes IDEs more powerful than text editors.

## Chapter 3: Bad Smells in Code

When you should start refactoring? It is a matter of intuition. However there are some indicators.

MYSTERIOUS NAME - code needs to be mundane and clear, good name can save hours of puzzled incomprehension in the future.

DUPLICATED CODE - if you see the same code structure in more than one place, your program will be better if you find a way to unify them., duplication means every time you read these copies you need to read them carefully and look for differences. 

LONG FUNCTION - the programs that live best and longest are those with short functions. Whenever you feel you need to comment something - decompose. Even a single line is worth extracting if it needs an explanation. Conditionals and loops are also signs for extractions.

LONG PARAMETER LIST - long lists of parameters are confusing - pass an object, use query on existing object or combine function on object.

GLOBAL DATA - problem with global data is that it can be modified from any place in the code base, this leads to bugs.  Global data: global variables, class variables, singletons. Global data is especially nasty when it is mutable. 

MUTABLE DATA - (from functional programming) data should never change, updating data structure should return a new copy of the structure, leaving the old data pristine.

DIVERGENT CHANGE - making changes should be easy, if you need to, for example, edit 4 functions every time you add a new financial instrument, something is off.

SHOTGUN SURGERY - every time you make a change, you have to make a lot of little edits to a lot of different classes, when changes are all over the place, they are hard to find and it is easy to miss an important change. In such case all fields should be put in a single module. 

FEATURE ENVY - for example: a function in one module spends more time communicating with functions or data inside another module than it does within its own module - the function clearly wants to be with the data, so move function to get it there. Put things together that change together. 

DATA CLUMPS - some items enjoy hanging around together, same three or four data items appear together in lots of places - you can group them together. 

PRIMITIVE OBSESSION - many programmers are reluctant to create their own fundamental types which are useful for their domain.

REPEATED SWITCHES - basically the same problem as in DUPLICATED CODE.

LOOPS - loops are less relevant in programming today because of presence of map and filter mechanisms.

LAZY ELEMENT - sometimes you may want to replace function with inline code or collapse objects hierarchy.

SPECULATIVE GENERALITY - all the special cases to handle situations that are not going to happen soon (YAGNI).

TEMPORARY FIELD - a class with a field which is set only in certain circumstances - difficult to understand.

MESSAGE CHAINS - client asks object for another object, which the client asks for yer another object - this might cause a train wreck, navigating such code is difficult. 

MIDDLE MAN - internal details of the object should be hidden from the rest of the world

INSIDER TRADING - modules should be separated to keep them whispering, if 2 modules have common interests, create a third module for this communication.

LARGE CLASS - when class has too many fields it is a sign that it is doing too much, this means duplicated code, chaos and death.

ALTERNATIVE CLASSES WITH DIFFERENT INTERFACES - if you are allowing substitution, classes have to have the same interface.

DATA CLASS - classes with fields, setters and getters - nothing else. Such classes are often being manipulated in far too much detail by other classes. You can try to move that behaviour into the data class. 

REFUSED BEQUEST - wrong hierarchy, subclasses don't want or need what they are given.

COMMENTS - when you feel the need to write a comment, first try to refactor the code so that any comment becomes superfluous. 

## Chapter 4: Building Tests

Proper refactoring can not be done without proper tests. A suite of tests is a powerful bug detector that decapitates the time it takes to find bugs. 

TDD allows to concentrate on the interface rather than the implementation, which is a good thing. 

Always make sure a test will fail when it should (try to break your code, to see if test fails as well).

Testing should be risk-driven, you don't need to test every getter. 

When you get a bug report, start by writing a unit test that exposes the bug. 

The best measure for a good enough test suite is subjective: How confident are you that is someone introduces a defect into your code, some test will fail? 

## Chapter 5: Introducing the Catalog

The rest of the book is a catalog of refactorings. Each *Refactoring* has: name, sketch, motivation, mechanics and examples.

## Chapter 6: A First Set of Refactorings

EXTRACT FUNCTION - write small functions.

INLINE FUNCTIONS - inverse of *extract function*, sometimes function body is as clear as the name. Helpful when you need to group functions - first you join them and then extract functions. 

EXTRACT VARIABLE - inverse of *inline variable*, expressions can become very complex and hard to read in such situations, local variables may help break the expression down into something more manageable. 

INLINE VARIABLE - inverse of *extract variable*, sometimes name doesn't communicate more than the expression itself.

CHANGE FUNCTION DECLARATION - if you see a function with the wrong name, change it as soon you understand what a better name would be, so next time you are looking at the code you don't have to figure out what is going on. Often a good way of improving name is to write a comment to describe the function's purpose - then turn that comment into a name (applies to names as well). Adding / removing parameters can be done through introducing intermediate wrapping function. 

ENCAPSULATE VARIABLE - encapsulate access to the variable using functions, instead of accessing data directly, do this through single access point - function. Keeping data encapsulated is less important for immutable data. 

RENAME VARIABLE - variables can do a lot to explain what programmer is up to (if he names it well). 

INTRODUCE PARAMETER OBJECT - often a group of data items travel together, appear in function after function. Such group is a data clump - this can be easily replaced with data structure.

Example: 

```
def amountInvoiced(start: date, end: date)
def amountInvoiced(date_range: Range)
```

Grouping data into a structure is valuable because it makes explicit the relationship between the data items and reduces the size of parameter lists. Grouping helps to identify new structures. 

COMBINE FUNCTIONS INTO CLASS - when group of functions operate closely together on a common body of data, there is an opportunity to form a class. 

> Uniform access principle - All services offered by a module should be available through a uniform notation, which does not betray whether they are implemented through storage or through computation. With this, the client of the class can't tell whether the *value* is a field or derived value.

COMBINE FUNCTIONS INTO TRANSFORM - instead of aggregating function into classes you can build functions that are enriching existing objects. Transformation is about producing essentially the same thing with some additional information. 

SPLIT PHASE - whenever you encounter code that does two things, look for a way to split it into separate modules. If some processing has 2 stages, make the difference explicit by turning them into 2 separate modules. 

## Chapter 7: Encapsulation

ENCAPSULATE RECORD - instead of using plain dictionaries, encapsulate them into object. With object you can hide what is stored and provide methods for all the values. The user does not have to care which value is calculated and which is stored. **Dictionaries are useful** in many programming situations **but they are not explicit about their fields**. Refactor implicit structures into explicit ones. 

ENCAPSULATE COLLECTION - good idea is to ensure that the getter for the collection can not accidentally change it. One way to proevent modification of a collection is to use some form of read-only proxy to the collection. Such proxy can allow all reads but block any write to the collection. The most popular approach is to provide a getting method for the collection, but make it return a copy of underlying collection. 

Replacing `customer.orders.size` with `customer.num_of_orders` is not recommended, because adds a lot of extra code and cripples the easy composability of collection operations.

If the team has the habit of not modifying collections outside the original module, it might be enough.

It is worse to be moderately paranoid about collections, rather copy them unnecessarily than debug errors due to unexpected modifications. For example instead of sorting in place return a new copy. 

REPLACE PRIMITIVE WITH OBJECT - simple facts can be represented by simple data items such as numbers or strings, as development proceeds, those simple items aren't so simple anymore. This is one of the most important refactorings. Starting with simple wrapping value with the object, you can extend the class with additional behaviours. 

REPLACE TEMP WITH QUERY - using temporary variables allows to refer to the value while explaining its meaning and avoiding repeating the code that calculates it. But while using a variable is handy, it can often be worthwhile to go a step further and use a function instead, mostly when the variable needs to be calculated multiple times across the class. 

EXTRACT CLASS - split classes containing too much logic into separate classes. Good signs for doing so:

- subset of the data and a subset of methods seem to go together
- data that usually change together or are particularly dependent on each other

Useful test: Ask question: what would happen if you remove a piece of data or a method, what other fields and methods would become nonsense?

INLINE CLASS - inverse of *Extract Class*. Generally useful as intermediate step when performing refactoring, eg. you put all attributes in one class, just to split them later. 

HIDE DELEGATE - Example: `person.department.manager` should be replaced with `person.manager` (additional getter hiding delegate). Why? If delegate changes its interface, change has to propagated across all parts of the system.

REMOVE MIDDLE MAN - inverse of *Hide Delegate*. Sometimes forwarding introduced by Hide Delegate, becomes irritating. Sometimes it is easier to call the delegate directly (violation of Law of Demeter, but author suggests better name: Occasionally Useful Suggestion of Demeter). 

SUBSTITUTE ALGORITHM - There are usually several ways to do the same thing, same is with algorithms. When you learn more about the problem, you can realise there is an easier way way to do it. 

## Chapter 8: Moving Features

Another important part of refactoring is moving elements between contexts.

MOVE FUNCTION - one of the most straightforward reasons to move a function is when it references elements in other contexts more than the one it currently resides in. Deciding to move a function rarely an easy decision. Examine the current and candidate contexts for that function.

MOVE FIELD - programming involves writing a lot of code that implements behaviour - but the strength of a program is really founded on its data structures. If I have a good set of data structures that match the problem, then my behaviour code is simple and straightforward. Moving fields usually happen in the context of a broader set of changes. 

MOVE STATEMENTS INTO FUNCTION - removing duplication is one of the best rules of thumb of healthy code. Look to combine repeating code into the function. That way any future modifications to the repeating code can be done in one place and used by all the callers. 

MOVE STATEMENTS TO CALLERS - this is inverse of *Move Statements into Function*. Motivation for this refactoring is that we rarely get the boundaries right. Sometimes common behaviour used in several places needs to vary in some of its calls, that is why you can move the varying behaviour function to its callers.

REPLACE INLINE CODE WITH FUNCTION CALL - functions allow to package bits of behaviour, this is useful for understanding - a named function can explain the purpose of the code rather than its mechanics. Also useful for deduplication. 

SLIDE STATEMENTS -  code is easier to understand when things that are related to each other appear together. If several lines of code accesses the same data structure, it is best for them to be together rather than intermingled with code accessing other data structures. You can also declare the variable just before you first use it.

SPLIT LOOP - you often seen loops that are doing two different things at once just because they can do that with one pass trough a loop. But if you are doing two different things in the same loop, then whenever you need to modify the loop you have to understand both things. By splitting loop, you ensure you only need to understand the behaviour you need to modify. Many programmers are uncomfortable with this refactoring as it forces you to execute the loop twice. REMINDER: Once you have your code clear, you can optimise it, and if the loop traversal is a bottleneck, it is easy to slam the loops back together. But the actual iteration through even a large list I rarely a bottleneck, and splitting the loops often enables other, more powerful optimisations. 

REPLACE LOOP WITH PIPELINE - language environments provide better constructs than loops - the collection pipeline (`input.filter(...).map(...)`). Logic much easier to follow if it is expressed as a pipeline. It can be read from top to bottom to see how objects flow through the pipeline. 

REMOVE DEAD CODE - decent compilers will remove unused code. But unused code is still a significant burden when trying to understand how the software works. Once code is not used it should be deleted. If you need it sometime in future - you have a version control system so you can always dig it out again. Commenting out dead code was once a bad habit, it wa useful before version control systeuswere widely used or when they were inconvenient. 

## Chapter 9: Organising Data

Data structures play an important role in our programs, so no surprise there are a clutch of refactorings that focus on them. 

SPLIT VARIABLE - Using a variable for two different things is very confusing for the reader. Any variable with more than one responsibility should be replaced with multiple variables, one for each responsibility.

Exception: Collecting variables (eg. `i = i + 1`) - often used for calculating sums, string concatenation, writing to stream or adding to a collection - don't split it.

RENAME FIELD - Data structures are the key to understand what is going in inside the system. It is essential to keep them clear. Rename fields in classes / records so they are easy to understand. 

REPLACE DERIVED VARIABLE WITH QUERY - One of biggest sources of problems in software is mutable data. Data changes can often couple together parts of code in awkward ways, with changes in one part leading to knock-on effects that are hard to spot. Remove variables that can be easily calculated. A calculation  often makes it clearer what the meaning of the data is, and it is being protected by from being corrupted when you fail to update the variable as the source data changes.

CHANGE REFERENCE TO VALUE - Instead of updating values of the nested objects, create new object with updated params. Value objects are generally easier to reason about, particularly because they are immutable. Immutable data structures are easier to work with.

CHANGE VALUE TO REFERENCE - (inverse of *Change Reference to Value*). A data structure may have several records linked to the same logical data structure. The biggest difficulty in having physical copies of the same logical data occurs when you need to update the shared data. Then you have to find all the copies and update them all. If you miss one, you will get a troubling inconsistency in the data. In this case, it is often worthwhile to change the copied data into a single reference.

## Chapter 10: Simplifying Conditional Logic 

Much of the power of programs comes from their ability to implement conditional logic - but, sadly, much of the complexity of programs lies in these conditionals. 

DECOMPOSE CONDITIONAL - Length of a function is in itself a factor that makes it hared to read, but conditions increase the difficulty. As with any large block of code, you can make your intention clearer by decomposing it and replacing each chunk of code with a function call named after the intention of that chunk.

CONSOLIDATE CONDITIONAL EXPRESSION - Sometimes you can run into a series of conditional checks where each check is different yet the resulting action is the same. When you see this, you can use `and` and `or` operators to consolidate them into a single conditional check with a single result.

Consolidating is important because it makes it clearer by showing that you are making a single check that combines other checks, and because it often sets you up for *Extract Function*. Extracting a condition is one of the most useful things you can do to clarify code. 

REPLACE NESTED CONDITIONAL WITH GUARD CLAUSES - Guard Clause says: "This isn't the core to this function, and if it happens, do something and get out". In other words, if you know the result, return it immediately instead of assigning to `result` variable, just to have one single return statement at the end of the function.

*// A guard clause is simply a check that immediately exits the function, either with a return statement or an exception.*

REPLACE CONDITIONAL WITH POLYMORPHISM - It is possible to put logic in superclasses which allows to reason about it without having to worry about the variants. Each variant case can be put in in a subclass. Complex conditional logic can be improved using polymorphism. This feature can be overused, basic conditional logic should use basic conditional statements. 

INTRODUCE SPECIAL CASE - also known as: *Introduce Null Object*. Many parts of the system have the same reaction to a particular value, you may want to bring that reaction into a single place. Special Case pattern is a mechanism that captures all the common behaviour, this allows to replace most of special-case checks with simple calls. A common value that needs special-case processing is null, which is why this pattern is often called the Null Object pattern. 

INTRODUCE ASSERTION - Often, sections of code work only if certain conditions are true. Such assumptions are not often stated explicitly, but can only be deducted by looking trough an algorithm. Sometimes, these assumptions are stated with a comment. A better technique is to make the assumption explicit by writing assertion. Failure of an assertion indicates a programmer error. Assertions should never be checked by other parts of the system. Assertions should be written that the program functions equally correctly if they all removed. Use assertions to check things that need to be true, use them when you think they should never fail.
