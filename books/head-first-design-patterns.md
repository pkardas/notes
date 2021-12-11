~~[go back](https://github.com/pkardas/learning)

# Head First Design Patterns: Building Extensible and Maintainable Object-Oriented Software

Book by Eric Freeman and Elisabeth Robson

- [Chapter 1: The Strategy Pattern - Welcome to Design Patterns](#chapter-1-welcome-to-design-patterns)
- [Chapter 2: The Observer Pattern - Keeping your Objects in the Know](#chapter-2-keeping-your-objects-in-the-know)
- [Chapter 3: The Decorator Pattern - Decorating Objects](#chapter-3-decorating-objects)
- [Chapter 4: The Factory Pattern - Baking with OO Goodness](#chapter-4-baking-with-oo-goodness)
- [Chapter 5: The Singleton Pattern - One-of-a-kind Objects](#chapter-5-one-of-a-kind-objects)
- [Chapter 6: The Command Pattern - Encapsulating Invocation](#chapter-6-encapsulating-invocation)
- [Chapter 7: The Adapter and Facade Patterns - Being Adaptive](#chapter-7-being-adaptive)
- [Chapter 8: The Template Method Pattern - Encapsulating Algorithms](#chapter-8-encapsulating-algorithms)

## Chapter 1: Welcome to Design Patterns

[The Strategy Pattern - Pattern implementation in Python](https://github.com/pkardas/learning/blob/master/books/head-first-design-patterns.py#L1)

Someone has already solved your problems. You can exploit the wisdom and lessons learned by other developers who have
been down the same design problems road and survived the trip. Instead of code reuse, with patterns you get experience
reuse.

Example with ducks, adding `fly` method to the `Duck` superclass turned out to introduce a bug to the `RubberDuck`
subclass. A localised update to the code caused a non-local side effect (flying rubber-duck).

*Which of the following are disadvantages of using inheritance to provide Duck behaviour?*

- My answer: [D] It is hard to gain knowledge of all duck behaviours. [F] Changes can unintentionally affect other
  ducks.

*What do YOU think about the design? What would you do if you were Joe?*

- My answer: New features would require adding many interfaces, for example: interface for migrating birds. Maybe
  instead, it would be better to have 2 types of ducks: Living and non-living and instead of introducing a single class
  per duck, reuse classes and make them parametrised with a name.

There is one constant in software development. What is the one thing you can always count on in software development. **
CHANGE**.No matter how well you design an application, over time an application must grow and change, or it will die.

*List some reasons you have had to change code in your application*:

- New definition of the operations process.
- Better understanding of the domain.
- Requirement to use worker instead of lambda.
- New library for the JSON serialisation.

We know using inheritance hasn't worked out very well. The `Flyable` and `Quackable` interfaces sounded good at first.
There is a design principle:

> Identify the aspects of your application that vary and separate them from what stays the same.

Another way to think about this principle: *take the parts that vary and encapsulate them, so that later you can alter
or extend the parts that vary without affecting those that don't*.

We know that `fly` and `quack` are the parts of the Duck class that vary across ducks. We pull these methods out of the
Duck class and create a new set of classes to represent each behaviour (FlyBehaviour, QuackBehaviour, ...). That way,
the Duck classes won't need to know any of the implementation details for their own behaviours.

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

A Duck will now delegate its flying and quacking behaviours, instead of using quacking and flying methods defined in the
Duck class. To change a duck's behaviour at runtime, just call the duck's setter method for that behaviour.

Design principle:

> Favour composition over inheritance.

Creating systems using composition gives you a lot more flexibility. Not only does it let you encapsulate a family of
algorithms into their own set of classes, but it also lets you change behaviour at runtime. Composition Is used in many
design patterns, and you will see a lot more about its advantages and disadvantages throughout the book.

*A duck call is a device that hunters use to mimic the calls (quacks) of ducks. How would you implement your own duck
call that does not inherit from the Duck class?*

- My answer: Compose a duck call of `QuackBehaviour`.

I have just applied the **STRATEGY** pattern. **The Strategy Pattern** - defines a family of algorithms, encapsulates
each one, and makes them interchangeable. Strategy lets the algorithm vary independently of clients that use it.

Design puzzle:

- *KnifeBehaviour, BowAndArrowBehaviour, AxeBehaviour, SwordBehaviour* IMPLEMENT *WeaponBehaviour*
- *Troll, Queen, King, Knight* EXTENDS *Character*
- *Character* HAS-A *WeaponBehaviour*
- `setWeapon` should be in *Character* class

Design Patterns give you a shared vocabulary with other developers. Once you have got the vocabulary, you can more
easily communicate with other developers and inspire those who don't know patterns to start learning them. It also
elevates your thinking about architectures by letting you think at the pattern level, not the nitty-gritty object level.

The power of a shared pattern vocabulary:

- Shared pattern vocabularies are POWERFUL. When you communicate with another developer using patterns, you are
  communicating not just a pattern name but a whole set of qualities, characteristics and constraints that the pattern
  represents.
- Patterns allow you to say more with less. Other developers can quickly know precisely the design you have in mind.
- Talking at the pattern level allows you to stay *in the design* loner, without having to dive deep down to the
  nitty-gritty details of implementing objects and classes.
- Shared vocabularies can turbo-charge your team. A team well versed in design patterns can move quickly with less room
  for misunderstanding.
- Shared vocabularies encourage more junior developers to get up to speed.

Design patterns don't go directly into your code, they first go into your **brain**. Once you have loaded your brain
with a good working knowledge of patterns, you can then start to apply them to new designs, and rework your old code
when you find it is degrading into inflexible mess.

OO Basics: Abstraction, Encapsulation, Polymorphism, Inheritance

OO Principles: Encapsulate what varies. Favour composition over inheritance. Program to interfaces, not implementations.

Bullet points:

- Knowing the OO basics does not make you a good OO designer.
- Good OO designs are reusable, extensible and maintainable.
- Patterns show you how to build systems with good OO design qualities.
- Patterns are proven OO experience.
- Patterns don't give you code, they give you general solutions to design problems. You apply them to your specific
  application.
- Patterns aren't invented, they are discovered.
- Most patterns and principles address issues of change n software.
- Most patterns allow some part of a system to vary independently of all other parts.
- We often try to take what varies in a system and encapsulate it.
- Patterns provide language that can maximise the value of your communication with other developers.

## Chapter 2: Keeping your Objects in the Know

[The Observer Pattern - Pattern implementation in Python](https://github.com/pkardas/learning/blob/master/books/head-first-design-patterns.py#L67)

Observer Pattern: Pattern that keeps your objects in the know when something they care about happens.

Weather-O-Rama, our task is to create an app that uses the WeatherData object top update 3 displays for current
conditions weather stats and a forecast.

*Based on our first implementation, which of the following apply?*

- My answers: [A] We are coding to concrete implementations, not interfaces. [B] For every new display we will need to
  alter this code. [C] We have no way to add or remove display elements at runtime. [E] We haven't encapsulated the part
  that changes.

You know how newspaper or magazine subscriptions work:

1. A newspaper publisher goes into business and begins publishing newspapers
2. You subscribe to a particular publisher, and every time there is a new edition it gets delivered to you. As long as
   you remain a subscriber, you get new newspapers.
3. You unsubscribe when you don't want papers anymore, and they stop being delivered.
4. While the publisher remains in business, people, hotels, airlines and other businesses constantly subscribe and
   unsubscribe to the newspaper.

> Publishers + Subscribers = Observer Pattern

The Observer Pattern:

> Defines a one-to-many dependency between objects so that when one object changes state, all of its dependencies are
> notified and updated automatically.

There are few different ways to implement the Observer Pattern, but most revolve around a class design that includes
Subject and Observer interfaces.

Because the subject is the sole owner of the data, the observers are dependent on the subject to update them when the
data changes. This leads to a cleaner OO design than allowing many objects to control the same data.

**We say an object is tightly coupled to another object when it is too dependent on that object.** Loosely coupled
object doesn't know or care too much about the details of another object. By not knowing too much about other objects,
we can create designs that can handle change better. The Observer Pattern is a great example of loose coupling.

The ways the pattern achieves loose coupling:

1. The only thing the subject knows about an observer is that is implements a certain interface.
2. We can add new observers at any time.
3. We never need to modify the subject to add new types of observers.
4. We can reuse subjects or observers independently of each other.
5. Changes to either the subject or an observer will not affect the other.

Design principle:

> Strive for loosely coupled designs between objects that interact.

Loosely coupled designs allow us to build flexible systems that can handle change because they minimise the
interdependency between objects.

The Observer Pattern is one of the most common patterns in use, and you will find plenty of examples of the pattern
being used in many libraries and frameworks (Swing, JavaBeans, Cocoa, ...). Listener == Observer Pattern.

The Observer Pattern can be used for sending "notifications" so that observers can pull the data on their own.

Bullet points:

- The Observer Pattern defines a now-to-many relationship between objects.
- Subjects update Observers using a common interface.
- Observers of any concrete type can participate in the pattern as long they implement the Observer interface.
- Observers are loosely coupled in that the Subject knows nothing about them, other than that they implement the
  Observer interface.
- You can push or pull data from the Subject when using the pattern (pull is considered more correct).
- Swing makes heavy use of the Observer Pattern, as do many GUI frameworks.
- You will also find the pattern in many other places including RxJava, JavaBeans and RMI, as well as in other language
  frameworks, like Cocoa, Swift and JavaScript events.
- The Observer Pattern is related to the Publish / Subscribe Pattern, which is for more complex situations with multiple
  Subjects and or / multiple message types.
- The Observer Pattern is a commonly used pattern, and we will see it again when we learn about Model-View-Controller.

*For each design principle, describe how the Observer Pattern makes use of the principle:*

- Identify the aspects of your application that vary and separate them from what stays the same: Observers and data
  vary.
- Program to an interface, not an implementation: Subject and Observers are loosely coupled because whet they know about
  each other are the interfaces they implement.
- Favour composition over inheritance: Subject holds a list of observers, observers hold a reference to the subject.

## Chapter 3: Decorating Objects

[The Decorator Pattern - Pattern implementation in Python](https://github.com/pkardas/learning/blob/master/books/head-first-design-patterns.py#L153[)

We will re-examine the typical overuse of inheritance, and we will learn how to decorate classes at runtime using a form
of object composition.

Starbuzz system has created a maintenance nightmare for themselves. They are violating "*Identify the aspects of your
application that vary and separate them from what stays the same" and "*Favour composition over inheritance*".

Problems with the suggested design:

- My answer: What if customer has promo coupon e.g -20%. What if condiment is not available.

If I can extend an objects' behaviour through composition, then I can do this dynamically at runtime. When I inherit by
subclassing that behaviour is set statically at compile time. By dynamically composing objects, I can add new
functionality by writing new code, rather than altering existing code. Because I am not changing existing code, the
changes of introducing bugs or causing unintended side effects in pre-existing code are much reduced. Code should be
closed to change, yet open to extension.

Design principle - one of the mist important design principles:

> Classes should be open for extension, but closed for modification.

OPEN - if it needs or requirements change, just go and make your own extensions. CLOSED - we spent a lot of time getting
this code correct and bug free, so we can't let you alter the existing code. It must remain closed to modification.

Our goal is to allow classes to be easily extended to incorporate new behaviour without modifying existing code. Designs
that are resilient to change and flexible enough to take on new functionality to meet changing requirements. E.g. The
Observer Pattern - we can add new Observers and extend the Subject at any time.

Many of the patterns give us time-tested designs that protect your code from being modified by supplying a means of
extension.

How can I make every part of my design follow the Open-Closed Principle? Usually you can't. Making OO design flexible
and open to extension without modifying existing code takes time and effort.

Applying the Open-Closed principle EVERYWHERE is wasteful and unnecessary, and can lead to complex, hard-to-understand
code.

The Decorator Pattern:

> Attaches additional responsibilities to an object dynamically. Decorators provide a flexible alternative to
> subclassing for extending functionality.

The decorator adds its own behaviour before and / or after delegating to the object it decorates to do the rest of the
job.

Just because we are subclassing, it doesn't mean we use inheritance. Sometimes we are subclassing in order to have the
correct type, not to inherit the behaviour. We can acquire new behaviour not by inheriting it from a superclass, but by
composing objects together.

Decorators are typically created using other patterns like Factory and Builder.

`java.io` is largely based on Decorator. Java I/O also points out one of the downsides of the Decorator Pattern: designs
using this pattern often result in a large number of small classes, that can be overwhelming to the developer trying to
use the Decorator-based API.

Bullet points:

- Inheritance is one form of extension, but not necessarily the best way to achieve flexibility in our designs.
- In our designs we should allow behaviour to be extended without the need to modify existing code.
- Composition and delegation is often used to add new behaviours at runtime.
- The Decorator Pattern an alternative to subclassing for extending behaviour.
- The Decorator Pattern involves a set of decorator patterns that are used to wrap concrete components.
- Decorator classes mirror the type of the components they decorate (in fact they are the same type as the components
  they decorate, either through inheritance or interface implementation).
- Decorators change the behaviour of their components by adding new functionality before and / or after method calls to
  the component.
- You can wrap a component with any number of decorators.
- Decorators are typically transparent to the client of the component - that is, unless the client is relying on the
  component's concrete type.
- Decorators can result in many small objects in our design, and overuse can be complex.

## Chapter 4: Baking with OO Goodness

[The Factory Pattern - Pattern implementation in Python](https://github.com/pkardas/learning/blob/master/books/head-first-design-patterns.py#L209)

There is more to making objects than just using the *new* operator. We will learn that instantiation is an activity that
shouldn't always be done in public and can often lead to coupling problems. The Factory Pattern can save us from
embarrassing dependencies.

We should not program to an implementation, but every time we use *new* that is exactly what we do. The *new* operator
instantiating a concrete class, so that is definitely an implementation not an interface.

CHANGE impacts our use of *new*. Code will have to be changed new concrete classes are added.

*How might you take all the parts of your application that instantiate concrete classes and separate or encapsulate them
from the rest of your application?*

- My answer: I would add a function returning instantiated classes.

Indeed, we can encapsulate object creation, we can take the creation code and move it into another object that is only
going to be concerned with creating pizzas. Anytime it needs pizza, it asks the pizza factory to make one. By
encapsulating object creation in one class, we have only one place to make modifications when the implementation
changes. Simple object factory can be a static function, however it has the disadvantage that we can not subclass and
change behaviour of the create method.

The Simple Factory isn't actually a Design Pattern, it is more of a programming idiom. Some developers do mistake this
idiom for the Factory Pattern.

A *factory method* handles object creation and encapsulates it in a subclass. This decouples the client code (
e.g. `orderPizza`) in the superclass from the object creation code in the subclass.

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

All factory patterns encapsulate object creation. The Factory Method Pattern encapsulates object creation by letting
subclasses decide what objects to create. For every concrete Creator, there is typically a whole set of products that it
creates. Chicago pizza creators create different types of Chicago-style pizza, New York pizza creators create different
types of New York-style pizza, and so on.

The Factory Method Pattern:

> Defines an interface for creating an object, but lets subclasses decide which class to instantiate. Factory Method
> lets a class defer instantiation to subclasses.

Creator is written to operate on products produced by the factory method. The Creator class is written without knowledge
of the ac dual products that will be created. Only subclasses actually implement the factory method and create products.

When you directly instantiate an object, you are depending on its concrete class. Reducing dependencies to concrete
classes in our code is a "good thing". General Principle - Dependency Inversion Principle:

> Depend upon abstractions. Do not depend upon concrete class.

It suggests that our high-level components should not depend on out low-level components, rather, they should both
depend on abstractions.

The "inversion" in the name Dependency Inversion Principle is there because it inverts they way you typically might
think about your OO design. Low-level components now depend on higher-level abstraction.

Guidelines that can help to avoid OO designs that violate the Dependency Inversion Principle:

- No variable should hold a reference to a concrete class (if you use new, you will be holding a reference, use factory
  instead)
- No class should derive from a concrete class (If you derive, you depend, derive from an abstraction)
- No method should override an implemented method of its base classes (if you override an implemented method, your base
  wasn't really an abstraction to start with)

This is a guideline you should strive for, rather than a rule you should follow all the time. Clearly, every single Java
program ever written violates these guidelines. But if you internalise these guidelines and have them in the back of
your mind when you design, you will know when you are violating the principle, and you will have a good reason for doing
so.

An Abstract Factory gives un an interface for creating a family of products. By writing code that uses this interface,
we decouple our code from actual factory that creates the products. That allows us to implement a variety of factories
that produce products meant for different contexts - such as different regions, operating systems of different look and
feels. Because code is decouples from the actual products, we can substitute different factories to get different
behaviours.

The Abstract Factory Pattern:

> Provides an interface for creating families of related or dependent objects without specifying their concrete classes.

Often the methods of an Abstract Factory are implemented as factory methods.

The Factory Method and The Abstract Factory are both good at decoupling applications from specific implementations.

- Use Abstract Factory whenever you have families of products you need to create, and you need to make sure your clients
  create products that belong together. Abstract Factory creates objects through object composition.
- Use Factory Methods to decouple client code from the concrete classes you need to instantiate, or if you don't know
  ahead of time all the concrete classes you are going to need. Factory Method creates objects through inheritance.

Bullet points:

- All factories encapsulate object creation.
- Simple Factory, while not a bona fide design pattern, is a simple way to decouple your clients from concrete classes.
- Factory Method relies on inheritance: object creation is delegated to subclasses, which implement the factory method
  to create objects.
- Abstract Factory relies on object composition: object creation is implemented in methods exposed in the factory
  interface.
- All factory patterns promote loose coupling by reducing the dependency of your application on concrete classes.
- The intent of Factory Method is to allow a class to defer instantiation to its subclasses.
- The intent of Abstract Factory is to create families of related objects without having to depend on their concrete
  classes.
- The Dependency Inversion Principle guides us to avoid dependencies on concrete types and to strive for abstractions.
- Factories are powerful technique for coding to abstractions, not concrete classes.

## Chapter 5: One-of-a-kind Objects

[The Singleton Pattern - Pattern implementation in Python](https://github.com/pkardas/learning/blob/master/books/head-first-design-patterns.py#L418)

The ticket to creating one-of-a-kind objects for which there is only one instance, ever. By using singleton you can
ensure that every object in your application is making use of the same global resource. Often used to manage pools of
resources, like connection or thread pools.

_How might things go wrong if more than one instance of ChocolateBoiler is created in an application?_

- My answer: Incorrect state management, because of multiple instances.

The Singleton Pattern:

> Ensures a class has only one instance, and provides a global point of access to it.

Despite using the Singleton Pattern, multithreaded-application can still cause problems - instantiate multiple objects.
In Javan solution for this is to use `synchronized` keyword.

```java
public static synchronized Singleton getInstance() {
  ...
}
```

`synchronized` - forces every thread to wait fot its turn before it can enter the method. That is, no 2 threads may
enter the method at the same time. Synchronization may be expensive, but here it will be used only once
on `uniqueInstance` initialization. After the first time, synchronization is totally unneeded overhead. There are
Java-specific solutions to this overhead (e.g. double-check locking).

The Singleton Pattern violates "_the loose coupling principle_", if you make a change to the Singleton, you will likely
have to make a change to every object connected to it.

A global variable can provide a global access, but not ensure only one instance. Global variables also tend to encourage
developers to pollute the namespace with lots of global references to small objects. Singletons don't encourage this in
the same way, but can be abused nonetheless.

It is possible to implement Singleton as an enum.

Bullet points:

- The Singleton Pattern ensures you have at most one instance of a class in your application.
- The Singleton Pattern also provides a global access point to that interface.
- Java's implementation of the Singleton Pattern makes use of a private constructor, a static method combined with a
  static variable.
- Examine your performance and resource constraints and carefully choose an appropriate Singleton for multithreaded
  applications (we should consider all applications multithreaded).

## Chapter 6: Encapsulating Invocation

[The Command Pattern - Pattern implementation in Python](https://github.com/pkardas/learning/blob/master/books/head-first-design-patterns.py#L470)

In this chapter we are going to encapsulate method invocation. By encapsulating method invocation, we can crystallize
pieces of computation so that the object invoking the computation doesn't need to worry about how to do things, it just
uses our crystallized method to get it done.

The Command Pattern allows you to decouple the requester of an action from the object that actually performs the action.
This can be achieved by introducing command objects into the design. A command object encapsulates a request to do
something on a specific object.

Example with a waitress taking orders and passing them to a cook - separation of an object making a request from the
object that receive and execute requests.

- Customer - Client
- Order - Command
- Waitress - Invoker
- Short-Order Cook - Receiver
- takeOrder - setCommand - sets what is supposed to be executed
- orderUp - execute

The Command Pattern:

> Encapsulates a request as an object, thereby letting you parametrize other objects with different requests,
> queue or log requests, and support undoable operations.

A null object is useful when you don;t have a meaningful object tor eturn, and yet you want to remove the responsibility
of handling null from the client, e.g. `NoCommand` - surrogate and does nothing when its execute method is called.

Command Pattern can be taken into the next level by using e.g. Java's lambda expressions. Instead of instantiating the
concrete command objects, you can use function objects in their place. This can be done if Command interface has one
abstract method.

In order to support undoable Commands, `Command` interface has to be extended with `undo` method.

`MacroCommand` can be used to execute multiple commands:

```java
MacroCommand partyOnMacro = new MacroCommand({lightOn, stereoOn, tvOn, hottubOn});
```

More uses of the Command Pattern:

- queueing requests - objects implementing the command interface are added to the queue, threads remove commands from
  the queue on by one and call their `execute` method. Once complete, they go back for a new command object. This gives
  us an effective way to limit computation to a fixed number of threads.
- logging requests - semantics of some applications require that we log all actions and be able to recover after a crash
  by re-invoking those actions. The Command Pattern can support these semantics with the addition of two
  methods: `store` and `load`.

Bullet points:

- The Command Pattern decouples an object making a request from the one that knows how to perform it.
- A Command object is at the center of this decoupling and encapsulates a receiver with an action (or set of actions).
- An invoker makes a request of a Command object by calling its execute method, which invokes these actions on the
  receiver.
- Invokers can be parametrized with Commands, even dynamically at runtime.
- Commands may support undo by implementing an undo method that restores the object to its previous state before the
  execute method was last called.
- MacroCommands are a simple extension of the Command Pattern that allow multiple commands to be invoked. Likewise,
  MacroCommands can easily support undo.
- In practice, it is not uncommon for "smart" Command objects to implement the request themselves rather than delegating
  to a receiver.
- Commands may also be used to implement logging and transactional systems.

## Chapter 7: Being Adaptive

[The Adapter and Facade Patterns - Pattern implementation in Python](https://github.com/pkardas/learning/blob/master/books/head-first-design-patterns.py#L615)

We are going to wrap some objects with a different purpose: to make their interfaces look something they are not. So we
can adapt a design expecting one interface to a class that implements a different interface. Also, we are going to look
at another pattern that wraps objects to simplify their interface.

You will have no trouble understanding what an OO adapter is because the real world is full of them (e.g. power adapter,
The British wall outlet exposes on interface for getting power, the adapter converts one interface into another, the US
laptop expects another interface).

OO adapters play the same role as their real-world counterparts: they take an interface and adapt it to one that a
client ise expecting. For example: you are going to use a new library, but the new vendor designed their interfaces
differently than the last vendor.

The adapter acts as the middleman by receiving requests from the client and converting them into requests that make
sense on the vendor classes.

_If it walks like a duck and quacks like a duck, then it ~~must~~ might be a ~~duck~~ turkey wrapped with a duck
adapter..._

```java
public class TurkeyAdapter implements Duck {
  // take Turkey in the constuctor, implement Duck's method by invoking Turkey's methods.
}
```

How the Client uses the Adapter:

1. The client makes a request to the adapter by calling a method on it using the target interface.
2. The adapter translates the request into one or more calls on the adaptee using the adaptee interface.
3. The client receives the results of teh call and never knows there is an adapter doing the translation.

It is possible to create a Two Way Adapter, just implement both interfaces involved, so the adapter can act as an old
interface or a new interface.

The Adapter Pattern:

> Converts the interface of a class into another interface the client expects. Adapter lets classes work together that
> couldn't otherwise because of incompatible interfaces.

Adapter is used to decouple the client from the implemented interface,a nd if we expect the interface to change over
time, the adapter encapsulates that change that the client doesn't have to be modified each time it needs to operate
against a different interface.

The Adapter Pattern is full of good OO design principles: uses object composition + binds the client to an interface,
not an implementation.

There is second type of adapter - class adapter, this one uses multiple inheritance (Target and Adaptee).

Real-world adapters:

- [Java] Enumerators - The Enumerator interface allows you to step through the elements of a collection without knowing
  the specifics of how they are managed in the collection.
- [Java] Iterators - The more recent Collection classes use an Iterator interface, allows you to iterate through a set
  of items in a collection, and adds the ability to remove items.

When a method in an adapter can not be supported you can throw e.g. `UnsupportedOperationException`.

_Some AC adapters do mor ethan just change the interface - they add other features like surge protection, indicator
lights, and other bells and whistles. If you were going to implement these kinds of features, what pattern would you
use?_

- My answer: The Decorator Pattern

Decorator vs Adapter:

- Decorators allow new behavior to be added to classes without altering existing code.
- Adapter always convert the interface of what they wrap.

Decorators and Adapters seem to look somewhat similar on paper, but clearly are miles apart.

The Facade Pattern alters an interface, but in order to simplify the interface - it hides all the complexity of one or
more classes behind a clean well-lit facade. The Facade Pattern can take a complex subsystem and make it easier to use.

Example home cinema system: instead of turning on popcorn machine, screen and audio system - all you need to do is
call `watchMovie`.

Facades don't encapsulate the subsystem classes, they merely provide a simplified interface to their functionality. The
subsystem classes still remain available. It provides a simplified interface while still exposing the full functionality
of the system to those who may need it.

A facade not only simplifies an interface, it decouples a client from a subsystem of components.

Facades and adapters may wrap multiple classes, but a facade's intent is to simplify, while an adapter's is to convert
the interface to something different.

The Facade Pattern:

> Provides a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes
> the subsystem easier to use.

Design principle - Principle of Least Knowledge (The Law of Demeter):

> Talk only to your immediate friends.

This principle guides us to reduce the interactions between objects to just a few close "friends". It means when you are
designing a system, for any object, be careful of the number of classes it interacts with and also how it comes to
interact with those classes.

This principle prevents us from creating designs that have a large number of classes coupled together so that changes in
one part of the system cascade to other parts.

This means, invoke only methods that belong to:

- the object itself
- objects passed in as a parameter to the method
- any object the method creates or instantiates
- any components of the object

_Side note: Principle of Least Knowledge is a better name than The Law of Demeter, because no principle is a law, and
they don't have to be always applied._

The Facade Pattern and the Principle of Least Knowledge - we try to keep subsystems adhering to the Principle of Least
Knowledge as well. If this gets too complex and too many friends are intermingling, we can introduce additional facades
to form layers of subsystems.

Bullet points:

- When you need to use an existing class and its interface is not the one you need, use an adapter.
- When you need to simplify and unify a large interface or complex set of interfaces, use a facade.
- An adapter changes an interface into one a client expects.
- A facade decouples a client from a complex subsystem.
- Implementing an adapter may require little work or a great deal of work depending on the size and complexity of the
  target interface.
- Implementing a facade requires that we compose the facade with its subsystem and use delegation to perform the work of
  the facade.
- There are two forms of the Adapter pattern: object and class adapters. Class adapters require multiple inheritance.
- You can implement more than one facade for a subsystem.
- An adapter wraps an object to add new behaviours and responsibilities, and a facade "wraps" a set of objects to
  simplify.

## Chapter 8: Encapsulating Algorithms

The Template Method Pattern - Pattern implementation in Python

We are going to get down to encapsulating pieces of algorithms so that subclasses can hook themselves right into a
computation any time they want.

We can generalize the recipe and place it in a base class.

```java
public abstract class CaffeineBeverage {
  final void prepareRecipe() {
    // Our template method - it serves as a template for an algorithm.
    boilWater();
    brew();
    pourInCup();
    addCondiments();
  }
  
  abstract void brew();
  abstract void addCondiments();
  
  void boilWater() {}
  void pourInCup() {}
}
```

The Template Method defines the steps of an algorithm and allows subclasses to provide the implementation for one or
more steps.

The Template Method Pattern:

> Defines the skeleton of an algorithm in a method, deferring some steps to subclasses. Template Method lets subclasses
> redefine certain steps of an algorithm without changing the algorithm's structure.

This pattern is all about creating a template for an algorithm. Template - just a method, method that defines and
algorithms as a set of steps. One or more of these steps is defined to be abstract and implemented by a subclass. This
ensures the algorithm's structure stays unchanged.

We can also have concrete methods that do nothing by default - we call them `hooks`. Subclasses are free to override
these but don't have to.

Use abstract classes when subclass MUST provide an implementation of the method. Use hooks when that part of the
algorithm is optional.

The Hollywood Principle:

> Don't call us, we'll call you.

The Hollywood Principle gives us a way to prevent _dependency rot_. We allow low-level components to hook themselves
into a system, but the high-level components determine when they are needed, and how. In other words, the high-level
components give the low-level components the "don't call us, we'll call you" treatment.

Patters using The Hollywood Principle:

- The Template Method Principle
- The Observer Pattern
- The Strategy Pattern
- The Factory Pattern

The Dependency Inversion Principle teaches us to avoid the use fo concrete classes and instead work as much as possible
with abstractions. The Hollywood Principle is a technique for building frameworks or components so that lower-level
components can be hooked into the computation, but without creating dependencies between lower and higher level
components.

This pattern is a great design tool for creating frameworks, where the framework controls how something gets done, but
leaves you to specify your own details about what is actually happening at each step of the framework's algorithm.

`sort` methods are in the spirit of The Template Method Pattern, developer has to define `compare` method.~~

Template Method vs Strategy:

- Strategy defines a family of algorithms and make them interchangeable.
- Factory Method defines the outline of an algorithm, and lets subclasses do some of the work.
- Strategy uses object composition.
- Template Method uses inheritance.

Bullet points:

- A template method defines the steps of an algorithm, deferring to subclasses for the implementation of those steps.
- The Template Method Pattern gives us an important technique for code reuse.
- The template method's abstract may define concrete methods, abstract methods and hooks.
- Abstract methods are implemented by subclasses.
- Hooks are methods that do nothing or default behavior in the abstract class, but may be overridden in the subclass.
- To prevent subclasses form changing the algorithm in the template method, declare the template method as final.
- The Hollywood Principle guides us to put decision making in high-level modules that can decide how and when to call
  low-level modules.
- You will see lots of uses of the Template Method Pattern in real-world code, but (as with any pattern) don't expect it
  all to be designed "by the book".
- The Strategy and Template Method Patterns both encapsulate algorithms, the first by composition and the other by
  inheritance.
- Factory Method is a specialisation of Template Method.
