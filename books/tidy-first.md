[go back](https://github.com/pkardas/learning)

# Tidy First?

Book by Kent Beck

- [1. Guard Classes](#1-guard-classes)
- [2. Dead code](#2-dead-code)
- [3. Normalize symmetries](#3-normalize-symmetries)
- [4. New Interface, Old implementation](#4-new-interface-old-implementation)
- [5. Reading Order](#5-reading-order)
- [6. Cohesion Order](#6-cohesion-order)
- [7. Move Declaration and Initialization Together](#7-move-declaration-and-initialization-together)
- [8. Explaining variables](#8-explaining-variables)
- [9. Explaining constants](#9-explaining-constants)
- [10. Explicit parameters](#10-explicit-parameters)
- [11. Chunk statements](#11-chunk-statements)
- [12. Extract helper](#12-extract-helper)
- [13. One pile](#13-one-pile)
- [14. Explaining comments](#14-explaining-comments)
- [15. Delete redundant comments](#15-delete-redundant-comments)
- [16. Separate Tidying](#16-separate-tidying)
- [17. Chaining](#17-chaining)
- [17. Chaining](#18-batch-sizes)
- [18. Batch Sizes](#18-batch-sizes)
- [19. Rhythm](#19-rhythm)
- [20. Getting Untangled](#20-getting-untangled)
- [21. First, After, Later, Never](#21-first-after-later-never)

## 1. Guard Classes

If you see code like:

```
if condition: ...
```

or

```
if condition:
    if another condition: ...
```

tidy the above to:

```
if not condition: return
if not another condition: return
...
```

Exit immediately, it is easier to read -- before we get into the details, there are some preconditions we need to bear
in mind.

https://github.com/Bogdanp/dramatiq/pull/470

## 2. Dead code

Delete it. If you need it later, use version control. Delete only a little code in each tidying diff. Just in case, if
it turns out that you were wrong, it will be easy to rever the change.

## 3. Normalize symmetries

Tidy forms of unnecessary variations. Use common style for your functions. Things get confusing when two or more
patterns are used interchangeably.

## 4. New Interface, Old implementation

If some interface you need to use is very difficult to use, implement the interface you wish you could call and call it.
Implement the interface by simply calling the old one.

## 5. Reading Order

Reorder the code in the file in the order in which a reader would prefer to encounter it.

## 6. Cohesion Order

If 2 functions are coupled, put them next to each other, if 2 files are coupled, put them in the same directory, ...

If you know how to eliminate coupling, go for it.

## 7. Move Declaration and Initialization Together

It is easier to understand the code if each of the variables is declared and initialized just before it's used. It is
hard to read when declaration is separated from initialization.

## 8. Explaining variables

When you understand a part of a big, hairy expression, extract the subexpression into a variable named after the
intention of the expression.

Always separate the tidying commit from the behaviour change commit.

## 9. Explaining constants

Create a symbolic constant. Replace uses of the literal constant with the symbol.

## 10. Explicit parameters

It's common to see blocks of parameters passed in a map. This makes it hard to read and understand what data it
required. Make the parameters explicit:

```
foo(params) -> foo(a, b)
```

## 11. Chunk statements

The simplest tidying. Put a blank line between 2 parts doing different things. After you've chunked statements, you have
many paths forward: Explaining Variables, Extract Helper or Explaining Comments.

## 12. Extract helper

A block of code that has an obvious purpose and limited interaction with the rest of the code can be extracted into a
helper function. Using the helper can be taken care of in another tidying.

## 13. One pile

Sometimes you read the code that has been split into many tine pieces, which makes it hard to understand. The biggest
cost of code is the cost of reading it, not the cost of writing it.

Sometimes in order to regain the clarity, the code must be merged together, so new, easier-to-understand parts can be
extracted.

## 14. Explaining comments

Write down only what wasn't obvious from the code. Put yourself in the place of the future reader, or yourself 15
minutes ago.

Immediately upon finding a defect is a good time to comment. It is much better to add the comment that points out the
issue, rather than leaving it buried in the sand.

## 15. Delete redundant comments

When you see a comment that says exactly what the code says, remove it.

## 16. Separate Tidying

Tidying should go into their own separate PRs, with as few tidyings per PR as possible. Behavior and structure changes
should be in separate PRs.

## 17. Chaining

Tidying can set up another tidyings. You will begin to flow tidyings together to achieve larger changes to the
structure of your code. Be wary of changing too much, too fast. A failed tidying is expensive relative to the cost of a
series of successful tidyings.

## 18. Batch Sizes

The more tidyings per batch, the longer the delay before integrating, and the greater the chance that a tidying collides
with someone else is doing.

The change of a batch accidentally changing behavior rises with the number of tidyings in the batch.

The more tidyings per batch, the more we are prone to tidying just because, with all the additional costs that creates.

In many orgs, the fixed cost of getting a single change through review and deployment is substantial. Programmers feel
this cost, so they move right in the trade-off space (despite collisions, interactions, ...).

## 19. Rhythm

More than an hour of tidying at a time before making a behavioral change likely means you've lost track of the minimum
set of structure changes needed to enable your desired behavior change.

Tidying is a minutes-to-an-hour kind of activity. Sometimes it may take longer, but not for long.

## 20. Getting Untangled

Tidying leads to more and more tidying. What to do? 3 options:

1. Ship as it is [very impolite, prone to errors, but quick]
2. Untangle the tidyings into separate PRs [more polite, but may require a lot of work]
3. Start over, tidying first [more work, but leaves a coherent chain of commits]

Re-implementation raises the possibility that you will see something new as you re-implement, letting you squeeze more
value out of the same set of behavioral changes.

## 21. First, After, Later, Never

**Never**

- you are never changing this code again
- there is nothing to learn by improving the design

**Later**

- you have a big batch of tidying to do without immediate payoff
- there is eventual payoff for completing the tidying
- you can tidy in little batches

**After**

- waiting until next time to tidy first will be more expensive
- you won't feel a sense of completion if you don't tidy after

**First**

- it will pay off immediately, either in improved comprehension or in cheaper behavior changes
- you know what to tidy and how
