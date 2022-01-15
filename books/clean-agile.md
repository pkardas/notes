[go back](https://github.com/pkardas/learning)

# Clean Agile: Back to Basics

Book by Robert Cecil Martin

- [Chapter 1: Introduction to Agile](#chapter-1-introduction-to-agile)

## Chapter 1: Introduction to Agile

The Agile Manifesto was written in February 2001 in Utah by 17 software experts. Once a movement become popular, the
name of that movement got blurred through misunderstanding and usurpation.

When did Agile begin? More than 50 000 years ago when humans first decided to collaborate on a common goal. The idea of
choosing small intermediate goals and measuring the progress after each is too intuitive, and too human, to be
considered any kind of revolution.

Agile was not the only game in town:

- Scientific Management - top-down, command-and-control approach. Big up-front planning followed by careful detailed
  implementation. Worked best for projects that suffered a high cost of change and solved very well-defined problems
  with extremely specific goals.
- Waterfall - logical descendant of Scientific Management. Even though it was not what the author was recommending, it
  was the concept people took away from his paper. And it dominated the next 3 decades. It dominated but it didn't work.

How could thoroughly analyzing the problem, carefully designing a solution, and then implementing that design fail so
spectacularly over and over again.

The beginnings of the Agile reformation began in the late 1980s. In 1995 a famous paper on Scrum was written.

The Preamble of the Agile Manifesto:

> We are uncovering better ways of developing software by doing it and helping others do it.

The Agile Manifesto:

> **Individuals and interactions** over processes and tools.

> **Working software** over comprehensive documentation.

> **Customer collaboration** over contract negotiation.

> **Responding to change** over following a plan.

The Iron Cross of project management: good, fast, cheap, done - pick any three you like, you will not have the fourth.

A good manager drives a project to be good enough, fast enough, cheap enough and done as much as necessary. This is kind
of management that agile strives to enable.

Agile is a _framework_ that helps developers and managers execute this kind of pragmatic project management. However,
such management is not done automatic. It is entirely possible to work within Agile framework and still completely
mismanage the project and drive it to failure.

Agile provides data. An Agile development team produces just the kinds of data that managers need in order to make good
decisions:

- Velocity - how much the development team has gotten done every week.
- Burn-down chart - shows how many points remain until the next major milestone. Has a slope that predicts when the
  milestone will probably be reached.

This data managers need to decide how to set the coefficients on the Iron Cross and drive the project to the best
possible outcome.

Agile development is first and foremost a feedback-driven approach. Each, week, each day, each hour, and even each
minute is driven by looking at the results of the previous week, day, hour and minute, and then making the appropriate
adjustments.

The Date (deadline) is usually fixed and is not going to change because some developers think they may not be able to
make it. At the same time, the requirements are wildly in flux and can never be frozen. This is because the customers
don't really know what they want. So the requirements are constantly being re-evaluated and re-thought.

The Waterfall model promised to give us a way to get our arms around this problem:

- The Analysis Phase - no real consensus on just what analysis is, the best definition: "it is what analyst do".
- The Design Phase - is where you split the project up into modules and design interfaces between those modules.
- The Implementation Phase - there is no way to successfully pretend it is done, meanwhile, the requirements are still
  coming.
- The Death March Phase - customers are angry, stakeholders are angry, the pressure mounts, people quit. Hell.

It can be called - Runway Process Inflation - we are going to do the thing that did not work, and do it a lot more of
it.

Of course Waterfall was not an absolute disaster. It did not crush every software project into rubble. But it was, and
remains, a disastrous way to run a software project.

The Waterfall just makes so much sense. First, we analyze the problem, then we design the solution, and then we
implement the design. Simple. Direct. Obvious. And wrong.

An Agile project begins with analysis, but it is an analysis that never ends. Time before deadline is divided into
regular increments called _iterations_ or _sprints_. The size of an iteration is usually one or two weeks.

The first iteration (Iteration Zero). is used to generate a short list of features (stories). Iteration Zero is used to
set up development environment, estimate the stories and lay out the initial plan. This process of writing stories,
estimating them, planning them and designing never stops. Every iteration will have some analysis and design and
implementation in it.

In Agile project, we are always analyzing and estimating.

Software is not a reliably estimable process. We programmers simply do not know how long things will take. There is no
way to know how complicated a task is going to be until that task is engaged and finished.

After a couple of iterations we get insight how much time will be needed basing on past iterations. This number averages
at a relatively stable velocity. After four or five iterations, we will have a much better idea when this project will
be done.

We practice Agile in order to destroy hope before that hope can kill the project. Hope is the project killer. Hope is
what makes a software team mislead managers abut their true progress. Hope is a very bad way to manage a software
project. And Agile is a way to provide an early and continuous dose of cold, hard reality as a replacement for hope.

Some folks think that Agile is about going fast. It is not. Agile is about knowing, as early as possible, just how
screwed we are.The reason we want to know this as early as possible is so that we can manage the situation. Managers
manage software projects by gathering data and then making the best decisions they can base on that data.

Managers do this by making changes to the scope, the schedule, the staff, and the quality:

- Changing the Schedule - ask stakeholders if we can delay the project. Do this as early as possible.
- Adding Staff - in general, business is simply not willing to change the schedule. When new staff is added,
  productivity plummets for a few weeks as the new people suck the life out of the old people. Then, hopefully, the new
  people start to get smart enough to actually contribute. Of course, you need enough time, and enough improvement, to
  make up for the initial loss.
- Decrease Quality - everyone knows that you can go much faster by producing crap. WRONG. There is no such thing as
  quick and dirty. Anything dirty is slow. **The only wat to go fast, is to go well**. If we want to shorten our
  schedule, the only option is to _increase_ quality.
- Changing Scope - if the organization is rational, then the stakeholders eventually bow their heads in acceptance and
  begin to scrutinize the plan.

Inevitably the stakeholders will find a feature that we have already implemented and then say "It is a real shame you
did that one, we sure do not need it". At the beginning of each iteration, ask the stakeholders which features to
implement first.

20 000 foot view of Agile:

> Agile is a process wherein a project is subdivided into iterations. The output of each iteration is measured and used
> to continuously evaluate the schedule. Features are implemented in the order of business value so that the most
> valuable things are implemented first. Quality is kept as high as possible. The schedule is primarily managed by
> manipulating scope.  
