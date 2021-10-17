[go back](https://github.com/pkardas/learning)

# Domain-Driven Design: Tackling Complexity in the Heart of Software

Book by Eric Evans

[TOC]

## Chapter 1: Crunching Knowledge

Effective modeling:

- Binding model and the implementation
- Cultivating a language based on the model
- Developing a knowledge-rich model
- Distilling the model - drop unneeded concepts
- Brainstorming and experimenting

Effective domain modellers are knowledge crunchers (take a torrent of information and prove it for relevant trickle). Knowledge crunching is a collaborative work, typically led by developers in cooperation with domain experts. Early versions or prototypes feed experience back into the team and change interpretations.

All projects lack knowledge - people leave, team reorganisations happen - in general, knowledge is lost. Highly productive teams grow their knowledge continuously - improve technical knowledge along with general domain-modelling skills, but also seriously learn about specific domain they are working on. The accumulated knowledge makes them effective knowledge crunchers.

Software is unable to fill in gaps with common sense - that is why knowledge crunching is important.

Example with overbooking strategy: overbooking check should be extracted from the booking functionality to be more explicit and visible. This is example fo domain modeling and securing and sharing knowledge. 

## Chapter 2: Communication and the Use of Language

The domain experts and developers use different language. Experts vaguely describe what they want, developers vaguely understand. Cost of translation, plus the risk of misunderstanding is too high. A project needs a common language. 

Ubiquitous language includes: names of classes and prominent operations, terms to discuss. Model based language should be used to describe artefacts, tasks and functionalities. 

Language may change to fit the discussion better. These changes will lead to refactoring of the code. Change in the language is change to the model. 

The domain-model-based terminology makes conversations more concise, you avoid talking about low level implementation details, instead you use high level concepts (like in the example: Itinerary, Routing Service, Route Specification instead of cargo id, origin and destination, ...).

Play with the model as you talk about the system, find easier ways to say what you need to say, and take those new ideas back down to the diagrams and code. 

The team should use ONE and only ONE language. Almost every conversation is an opportunity for the developers and domain experts to play with the model, deepen understanding and fine tune it.

Domain model is something between business terms developers don't understand and technical aspect of the design.

The vital detail about the design in captured in the code. Well written implementation should be transparent and reveal the model underlying it. The model is not the diagram, diagrams help to communicate and explain the model. 

Extreme Programming advocates using no extra design documents at all (usually because the fall out of sync) - the code should speak for itself. This motivates developers to keep code clean and transparent. 

However if document exists, it should not try to do what code already does well - document should illuminate meaning, give insight into large-scale structures, clarify design intent, complement the code and the talking.

## Chapter 3: Binding Model and Implementation

Tightly relating the code to an underlying model gives the code meaning and makes the model relevant. Design must map to the domain model, if not, the correctness of the software is suspect. 

Model-Driven Design - discards the dichotomy of analysis model and design to search out a single model that serves both purposes (ubiquitous language). Each object in the design plays a conceptual role described in the model. Model needs to be revised to reflect the model in a very literal way, so mapping is obvious. The code becomes expression of the model.

Model-Driven Design is hard to accomplish in procedural languages like C or Fortran. This approach is reserved for object-oriented programming languages. 

Implementation model should not be exposed to the user.

People responsible for the implementation should participate in modeling. Strict separation of responsibilities is harmful. Modeling and implementation are couples in model-driven design. Any technical person contributing to the model must spend some time touching the code. Every developer must be involved in some level of discussion about the model.

## Chapter 4: Isolating the Domain

Layered Architecture - the essential principle is that any element of a layer depends only on other elements in the same layer or on elements of the layers beneath it. Each layer specialises in a particular aspect of a computer program. Most commonly used layers:

- UI (Presentation) Layer - showing information to the user and interpreting the user's commands.
- Application Layer - this layer does not contain business logic, but only coordinates tasks and delegates work to collaborations of domain objects in the next layer down.
- Domain (Model) Layer - responsible for representing concepts of business, information about business situation and business rules. This layer is the heart of business software.
- Infrastructure Layer - generic technical capabilities that support the higher layers (message sending, drawing widgets on the UI, ...), may also support the pattern of interactions between the 4 layers through an architectural framework.

Partition a complex program into layers, develop a design within each layer that is cohesive and that depends only on the layers below. Concentrate all the code related the domain model in one layer and isolate it from the rest of the user interface, application and infrastructure code.

The domain models, free of the responsibility of displaying themselves, storing themselves, managing application tasks and so forth, can be focused on expressing the domain model. This allows to evolve model to be rich enough and clear enough to capture essential business knowledge and put it to work.

Such separation allows a much cleaner design for each layer, especially because they tend to evolve at different pace. 

Upper layers can user or manipulate elements of lower ones straightforwardly by calling their public interfaces.

Domain-driven design requires only one particular layer to exist. 

## Chapter 5: A Model Expressed in Software

ASSOCIATIONS. For every traversable association in the model, there is a mechanism in the software with the same properties. Constraints on associations should be included in the model and implementation (eg. president of ... for a period of time), they make the model more precise and the implementation easier to maintain. 

ENTITIES. Object modeling tends to lead us to focus on the attributes of an object, but the fundamental concept of an entity is an abstract continuity threading through a life cycle and even passing through multiple forms. Sometimes such an object must be matched with another object even though attributes differ. 

Transactions in a banking application, two deposits of the same amount to the same account on the same day are still distinct transactions. They have identity and are entities.

> When an object is distinguished by its identity, rather than its attributes, make this primary to its definition in the model. Keep the class definition simple and focused on life cycle continuity and identity. Define a means of distinguishing each object regardless of its form or history. 

Identity - this may simply mean unique identifier. 

Each entity must have an operational way of establishing its identity with another object - distinguishable even from another object with the same descriptive attributes.

Defining identity demands understanding of the domain.

VALUE OBJECTS. An object that represents a descriptive aspect of the domain with no conceptual identity. These are objects that describe things. When you care only about the attributes of an element of the model, classify it as a value object.

SERVICES. Some concepts from the domain aren't natural to model as objects. Forcing the required domain functionality to be the responsibility of an entity or value either distorts the definition of a model-based object or adds meaningless artificial objects. A service is an operation offered as an interface that stands alone in the model, without encapsulating state. The name *service* emphasises the relationship with other objects. Service have to be stateless. 

MODULES. Many don't consider modules as part of the model. Yet it isn't just code being divided into modules, but concepts. Low coupling between modules minimises the cost of understanding their place in the design. It is possible to analyse the contents of one module with a minimum of reference to others that interact. 

Choose modules that tell the story of the system and contain a cohesive set of concepts. Give the modules names that become part of the ubiquitous language. Modules and their names should reflect insight into the domain.

Modules need to coevolve with the rest of the model. This means refactoring modules right along with the model and code. But this refactoring often doesn't happen.

Use packaging to separate the domain layer from other code. Otherwise, leave as much freedom as possible to the domain developers to package the domain objects in ways that support their model and design choices. 

## Chapter 6: The Life Cycle of a Domain Object

The challenges:

- Maintaining object integrity throughout the life cycle
- Preventing the model from getting swamped by the complexity of managing the life cycle

These issues can be addressed using 3 patterns.

AGGREGATES. It is difficult to guarantee the consistency of changes to objects in a model with complex associations. Invariants need to be maintained that apply to closely related groups of objects, not just discrete objects. Yet cautious locking schemes cause multiple users to interfere pointlessly with each other and make a system unusable. An aggregate is a cluster or associated objects that we treat as a unit for the purpose of data changes. Each aggregate has a root and a boundary. Chose one entity to be the root of each aggregate, and control all access to the objects inside the boundary through the root. Allow external objects to hold references to the root only.

FACTORIES. When creation of an object, or an entire aggregation, becomes complicated or reveals too much of the internal structure, factories provide encapsulation (assembly of a car: cars are never assembled and driven at the same time, there is no value in combining both of these functions into the same mechanism). Creation of an object can be a major operation by itself, but complex assembly operations do not fit the responsibility of the created objects. Combining such responsibilities can produce ungainly designs that are hard to understand. Making the client direct construction muddies the design of the client, breaches encapsulation of the assembled object or aggregate, and overly couples the client to the implementation of the created object.

Two basic requirements for any good factory:

1.  Each creation method is atomic and enforces all invariants of the created object or aggregate.
2. The factory should be abstracted to the type desired, rather than the concrete class created

REPOSITORIES. Associations allow us to find an object based on its relationship to another. But we must have a starting point for a traversal to an entity of value in the middle of its life cycle. For each type of object that needs global access, create an object that can provide the illusion of an in-memory collection of all objects of that type. Set up access through a well-known global interface. Provide methods to add and remove objects, which will encapsulate the actual insertion or removal of data in the data store. Provide methods that select objects based on some criteria and return objects. Provide repositories only for aggregate roots that actually need direct access. Keep the client focused on the model, delegating all object storage and access to the repositories. 

Repository provide methods that allow a client to request objects matching some criteria.
