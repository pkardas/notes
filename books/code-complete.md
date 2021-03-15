[go back](https://github.com/pkardas/learning)

## Code Complete: A Practical Handbook of Software Construction
Book by Steve McConnell

[TOC]

#### Chapter 1: Software Construction

Construction - proces of building (planning, designing, checking the work). Construction is mostly coding and debugging but also involves designing, planning, unit testing, ... Centre of the software development process. The only activity that is guaranteed to be done (planning might be imperfect, etc.).

#### Chapter 2: Metaphors for a Richer Understanding of Software Development

Metaphors contribute to a greater understanding of software-development issues - paper writing metaphor, farming metaphor, etc...

#### Chapter 8: Defensive Programming

Protecting yourself from "cruel world of incorrect data". Use assertions to document assumptions made in the code.

Guidelines:

- use assertions for conditions that should never occur, this is not error checking code. On error program should take corrective actions, on assertion fail source code should be updated.
- no executable code in asserts:
  - bad: `assert foo(), ...`
  - good: `result = foo(); assert result, ...`
- use asserts to document and verify preconditions (before executing the routine) and postconditions (after executing the routine)
- for high robustness: failed assertions should be handled anyway

Error handling:

- return neutral value - 0, empty string, ...
- substitute the next piece of valid data - for example when processing stream of data from the sensor (eg. temperature), you may want to skip the missing value and wait for another
- return the same answer as the previous time - some data might not change in time dramatically, so it is okay to return the last correct value
- substitute the closest legal value - for example reversing car does not show negative speed value but instead shows 0 (closest legal value)
- log a warning message on incorrect data
- return error code - report error has ben encountered and trust some other routine higher up will handle the error
- call centralised error-processing routine, disadvantage is that entire program coupled with the mechanism
- display error message to the user, warning: don't share too much with the user, attacker may use this information
- shut down - useful in safety-critical applications

While handling errors you need to choose between robustness (do something to keep the software alive) and correctness (ensuring the data is always correct). Once approach is selected it should be coherent across the system.

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

*Offensive programming* - exceptional cases should be handled in a way that makes them obvious during development and recoverable when production code is running. During development, you want errors to be as visible as possible but during production it should not be observable. 

#### Chapter 20: The Software-Quality Landscape

There are many quality metrics: correctness, usability, efficiency, reliability, integrity, adaptivity, accuracy, robustness - these are metrics important to the user, for a programmer more important metrics are: maintainability, flexibility, portability, reusability, readability, testability, understandability. 

*Techniques for Improving Software Quality*: set up software quality objectives, perform quality assurance activities, prototyping.

Defect-detection techniques: design reviews, code reviews, prototyping, unit tests, integration tests, regression tests, ... even all of them combined will not detect all the issues. 

> Most studies have found that inspections are cheaper than testing. A study at the Software Engineering Laboratory found that code reading detected about 80% more faults per hour than testing.

Cost of detection is only one part. There is also cost of fixing the issues. The longer defect remains in the system, the more expensive it becomes to remove. 

Recommended combination: Formal inspections of all requirements, architecture, design -> Modeling / prototyping -> Code reading -> Testing.

Remember: Improving quality reduces development cost.

#### Chapter 21: Collaborative Construction

> IBM found that each hour of inspection prevented about 100 hours or related work (testing and defect correction)

> Reviews cut the errors by over 80%

> Reviews create a venue for more experienced and less experienced programmers to communicate about technical issues. 

Collective ownership - code is owned by the group rather than by the individuals and can be accessed and modified by various members. 

Guide on pair programming:

- it will not be effective if you argue on styling conventions
- don't let it turn into watching - person without the keyboard should be an active participant
- sometimes it is better to discuss something on the whiteboard and then go programming solo
- rotate pairs
- match other's pace, the fast learner needs to slow down
- don't force people who don't like each other to pair
- no pairing between newbies

Nice idea: for discussing the design everyone should come with a prepared list of potential issues. It is good to assign perspectives - maintainer, coder, user, designer. Author in such discussion should play minor role, should only present the overview. Reviewer can be anyone outside author - tester, developer. Management should not be present at the meeting, however should be briefed with the results after the discussion. Design review can not be used for performance appraisals.  Group should be focused on identifying defects. Goal of this meeting is not to explore alternatives ar debate who is right and who is wrong. 

> NASA's Software Engineering Laboratory found that code reading detected about 3.3 defects per hour of effort. Testing detected 1.8 errors per hour.

#### Chapter 22: Developer Testing

> You must hope to find errors in your code. Such hope might seem like an unnatural act, but you should hope that it's you who who finds the errors and not someone else.

Why TDD:

- same effort to write test cases before and after
- you detect defects earlier and you can correct them more easily
- forces you to think a little bit about the requirements and design before writing code
- exposes requirements problems sooner

Developers tend to write *clean tests* rather than test for all the ways code breaks. Developer's testing isn't sufficient to provide adequate quality assurance. 

General Principle of Software Quality: improving quality improves the development schedule and reduces development cost.



