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
Dog d = new Dog();  // a concrete implementation of Animal 
d.bark()
```

Programming to an interface/supertype:

```java
Animal anumal = new Dog();  // we knwo it is a Dog, but we can now use the animal reference polymorphically
animal.makeSound();
```

*Using our new design, what would you do if you needed to add rocker-powered flying to the SimUDuck app?*

- My answer: Add a new implementation of the `FlyBehaviour`

*Can you think of a class that might want to use the Quack behaviour that isn't a duck?*

- My answer: Russian quacking machine

A Duck will now delegate its flying and quacking behaviours, instead of using quacking and flying methods defined in the Duck class. To change a duck's behaviour at runtime, just call the duck's setter method for that behaviour. 

Design principle:

> Factor composition over inheritance.

Creating systems using composition gives you a lot more flexibility. Not only does it let you encapsulate a family of algorithms into their own set of classes, but it also lets you change behaviour at runtime. Composition Is used in many design patterns and you will see a lot more about its advantages and disadvantages throughout the book.

*A duck call is a device that hunters use to mimic the calls (quacks) of ducks. How would you implement your own duck call that does not inherit from the Duck class?*

-  My answer: Compose a duck call of `QuackBehaviour`.

I have just applied the **STRATEGY** pattern. **The Strategy Pattern** - defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently from clients that use it.

Design puzzle:

- *KnifeBehaviour, BowAndArrowBehaviour, AxeBehaviour, SwordBehaviour* IMPLEMENT *WeaponBehaviour* 
- *Troll, Queen, King, Knight* EXTENDS *Character*
- *Character* HAS-A *WeaponBehaviour*
- `setWeapon` should be in *Character* class

Design Patterns give you a shared vocabulary with other developers. Once you have got the vocabulary, you can more easily communicate with other developers and inspire those who don't know patterns to start learning them. It also elevates your thinking about architectures by letting you think at the pattern level, not the nitty-gritty object level.

The power of a shared pattern vocabulary:

- Shared pattern vocabularies are POWERFUL. When you communicate with another developer using patterns, you are communicating not just a pattern name but a whole set of qualities, characteristics and constraints that the pattern represents.
- Patterns allow you to say more with less. Other developers can quickly know precisely the design you have in mind.
- Talking at the pattern level allows you to stay *in the design* loner, without having to dive deep down to the nitty-gritty details of implementing objects and classes.
- Shared vocabularies can turbo-charge your team. A team well versed in design patterns can move quickly with less room for misunderstanding.
- Shared vocabularies encourage more junior developers to get up to speed.

Design patterns don't go directly into your code, they first go into your **brain**. Once you have loaded your brain with a good working knowledge of patterns, you can then start to apply them to new designs, and rework your old code when you find it is degrading into inflexible mess.

OO Basics: Abstraction, Encapsulation, Polymorphism, Inheritance

OO Principles: Encapsulate what varies. Favour composition over inheritance. Program to interfaces, not implementations.

Bullet points:

- Knowing the OO basics does not make you a good OO designer.
- Good OO designs are reusable, extensible and maintainable.
- Patterns show you how to build systems with good OO design qualities.
- Patterns are proven OO experience.
- Patterns don't give you code, they give you general solutions to design problems. You apply them to your specific application.
- Patterns aren't invented, they are discovered.
- Most patterns and principles address issues of change n software.
- Most patterns allow some part of a system to vary independently of all other parts.
- We often try to take what varies in a system and encapsulate it.
- Patterns provide language that can maximise the value of your communication with other developers.

## Chapter 2: Keeping your Objects in the Know

Observer Pattern: Pattern that keeps your objects in the know when something they care about happens.

Weather-O-Rama, our task is to create an app that uses the WeatherData object top update 3 displays for current conditions weather stats and a forecast.

*Based on our first implementation, which of the following apply?*

- My answers: [A] We are coding to concrete implementations, not interfaces. [B] For every new display we will need to alter this code. [C] We have no way to add or remove display elements at runtime. [E] We haven't encapsulated the part that changes.

You know how newspaper or magazine subscriptions work:

1. A newspaper publisher goes into business and begins publishing newspapers
2. You subscribe to a particular publisher, and every time there is a new edition it gets delivered to you. As long as you remain a subscriber, you get new newspapers.
3. You unsubscribe when you don't want papers anymore, and they stop being delivered.
4. While the publisher remains in business, people, hotels, airlines and other businesses constantly subscribe and unsubscribe to the newspaper.

> Publishers + Subscribers = Observer Pattern

The Observer Pattern:

> Defines a one-to-many dependency between objects so that when one object changes state, all of its dependencies are notified and updated automatically.

There are few different ways to implement the Observer Pattern, but most revolve around a class design that includes Subject and Observer interfaces.

Because the subject is the sole owner of the data, the observers are dependent on the subject to update them when the data changes. This leads to a cleaner OO design than allowing many objects to control the same data.

**We say an object is tightly coupled to another object when it is too dependant on that object.** Loosely coupled object doesn't know or care too much about the details of another object. By not knowing too much about other objects, we can create designs that can handle change better.  The Observer Pattern is a great example of loose coupling.

The ways the pattern achieves loose coupling:

1. The only thing the subject knows about an observer is that is implements a certain interface.
2. We can add new observers at any time.
3. We never need to modify the subject to add new types of observers.
4. We can reuse subjects or observers independently of each other.
5. Changes to either the subject or an observer will not affect the other.

Design principle:

> Strive for loosely coupled designs between objects that interact.

Loosely coupled designs allow us to build flexible systems that can handle change because the minimise the interdependency between objects.

The Observer Pattern is one of the most common patterns in use, and you will find plenty of examples of the pattern being used in many libraries and frameworks (Swing, JavaBeans, Cocoa, ...). Listener == Observer Pattern.

The Observer Pattern can be used for sending "notifications" so that observers can pull the data on their own.

Bullet points:

- The Observer Pattern defines a now-to-many relationship between objects.
- Subjects update Observers using a common interface.
- Observers of any concrete type can participate in the pattern as long they implement the Observer interface.
- Observers are loosely coupled in that the Subject knows nothing about them, other than that they implement the Observer interface.
- You can push or pull data from the Subject when using the pattern (pull is considered more correct).
- Swing makes heavy use of the Observer Pattern, as do many GUI frameworks.
- You will also find the pattern in many other places including RxJava, JavaBeans and RMI, as well as in other language frameworks, like Cocoa, Swift and JavaScript events.
- The Observer Pattern is related to the Publish / Subscribe Pattern, which is for more complex situations with multiple Subjects and or / multiple message types.
- The Observer Pattern is a commonly used pattern, and we will see it again when we learn about Model-View-Controller.

*For each design principle, describe how the Observer Pattern makes use of the principle:*

- Identify the aspects fo your application that vary and separate them from what stays the same: Observers and data vary.
- Program to an interface, not an implementation: Subject and Observers are loosely coupled because whet they know about each other are the interfaces they implement.
- Favour composition over inheritance: Subject holds a list of observers, observers hold a reference to the subject.
