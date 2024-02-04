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
