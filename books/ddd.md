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

Effective domain modelers are knowledge crunchers (take a torrent of information and prove it for relevant trickle). Knowledge crunching is a collaborative work, typically led by developers in cooperation with domain experts. Early versions or prototypes feed experience back into the team and change interpretations.

All projects lack knowledge - people leave, team reorganisations happen - in general, knowledge is lost. Highly productive teams grow their knowledge continuously - improve technical knowledge along with general domain-modeling skills, but also seriously learn about specific domain they are working on. The accumulated knowledge makes them effective knowledge crunchers.

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



