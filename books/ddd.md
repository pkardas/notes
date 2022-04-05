[go back](https://github.com/pkardas/learning)

# Domain-Driven Design: Tackling Complexity in the Heart of Software

Book by Eric Evans

- [Chapter 1: Crunching Knowledge](#chapter-1-crunching-knowledge)
- [Chapter 2: Communication and the Use of Language](#chapter-2-communication-and-the-use-of-language)
- [Chapter 3: Binding Model and Implementation](#chapter-3-binding-model-and-implementation)
- [Chapter 4: Isolating the Domain](#chapter-4-isolating-the-domain)
- [Chapter 5: A Model Expressed in Software](#chapter-5-a-model-expressed-in-software)
- [Chapter 6: The Life Cycle of a Domain Object](#chapter-6-the-life-cycle-of-a-domain-object)
- [Chapter 7: Using the Language: An Extended Example](#chapter-7-using-the-language-an-extended-example)
- [Chapter 8: Breakthrough](#chapter-8-breakthrough)
- [Chapter 9: Making Implicit Concepts Explicit](#chapter-9-making-implicit-concepts-explicit)
- [Chapter 10: Supple Design](#chapter-10-supple-design)
- [Chapter 11: Applying Analysis Patterns](#chapter-11-applying-analysis-patterns)
- [Chapter 12: Relating Design Patterns to the Model](#chapter-12-relating-design-patterns-to-the-model)
- [Chapter 13: Refactoring Toward Deeper Insight](#chapter-13-refactoring-toward-deeper-insight)
- [Chapter 14: Managing Model Integrity](#chapter-14-managing-model-integrity)
- [Chapter 15: Distillation](#chapter-15-distillation)
- [Chapter 16: Large-Scale Structure](#chapter-16-large-scale-structure)

## Chapter 1: Crunching Knowledge

Effective modeling:

- Binding model and the implementation
- Cultivating a language based on the model
- Developing a knowledge-rich model
- Distilling the model - drop unneeded concepts
- Brainstorming and experimenting

Effective domain modellers are knowledge crunchers (take a torrent of information and prove it for relevant trickle).
Knowledge crunching is a collaborative work, typically led by developers in cooperation with domain experts. Early
versions or prototypes feed experience back into the team and change interpretations.

All projects lack knowledge - people leave, team reorganisations happen - in general, knowledge is lost. Highly
productive teams grow their knowledge continuously - improve technical knowledge along with general domain-modelling
skills, but also seriously learn about specific domain they are working on. The accumulated knowledge makes them
effective knowledge crunchers.

Software is unable to fill in gaps with common sense - that is why knowledge crunching is important.

Example with overbooking strategy: overbooking check should be extracted from the booking functionality to be more
explicit and visible. This is example of domain modeling and securing and sharing knowledge.

## Chapter 2: Communication and the Use of Language

The domain experts and developers use different language. Experts vaguely describe what they want, developers vaguely
understand. Cost of translation, plus the risk of misunderstanding is too high. A project needs a common language.

Ubiquitous language includes: names of classes and prominent operations, terms to discuss. Model based language should
be used to describe artefacts, tasks and functionalities.

Language may change to fit the discussion better. These changes will lead to refactoring of the code. Change in the
language is change to the model.

The domain-model-based terminology makes conversations more concise, you avoid talking about low level implementation
details, instead you use high level concepts (like in the example: Itinerary, Routing Service, Route Specification
instead of cargo id, origin and destination, ...).

Play with the model as you talk about the system, find easier ways to say what you need to say, and take those new ideas
back down to the diagrams and code.

The team should use ONE and only ONE language. Almost every conversation is an opportunity for the developers and domain
experts to play with the model, deepen understanding and fine tune it.

Domain model is something between business terms developers don't understand and technical aspect of the design.

The vital detail about the design in captured in the code. Well written implementation should be transparent and reveal
the model underlying it. The model is not the diagram, diagrams help to communicate and explain the model.

Extreme Programming advocates using no extra design documents at all (usually because the fall out of sync) - the code
should speak for itself. This motivates developers to keep code clean and transparent.

However, if document exists, it should not try to do what code already does well - document should illuminate meaning,
give insight into large-scale structures, clarify design intent, complement the code and the talking.

## Chapter 3: Binding Model and Implementation

Tightly relating the code to an underlying model gives the code meaning and makes the model relevant. Design must map to
the domain model, if not, the correctness of the software is suspect.

Model-Driven Design - discards the dichotomy of analysis model and design to search out a single model that serves both
purposes (ubiquitous language). Each object in the design plays a conceptual role described in the model. Model needs to
be revised to reflect the model in a very literal way, so mapping is obvious. The code becomes expression of the model.

Model-Driven Design is hard to accomplish in procedural languages like C or Fortran. This approach is reserved for
object-oriented programming languages.

Implementation model should not be exposed to the user.

People responsible for the implementation should participate in modeling. Strict separation of responsibilities is
harmful. Modeling and implementation are couples in model-driven design. Any technical person contributing to the model
must spend some time touching the code. Every developer must be involved in some level of discussion about the model.

## Chapter 4: Isolating the Domain

Layered Architecture - the essential principle is that any element of a layer depends only on other elements in the same
layer or on elements of the layers beneath it. Each layer specialises in a particular aspect of a computer program. Most
commonly used layers:

- UI (Presentation) Layer - showing information to the user and interpreting the user's commands.
- Application Layer - this layer does not contain business logic, but only coordinates tasks and delegates work to
  collaborations of domain objects in the next layer down.
- Domain (Model) Layer - responsible for representing concepts of business, information about business situation and
  business rules. This layer is the heart of business software.
- Infrastructure Layer - generic technical capabilities that support the higher layers (message sending, drawing widgets
  on the UI, ...), may also support the pattern of interactions between the 4 layers through an architectural framework.

Partition a complex program into layers, develop a design within each layer that is cohesive and that depends only on
the layers below. Concentrate all the code related the domain model in one layer and isolate it from the rest of the
user interface, application and infrastructure code.

The domain models, free of the responsibility of displaying themselves, storing themselves, managing application tasks
and so forth, can be focused on expressing the domain model. This allows to evolve model to be rich enough and clear
enough to capture essential business knowledge and put it to work.

Such separation allows a much cleaner design for each layer, especially because they tend to evolve at different pace.

Upper layers can user or manipulate elements of lower ones straightforwardly by calling their public interfaces.

Domain-driven design requires only one particular layer to exist.

## Chapter 5: A Model Expressed in Software

ASSOCIATIONS. For every traversable association in the model, there is a mechanism in the software with the same
properties. Constraints on associations should be included in the model and implementation (e.g. president of ... for a
period of time), they make the model more precise and the implementation easier to maintain.

ENTITIES. Object modeling tends to lead us to focus on the attributes of an object, but the fundamental concept of an
entity is an abstract continuity threading through a life cycle and even passing through multiple forms. Sometimes such
an object must be matched with another object even though attributes differ.

Transactions in a banking application, two deposits of the same amount to the same account on the same day are still
distinct transactions. They have identity and are entities.

> When an object is distinguished by its identity, rather than its attributes, make this primary to its definition in
> the model. Keep the class definition simple and focused on life cycle continuity and identity. Define a means of
> distinguishing each object regardless of its form or history.

Identity - this may simply mean unique identifier.

Each entity must have an operational way of establishing its identity with another object - distinguishable even from
another object with the same descriptive attributes.

Defining identity demands understanding of the domain.

VALUE OBJECTS. An object that represents a descriptive aspect of the domain with no conceptual identity. These are
objects that describe things. When you care only about the attributes of an element of the model, classify it as a value
object.

SERVICES. Some concepts from the domain aren't natural to model as objects. Forcing the required domain functionality to
be the responsibility of an entity or value either distorts the definition of a model-based object or adds meaningless
artificial objects. A service is an operation offered as an interface that stands alone in the model, without
encapsulating state. The name *service* emphasises the relationship with other objects. Service have to be stateless.

MODULES. Many don't consider modules as part of the model. Yet it isn't just code being divided into modules, but
concepts. Low coupling between modules minimises the cost of understanding their place in the design. It is possible to
analyse the contents of one module with a minimum of reference to others that interact.

Choose modules that tell the story of the system and contain a cohesive set of concepts. Give the modules names that
become part of the ubiquitous language. Modules and their names should reflect insight into the domain.

Modules need to co-evolve with the rest of the model. This means refactoring modules right along with the model and
code. But this refactoring often doesn't happen.

Use packaging to separate the domain layer from other code. Otherwise, leave as much freedom as possible to the domain
developers to package the domain objects in ways that support their model and design choices.

## Chapter 6: The Life Cycle of a Domain Object

The challenges:

- Maintaining object integrity throughout the life cycle
- Preventing the model from getting swamped by the complexity of managing the life cycle

These issues can be addressed using 3 patterns.

AGGREGATES. It is difficult to guarantee the consistency of changes to object in a model with complex associations.
Invariants need to be maintained that apply to closely related groups of objects, not just discrete objects. Yet
cautious locking schemes cause multiple users to interfere pointlessly with each other and make a system unusable. An
aggregate is a cluster or associated objects that we treat as a unit for the purpose of data changes. Each aggregate has
a root and a boundary. Chose one entity to be the root of each aggregate, and control all access to the objects inside
the boundary through the root. Allow external objects to hold references to the root only.

FACTORIES. When creation of an object, or an entire aggregation, becomes complicated or reveals too much of the internal
structure, factories provide encapsulation (assembly of a car: cars are never assembled and driven at the same time,
there is no value in combining both of these functions into the same mechanism). Creation of an object can be a major
operation by itself, but complex assembly operations do not fit the responsibility of the created objects. Combining
such responsibilities can produce ungainly designs that are hard to understand. Making the client direct construction
muddies the design of the client, breaches encapsulation of the assembled object or aggregate, and overly couples the
client to the implementation of the created object.

Two basic requirements for any good factory:

1. Each creation method is atomic and enforces all invariants of the created object or aggregate.
2. The factory should be abstracted to the type desired, rather than the concrete class created

REPOSITORIES. Associations allow us to find an object based on its relationship to another. But we must have a starting
point for a traversal to an entity of value in the middle of its life cycle. For each type of object that needs global
access, create an object that can provide the illusion of an in-memory collection of all objects of that type. Set up
access through a well-known global interface. Provide methods to add and remove objects, which will encapsulate the
actual insertion or removal of data in the data store. Provide methods that select objects based on some criteria and
return objects. Provide repositories only for aggregate roots that actually need direct access. Keep the client focused
on the model, delegating all object storage and access to the repositories.

Repository provide methods that allow a client to request objects matching some criteria.

## Chapter 7: Using the Language: An Extended Example

The model organises domain knowledge and provides a language for the team. Each object in the model has a clear meaning.

To prevent domain responsibilities from being mixed with those of other parts of the system apply layered architecture.

Modeling and design is not a constant forward process. It will grind to a halt unless there is a frequent refactoring to
take advantage of new insights to improve the model and the design.

The real challenge is to actually find an incisive model, one that captures subtle concerns of the domain experts and
can drive a practical design. Ultimately, we hope to develop a model that captures a deep understanding of the domain.

Refactoring is the redesign of software in ways that do not change its functionality. Rather than doing elaborate
up-front design decisions, developers take code through a continuous series of small, discrete design changes, each
leaving existing functionality unchanged while making the design more flexible or easier to understand.

Initial models usually are naive and superficial, based on shallow knowledge. Versatility, simplicity and explanatory
power come from a model that is truly in tune with the domain.

You will usually depend on creativity and trail and error to find good ways to model the concepts you discover.

## Chapter 8: Breakthrough

The returns from refactoring are not linear. Usually there is marginal return for a small effort, and the small
improvements add up.

Slowly but surely, the team assimilates knowledge and crunches it into a model. Each refinement of code and model gives
developers a clearer view. This clarity creates the potential for a breakthrough.

Don't become paralysed trying to bring about a breakthrough. The possibility usually comes after many modest
refactorings. Most of the time is spent making piecemeal improvements, with model insights emerging gradually during
each successive refinement.

Don't hold back from modest improvements, which gradually deepen the model, even if confined with the same general
conceptual framework.

## Chapter 9: Making Implicit Concepts Explicit

A deep model has power because it contains the central concepts and abstractions that can succinctly and flexibly
express essential knowledge of the user's activities, their problems and their solutions.

The first step is to somehow represent the essential concepts of the domain in the model. Refinement comes later, after
successive iterations of knowledge crunching and refactoring. But this process really gets into gear when an important
concept is recognised and made explicit in the model and design.

Transformation of a formerly implicit concept into an explicit one is a breakthrough that leads to a deep model. More
often, though, the breakthrough comes later, after a number of important concepts are explicit in the model.

Listen to the language the domain experts use. Are there terms that succinctly state something complicated? Are they
correcting your word choice? Do the puzzled looks on their faces go away when you use a particular phrase? These are
hints of a concept that might benefit the model.

Constraints make up a particularly important category of model concepts. They often emerge implicitly, and expressing
them explicitly can greatly improve a design. Sometimes constraints find a natural home in an object or separate method.

Specification - a predicate that determines if an object does satisfy some criteria.

## Chapter 10: Supple Design

The ultimate purpose of software is to serve users. But first, that same software has to serve developers. This is
especially true in a process that emphasises refactoring.

When software with complex behaviour lacks good a design, it becomes hard to refactor or combine elements. Duplication
starts to appear as soon as a developer isn't confident of predicting the full implications of computation. Duplication
is forced when design elements are monolithic, so that the parts cannot be recombined.

Supple design is the complement to deep modelling. Once you have dug out implicit concepts and made them explicit, you
have the raw material. Thorough the iterative cycle, you hammer that material into a useful shape.

If developer must consider the implementation of a component in order to use it, the value of encapsulation is lost.
Tames should conform to the ubiquitous language so that team members can quickly infer their meaning. Write a test of a
behaviour before creating it, to force your thinking into client developer mode.

Place as much of the logic of the program as possible into functions, operations that return results with no observable
side effects.

Decompose design elements (operations, interfaces, classes and aggregates) into cohesive units, taking into
consideration your intuition of the important divisions in the domain. Align the model with the consistent aspects of
the domain that make it a viable area of knowledge in the first place.

Low coupling is fundamental to object design. When you can go all the way. Eliminate all other concepts from the
picture. Then the class will be completely self-contained and can be studied and understood alone. Every such
self-contained class significantly eases the burden of understanding a module.

Where it fits, define an operation whose return type is the same as the type of its arguments.

## Chapter 11: Applying Analysis Patterns

> Analysis patterns are groups of concepts that represent a common construction in business modelling. It may be
> relevant to only one domain, or it may span many domains.

An analysis pattern is a template for solving an organizational, social or economic problem in a professional domain.

## Chapter 12: Relating Design Patterns to the Model

Not all design patterns can be used as domain patterns.

STRATEGY - Domain models contain processes that are not technically motivated but actually meaningful in the problem
domain. When alternative processes must be provided, the complexity of choosing the appropriate process combines with
the complexity of the multiple processes themselves, and things get out of hand. Factor the varying parts of process
into a separate "strategy" object in the model. Factor apart a rule and the behaviour it governs. Implement the rule or
substitutable process following the strategy design pattern. Multiple versions of the strategy object represents
different ways the process can be done.

COMPOSITE - When the relatedness of nested containers is not reflected in the model, common behaviour has to be
duplicated at each level of the hierarchy, and nesting is rigid. Clients must deal with different levels of the
hierarchy through different interfaces, even though there may be no conceptual difference they care about. Recursion
through the hierarchy to produce aggregated information is very complicated. Define an abstract type that encompasses
all members of the composite. Methods that return information are implemented on containers to return aggregated
information about their contents. Leaf nodes implement those methods based on their own values. Clients deal with the
abstract type and have no need to distinguish leaves from containers.

## Chapter 13: Refactoring Toward Deeper Insight

Multifaceted process. There are 3 things you have to focus on:

1. Live in the domain
2. Keep looking at things a different way
3. Maintain an unbroken dialog with domain experts

Seeking insight into the domain creates a broader context for the process of refactoring.

Refactoring toward deeper insight is a continuing process. Implicit concepts are recognised and made explicit.
Development suddenly comes to the brink of a breakthrough and plunges through to a deep model.

## Chapter 14: Managing Model Integrity

Total unification of the domain model for a large system will not be feasible or cost-effective.

BOUNDED CONTEXT. Multiple models are in play on any large project. Yet when code based on distinct models is combined,
software becomes buggy, unreliable and difficult to understand. Communication among team members becomes confused. It is
often unclear in what context a model should not be applied. Therefore, explicitly define the context within which a
model applies. Explicitly set boundaries in terms of team organisation, usage within specific parts of the application.
And physical manifestations such as code bases and database schemas. Keep the model strictly consistent within these
bounds, but don't be distracted or confused by issues outside.

CONTINUOUS INTEGRATION. When a number of people are working in the same bounded context, there is a strong tendency for
the model to fragment. The bigger the team, the bigger the problem, but a few as three or four people can encounter
serious problems. Yet breaking down the system into even-smaller contexts eventually loses a valuable level of
integration and coherency. Therefore, institute a process of merging all code and other implementation artefacts
frequently, with automated tests to flag fragmentation quickly. Relentlessly exercise the ubiquitous language to hammer
out a shared view of the model as the concepts evolve in different people's heads.

CONTEXT MAP. People on other teams will not be very aware of the context sounds and will unknowingly make changes that
blur the edges or complicate the interconnections. When connections must be made between different contexts, they tend
to bleed into each other. Therefore, identify each model in play on the project and define its bounded context. This
includes the implicit models of non-object-oriented subsystems. Name each bounded context, and make the names part of
ubiquitous language. Describe the points of contact between the models, outlining explicit translation for any
communication and highlighting any sharing.

SHARED KERNEL. Uncoordinated teams working on closely related applications can go racing forward for a while, but what
they produce may not fit together. They can end up spending more on translation layers and retrofitting than they would
have on continuous integration in the first place, meanwhile duplicating effort and losing the benefits of a common
ubiquitous language. Therefore, designate some subset of the domain that the two teams agree to share. Of course this
includes, along with this subset of the model, the subset of code or of the database design associated with that part of
the model. This explicitly shared stuff has special status, and shouldn't be changed without consultation with the other
team. Integrate a functional system frequently, but somewhat less often than the pace of continuous integration within
the teams. At these integrations, run the tests of both teams.

CUSTOMER / SUPPLIER DEVELOPMENT TEAMS. The freewheeling development of the upstream team can be cramped if the
downstream team has no veto power over changes, or if procedures for requesting changes are too cumbersome. The upstream
team may even be inhibited, worried about breaking the downstream system. Meanwhile, the downstream team can be
helpless, at the mercy of upstream priorities. Therefore, establish a clear customer / supplier relationship between the
two teams. In planning sessions, make the downstream team play the customer role to the upstream team. Negotiate the
budget and tasks for downstream requirements so that everyone understands the commitment and schedule.

CONFORMIST. When two development teams have an upstream / downstream relationship in which the upstream has no
motivation to provide for the downstream team's needs, the downstream team is helpless. Therefore, eliminate the
complexity of translation between bounded contexts by slavishly adhering to the model of the upstream team.

ANTI-CORRUPTION LAYER. When a new system is being built that must have a large interface with another, the difficulty of
relating two models can eventually overwhelm the intent of the new model altogether, causing it to be modified to
resemble the other system's model, in an ad hoc fashion. Therefore, create an isolating layer to provide clients with
functionality in terms of their own domain model. The layer talks to the other system through its existing interface,
requiring little or no modification to the other system.

SEPARATE WAYS. Integration is always expensive. Sometimes the benefit is small. Therefore, declare a bounded context to
have no connection to the others at all, allowing developers to find simple, specialised solutions within this small
scope.

OPEN HOST SERVICE. When a subsystem has to be integrated with many others, there is more and more to maintain and more
and more to worry about when changes are made. Therefore, define a protocol that gives access to your subsystem as a set
of services.

PUBLISHED LANGUAGE. Direct translation to and from the existing domain models may not be a good solution. Those models
may be overly complex or poorly factored. Therefore, use a well-documented shared language that can express the
necessary domain information as a common medium of communication, translating as necessary into and out of that
language.

## Chapter 15: Distillation

CORE DOMAIN. In designing a large system, there are so many contributing components, all complicated and all absolutely
necessary to success, that the essence of the domain model, can be obscured and neglected. Therefore, boil the model
down. Make the core small.

GENERIC SUBDOMAINS. Anything extraneous makes the core domain harder to discern and understand. Therefore, identify
cohesive subdomains that are not the motivation for your project. Factor out generic models of these subdomains and
place them in separate models.

DOMAIN VISION STATEMENT. In later stages of development, there is a need for explanation the value of the system that
does not require an in-depth study of the model. Therefore, write a short description of the core domain. Keep it
narrow. Write this statement early and revise it as you gain new insight.

HIGHLIGHTED CORE. The mental labor of constantly filtering the model to identify key parts absorbs concentration better
spent on design thinking, and it requires comprehensive knowledge of the model. Therefore, write a brief document that
describes the core domain and the primary interactions among core elements.

COHESIVE MECHANISMS. Computations sometimes reach a level of complexity that begins to bloat the design. The
conceptual *what* is swamped by the mechanistic *how*. Therefore, partition a conceptually cohesive mechanism into a
separate lightweight framework.

SEGREGATED CODE. Elements in the model may partially serve the core domain and partially play supporting role. Core
elements may be tightly coupled to generic ones. Therefore, refactor the model to separate the core concepts from
supporting players and strengthen the cohesion of the core while reducing its coupling to other code.

ABSTRACT CORE. When there is a lot of interaction between subdomains in separate modules, either many references will
have to be created between modules, which defeats much of the value of the partitioning or the interaction will have to
be made indirect, which makes the model obscure. Therefore, identify the most fundamental concepts in the model and
factor them into distinct classes, abstract classes or interfaces.

## Chapter 16: Large-Scale Structure

EVOLVING ORDER. Design free-for-all's produce systems no one can make sense of as whole. Therefore, let this conceptual
large-scale structure evolve with the application, possibly changing to a completely different type of structure along
the way. Don't over constrain the detailed design and model decisions that must be made with detailed knowledge.

SYSTEM METAPHOR. Software decisions tend to be very abstract and hard to grasp. Developers and users alike need tangible
ways to understand the system and share a view of the system as a whole. Therefore, organise the design around metaphor
and absorb it into the ubiquitous language.

RESPONSIBILITY LAYERS. When each individual object has handcrafted responsibilities, there are no guidelines, no
infirmity and no ability to handle large swaths of the domain together. Therefore, look at the conceptual dependencies
in your model and the varying rates and sources of change of different parts of your domain. Refactor the model so that
the responsibilities of each domain object fit nearly within the responsibility of one layer.

KNOWLEDGE LEVEL. In application in which the roles and relationships between entities vary in different situations,
complexity can explode. Objects end up with references to other types to cover a variety of cases, or with attributes
that are used in different ways in different situations. Therefore, create a distinct set of objects that can be used to
describe and constrain the structure and behaviour of the basic model.

PLUGGABLE COMPONENT BEHAVIOUR. When a variety of applications have to interoperate, all based on the same abstractions
but designed independently, translations between multiple bounded contexts limit integration. Duplication and
fragmentation raise costs of development and installation. Therefore, distill an abstract core of interfaces and
interactions and create a framework that allow diverse implementations of those interfaces to be freely substituted. 
