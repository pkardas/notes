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
