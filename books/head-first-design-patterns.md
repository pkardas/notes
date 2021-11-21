[go back](https://github.com/pkardas/learning)

# Head First Design Patterns: Building Extensible and Maintainable Object-Oriented Software

Book by Eric Freeman and Elisabeth Robson 

[TOC]

## Chapter 1: Welcome to Design Patterns

[The Strategy Pattern - Pattern implementation in Python](https://github.com/pkardas/learning/blob/master/books/head-first-design-patterns.py#L1)

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

We know using inheritance hasn't worked out very well. The `Flyable` and `Quackable` interfaces sounded good at first. There is a design principle:

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
Animal animal = new Dog();  // we knwo it is a Dog, but we can now use the animal reference polymorphically
animal.makeSound();
```

*Using our new design, what would you do if you needed to add rocker-powered flying to the SimUDuck app?*

- My answer: Add a new implementation of the `FlyBehaviour`

*Can you think of a class that might want to use the Quack behaviour that isn't a duck?*

- My answer: Russian quacking machine

A Duck will now delegate its flying and quacking behaviours, instead of using quacking and flying methods defined in the Duck class. To change a duck's behaviour at runtime, just call the duck's setter method for that behaviour. 

Design principle:

> Favour composition over inheritance.

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

[The Observer Pattern - Pattern implementation in Python](https://github.com/pkardas/learning/blob/master/books/head-first-design-patterns.py#L67)

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

- Identify the aspects of your application that vary and separate them from what stays the same: Observers and data vary.
- Program to an interface, not an implementation: Subject and Observers are loosely coupled because whet they know about each other are the interfaces they implement.
- Favour composition over inheritance: Subject holds a list of observers, observers hold a reference to the subject.

## Chapter 3: Decorating Objects

[The Decorator Pattern - Pattern implementation in Python](https://github.com/pkardas/learning/blob/master/books/head-first-design-patterns.py#L153[)

We will re-examine the typical overuse of inheritance and we will learn how to decorate classes at runtime using a form of object composition. 

Starbuzz system has created a maintenance nightmare for themselves. They are violating "*Identify the aspects of your application that vary and separate them from what stays the same" and "*Favour composition over inheritance*".

Problems with the suggested design:

- My answer: What if customer has promo coupon e.g -20%. What if condiment is not available.

If I can extend an objects behaviour through composition, then I can do this dynamically at runtime. When I inherit by subclassing that behaviour is set statically at compile time. By dynamically composing objects, I can add new functionality by writing new code, rather than altering existing code. Because I am not changing existing code, the changes of introducing bugs or causing unintended side effects in pre-existing code are much reduced. Code should be closed to change, yet open to extension.

Design principle - one of the mist important design principles:

> Classes should be open for extension, but closed for modification.

OPEN - if needs or requirements change, just go and make your own extensions. CLOSED - we spent a lot of time getting this code correct and bug free, so we can't let you alter the existing code. It must remain closed to modification.

Our goal is to allow classes to be easily extended to incorporate new behaviour without modifying existing code. Designs that are resilient to change and flexible enough to take on new functionality to meet changing requirements. Eg. The Observer Pattern - we can add new Observers and extend the Subject at any time.

Many of the patterns give us time-tested designs that protect your code from being modified by supplying a means of extension. 

How can I make every part of my design follow the Open-Closed Principle? Usually you can't. Making OO design flexible and open to extension without modifying existing code takes time and effort. 

Applying the Open-Closed principle EVERYWHERE is wasteful and unnecessary, and can lead to complex, hard-to-understand code. 

The Decorator Pattern:

> Attaches additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality.

The decorator adds its own behaviour before and / or after delegating to the object it decorates to do the rest of the job.

Just because we are subclassing, it doesn't mean we use inheritance. Sometimes we are subclassing in order to have the correct type, not to inherit the behaviour. We can acquire new behaviour not by inheriting it from a superclass, but by composing objects together.

Decorators are typically created using other patterns like Factory and Builder.

`java.io` is largely based on Decorator. Java I/O also points out one of the downsides of the Decorator Pattern: designs using this pattern often result in a large number of small classes, that can be overwhelming to the developer trying to use the Decorator-based API. 

Bullet points:

- Inheritance is one form of extension, but not necessarily the best way to achieve flexibility in our designs.
- In our designs we should allow behaviour to be extended without the need to modify existing code.
- Composition and delegation is often used to add new behaviours at runtime.
- The Decorator Pattern an alternative to subclassing for extending behaviour. 
- The Decorator Pattern involves a set of decorator patterns that are used to wrap concrete components.
- Decorator classes mirror the type of the components they decorate (in fact they are the same type as the components they decorate, either through inheritance or interface implementation).
- Decorators change the behaviour of their components by adding new functionality before and / or after method calls to the component.
- You can wrap a component with any number of decorators.
- Decorators are typically transparent to the client of the component - that is, unless the client is relying on the component's concrete type.
- Decorators can result in many small objects in our design, and overuse can be complex.

## Chapter 4: Baking with OO Goodness

The Factory Pattern - Pattern implementation in Python

There is more to making objects than just using the *new* operator. We will learn that instantiation is an activity that shouldn't always be done in public and can often lead to coupling problems. The Factory Pattern can save us from embarrassing dependencies.

We should not program to an implementation, but every time we use *new* that is exactly what we do. The *new* operator instantiating a concrete class, so that is definitely an implementation not an interface.

CHANGE impacts our use of *new*. Code will have to be changed new concrete classes are added. 

*How might you take all the parts of your application that instantiate concrete classes and separate or encapsulate them from the rest of your application?*

- My answer: I would add a function returning instantiated classes.

Indeed we can encapsulate object creation, we can take the creation code and move it into another object that is only going to be concerned with creating pizzas. Anytime it needs pizza, it asks the pizza factory to make one. By encapsulating object creation in one class, we have only one place to make modifications when the implementation changes. Simple object factory can be a static function, however it has the disadvantage that we can not subclass and change behaviour of the create method.

The Simple Factory isn't actually a Design Pattern, it is more of a programming idiom. Some developers do mistake this idiom for the Factory Pattern. 

A *factory method* handles object creation and encapsulates it in a subclass. This decouples the client code (eg. `orderPizza`) in the superclass from the object creation code in the subclass.

```java
public abstract class PizzaStore {
  public Pizza orderPizza(String type) {
    Pizza pizza;
    
    pizza = createPizza(type);
    
    pizza.prepare();
    pizza.bake();
    pizza.cut();
    pizza.box();
    
    return pizza;
  } 
  
  protected abstract Pizza createPizza(String type);
}
```

All factory patterns encapsulate object creation. The Factory Method Pattern encapsulates object creation by letting subclasses decide what objects to create. For every concrete Creator, there is typically a whole set of products that it creates. Chicago pizza creators create different types of Chicago-style pizza, New York pizza creators create different types of New York-style pizza, and so on.

The Factory Method Pattern:

> Defines an interface for creating an object, but lets subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses.

Creator is written to operate on products produced by the factory method. The Creator class is written without knowledge of the ac dual products that will be created. Only subclasses actually implement the factory method and create products.

When you directly instantiate an object, you are depending on its concrete class. Reducing dependencies to concrete classes in our code is a "good thing". General Principle - Dependency Inversion Principle:

> Depend upon abstractions. Do not depend upon concrete class.

It suggests that our high-level components should not depend on out low-level components, rather, they should both depend on abstractions. 

The "inversion" in the name Dependency Inversion Principle is there because it inverts they way you typically might think about your OO design. Low-level components now depend on higher-level abstraction.

Guidelines that can help to avoid OO designs that violate the Dependency Inversion Principle:

- No variable should hold a reference to a concrete class (if you use new, you will be holding a reference, use factory instead)
- No class should derive from a concrete class (If you derive, you depend, derive from an abstraction)
- No method should override an implemented method of any of its base classes (if you override an implemented method, your base wasn't really an abstraction to start with)

This is a guideline you should strive for, rather than a rule you should follow all the time. Clearly, every single Java program ever written violates these guidelines. But if you internalise these guidelines and have them in the back of your mind when you design, you will know when you are violating the principle and you will have a good reason for doing so.

An Abstract Factory gives un an interface for creating a family of products. By writing code that uses this interface, we decouple our code from actual factory that creates the products. That allows us to implement a variety of factories that produce products meant for different contexts - such as different regions, operating systems of different look and feels. Because code is decouples from the actual products, we can substitute different factories to get different behaviours. 

The Abstract Factory Pattern:

> Provides an interface for creating families of related or dependent objects without specifying their concrete classes.

Often the methods of an Abstract Factory are implemented as factory methods.

The Factory Method and The Abstract Factory are both good at decoupling applications from specific implementations. 

- Use Abstract Factory whenever you have families of products you need to create and you need to make sure your clients create products that belong together. Abstract Factory creates objects through object composition.
- Use Factory Methods to decouple client code from the concrete classes you need to instantiate, or if you don't know ahead of time all the concrete classes you are going to need. Factory Method creates objects through inheritance.

Bullet points:

- All factories encapsulate object creation.
- Simple Factory, while not a bona fide design pattern, is a simple way to decouple your clients from concrete classes.
- Factory Method relies on inheritance: object creation is delegated to subclasses, which implement the factory method to create objects.
- Abstract Factory relies on object composition: object creation is implemented in methods exposed in the factory interface.
- All factory patterns promote loose coupling by reducing the dependency of your application on concrete classes.
- The intent of Factory Method is to allow a class to defer instantiation to its subclasses.
- The intent of Abstract Factory is to create families of related objects without having to depend on their concrete classes.
- The Dependency Inversion Principle guides us to avoid dependencies on concrete types and to strive for abstractions.
- Factories are powerful technique for coding to abstractions, not concrete classes.
