[go back](https://github.com/pkardas/learning)

# Fundamentals of Software Architecture: An Engineering Approach.

Book by Mark Richards and Neal Ford

- [Preface: Invalidating Axioms](#preface-invalidating-axioms)
- [Chapter 1: Introduction](#chapter-1-introduction)

## Preface: Invalidating Axioms

> Axiom - A statement or proposition which is regarded as being established, accepted, or self-evidently true.

Software architects (like mathematicians) also build theories atop axioms (but the software world is _softer_ than
mathematics).

Architects have an important responsibility to question assumptions and axioms left over from previous eras. Each new
era requires new practices, tools, measurements, patterns, and a host of other changes.

## Chapter 1: Introduction

THe industry does not have a good definition of software architecture.

> Architecture is about the important stuff... whatever that is ~ Ralph Johnson

The responsibilities of a software architect encompass technical abilities, soft skills, operational awareness, and a
host of others.

When studying architecture - keep in mind that everything can be understood in context - why certain decisions were
made, was based on the realities of the environment (for example building microservice architecture in 2002 would be
inconceivably expensive).

Knowledge of the architecture structure, architecture characteristics, architecture decisions, and design principles is
needed to fully understand the architecture of the system.

- structure/style: microservices, layered, microkernel, ...
- characteristics: availability, reliability, scalability, fault tolerance, security, ...
- decisions: what is and what is not allowed, rules for a system how it should be constructed
- design principles: guidelines for constructing systems -- leverage async messaging between services to increase
  performance

Expectations of an architect:

- make architecture decisions
    - instead of making technical decisions (use React.js), instruct development teams (use a reactive-based framework)
- continually analyze the architecture
    - validate decisions made years ago in order to prevent structural decay
- keep current with the latest trends
    - the decisions an architect makes tend to be long-lasting and difficult to change. understanding and following key
      trends helps the architect prepare for the future
- ensure compliance with decisions
    - continually verify that development teams are following the architecture decisions and design principles defined
- diverse exposure and experience
    - an architect should be at least familiar with a variety of technologies, effective architect should be aggressive
      in seeking out opportunities to gain experience in multiple languages, platforms and technologies
- have business domain knowledge
    - without business knowledge, an architect cannot communicate with stakeholders and business users and will quickly
      lose credibility
- possess interpersonal skills
    - interpersonal skills, including teamwork, facilitation, and leadership
    - engineers love to solve technical problems, however G. Weinberg said: "no matter what they tell you, it is always
      a people problem"
    - many architects are excellent technologists, but are ineffective architects because of poor communication skills
- understand and navigate politics
    - have negotiation skills, almost every decision an architect makes will be challenged

> All architectures become iterative because of _unknown unknowns_. Agile just recognizes this and does it sooner.

Iterative process fits the nature of software architecture. Trying to build a modern system such as microservices using
Waterfall will find a great deal of friction.

Nothing remain static. WHat we need is _evolutionary architecture_ - mutate the solution, evolve new solutions
iteratively. Adopting Agile engineering practices (continuous integration, automated machine provisioning, ...) makes
building resilient architectures easier.

Agile methodologies support changes better than planning-heavy processes because of tight feedback loop.

Laws of Software Architecture:

- Everything in software architecture is a trade-off
- If an architect thinks they have discovered something that isn't a trade-off, more likely they just haven't identified
  the trade-off yet
- Why is more important than how
