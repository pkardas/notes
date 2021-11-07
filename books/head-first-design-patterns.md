[go back](https://github.com/pkardas/learning)

# Head First Design Patterns: Building Extensible and Maintainable Object-Oriented Software

Book by Eric Freeman and Elisabeth Robson 

[TOC]

## Chapter 1: Welcome to Design Patterns

Someone has already solved your problems. You can exploit the wisdom and lessons learned by other developers who have been down the same design problems road and survived the trip. Instead of code reuse, with patterns you get experience reuse. 

Example with ducks, adding `fly` method to the `Duck` superclass turned out to introduce a bug to the `RubberDuck` subclass. A localised update to the code caused a non-local side-effect (flying rubber-duck).

*Which of the following are disadvantages of using inheritance to provide Duck behaviour?* 

- My answer: [D] It is hard to gain knowledge of all duck behaviours. [F] Changes can unintentionally affect other ducks. 

*What do YOU think about the design? What would you do if you were Joe?*

- My answer: New features would require adding many interfaces, for example: interface for migrating birds. Maybe instead, it would be better to have 2 types of ducks: Living and non-living and instead of introducing a single class per duck, reuse classes and make them parametrised with a name. 

There is one constant in software development. What is the one thing you can always count on in software development. **CHANGE**.No matter how well you design an application, over time an application must grow and change or it will die.

*List some reasons you have had to change code in your application*:

- New definition of the operations process.
- Better understanding of the domain.
- Requirement to use worker instead of lambda.
- New library for the JSON serialisation.

We know using inheritance hasn't;t worked out very well. The `Flyable` and `Quackable` interfaces sounded good at first. There is a design principle:

> Identify the aspects of your application that vary and separate them from what stays the same.

Another way to thing about this principle: *take the parts that vary and encapsulate them, so that later you can alter or extend the parts that vary without affecting those that don't*.

We know that `fly` and `quack` are the parts of the Duck class that vary across ducks. We pull these methods out of the Duck class and create a new set of classes to represent each behaviour (FlyBehaviour, QuackBehaviour, ...). That way, the Duck classes won't need to know any of the implementation details for their own behaviours. 

> Program to an interface, not an implementation. == Program to a supertype.

Programming to an implementation:

```java
Dog d = new Dog();  // a concrete implementation of Anumal 
d.back()
```

Programming to an interface/supertype:

```java
Animal anumal = new Dog();  // we knwo it is a Dog, but we can now use the animal reference polymorphically
animal. makeSound;
```
