[go back](https://github.com/pkardas/learning)

# Clean Agile: Back to Basics

Book by Robert Cecil Martin

- [Chapter 1: Introduction to Agile](#chapter-1-introduction-to-agile)
- [Chapter 2: The Reasons For Agile](#chapter-2-the-reasons-for-agile)
- [Chapter 3: Business Practices](#chapter-3-business-practices)

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

## Chapter 2: The Reasons For Agile

Agile is important because of professionalism and the reasonable expectations from our customers.

- Professionalism - nowadays the cost of software failure is high, therefore we need to increase our professionalism. We
  are surrounded by computers, and they all need to be programmed - they all need software. Nowadays, virtually nothing
  of significance can be done without interacting with a software system. Now our actions are putting lives and fortunes
  at stake.
- Reasonable Expectations - meeting expectations is one of primary goals of Agile development.
    - we will not ship sh*t - Agile's emphasis on Testing, Refactoring, Simple Design and customer feedback is the
      obvious remedy fo shipping bad code.
    - continuous technical readiness - system should be technically (solid enough to be deployed) deployable at the end
      of every iteration.
    - stable productivity - big redesigns are horrifically expensive and seldom are deployed. Developers instead, should
      continuously keep the architecture, design and code as clean as possible, this allows to keep their productivity
      high and prevent the otherwise inevitable spiral into low productivity and redesign.
    - inexpensive adaptability - software - soft (easy to change), ware (product). Software was invented because we
      wanted a way to quickly and easily change the behavior of our machines. Developers should celebrate change because
      that is why we are here. Changing requirements is the name of the whole game. Our jobs depend on our ability to
      accept and engineer changing requirements and to make those changes relatively inexpensive. If a change to the
      requirements breaks your architecture, then your architecture sucks.
    - continuous improvement - the older a software system is, the better it should be. Unfortunately it seldom happens.
      We make things worse with time. The Agile practices of Pairing, TDD, Refactoring, and Simple Design strongly
      support this expectation.
    - fearless competence - people are afraid of changing bad code, you can break it, and if it breaks it will become
      yours. This fear forces you to behave incompetently. Customers, users, and managers expect _fearless competence_.
      They expect that if you see something wrong or dirty, you will fix it and clean it. They don't expect you to allow
      problems to fester and grow - they expect you to stay on top of the code, keeping it as clean and clear as
      possible. How to eliminate that fear? Use TDD.
    - qa should find nothing - the Agile practices support this expectation.
    - test automation - manual tests are always eventually lost. Manual tests are expensive and so are always a target
      for reduction. Besides, asking humans to do what machines can do is expensive, inefficient, and immoral. Every
      test that can be feasibly automated must be automated. Manual testing should be limited to those things that
      cannot be automatically validated and to the creative discipline of Exploratory Testing.
    - we cover for each other - each individual member of a software team makes sure that there is someone who can for
      him if he goes down.It is your responsibility to make sure that one or more of your teammates can cover for you.
    - honest estimates - you should provide estimates based on what you do and do not know. You can estimate in relative
      terms (task B should take half of the time spent on task A), you can also estimate using ranges.
    - you need to say "no" - when answer for something is "no", then the answer is really "no". For example if solution
      for a problem can not be found.
    - continuous aggressive learning - our industry changes quickly. We must be able to change with it. So learn, learn,
      learn! Learn with or without company's help.
    - mentoring - the best way to learn is to teach. So when new people join the team, teach them. Learn is to teach
      other.

Customer Bill of Rights:

- You have the right to an overall plan and to know what can be accomplished when and at what cost.
    - We cannot agree to deliver fixed scopes on gard dates. Either the scopes or the dates must be soft.
- You have the right to get the most possible value out of every iteration.
    - The business has the right to expect that developers will work on the most important things at any given time, and
      that each iteration will provide them the maximum possible usable business value.
- You have the right to see progress in a running system, proven to work by passing repeatable tests that you specify.
- You have the right to change your mind, to substitute functionality, and to change priorities without paying
  exorbitant costs.
- You have the right to be informed of schedule and estimate changes, in time to choose how to reduce the scope to meet
  a required date. You can cancel at any time and be left with a useful working system reflecting investment to date.

Developer Bill of Rights:

- You have the right to know what is needed with clear declarations of priority.
    - Developers are entitled to precision in requirements and in the importance of those requirements.This right
      applies within the context of an iteration. Outside an iteration, requirements and priorities will shift and
      change.
- You have the right to produce hugh-quality work at all times.
    - The business has no right to tell developers to cut corners or do low quality work. Or, to say this differently,
      the business has no right to force developers to ruin their professional reputations or violate their professional
      ethics.
- You have the right to ask for and receive help from peers, managers, and customers.
    - This statement gives programmers the right to communicate.
- You have the right to make and update your estimates.
    - You can change your estimate when new factors come to light. Estimates are guesses that get better with time.
      Estimates are never commitments.
- You have the right to accept your responsibilities instead of having them assigned to you.
    - Professionals accept work, they are not assigned work. A professional developer has every right to say "no" to a
      particular job or task. It may be that the developer does not feel confident in their ability to complete tge
      task, or it may be that the developer believes the task better suited for someone else. Or, it may be that the
      developer rejects the task for personal or moral reasons. Acceptance implies responsibility.

> Agile is a set of rights, expectations, and disciplines of the kind that form the basis of an ethical profession.

## Chapter 3: Business Practices

If you would like an accurate and precise estimate of a project, then break it down into individual lines of codes. The
time it takes you to do this will give you a very accurate and precise measure of how long it took you to build the
project.

Trivariate Analysis - such estimates are composed of three numbers: best-case, nominal-case, and worst-case. These
numbers are confidence numbers. The worst-case number is the amount of time which you feel 95% confident that the task
will be completed. The nominal-case has only 50% confidence, and the best case only 5%.

Stories and Points - a user story is an abbreviated description of a feature of the system, told from the point of view
of a user. We want to delay the specification of those details as long as possible, right up to the point where the
story is developed.

Story points are a unit of estimated effort, not real time. They are not even estimated time - they are estimated
effort. Velocity is not a commitment. The team is not making a promise to get 30 points done during the iteration. They
aren't even making the promise to try get 30 points done. This is nothing mor ethan their best guess as to how many
points will be complete by the end of the iteration.

The Four-Quadrant Game (The Highest Return of Investment) - the stories that are valuable but cheap will be done right
away. Those that are valuable but expensive will be done later. Those that ate neither valuable nor expensive might get
done one day. Those that are not valuable but are expensive will never be done.

Yesterday's weather - the best predictor of today's weather is yesterday's weather. The best predictor of the progress
of an iteration is the previous iteration.

The project is over when there are no more stories in the deck worth implementing.

User stories are simple statements that we use as reminders of features. We try not to record too much detail when we
write the story because we know that those details will likely change. Stories follow a simple set of guidelines that we
remember with the acronym INVEST:

- I - Independent - they do not need to be implemented in any particular order. This is a soft requirement because there
  may be stories that depend on other stories. Still, we try to separate the stories so that there is little dependence.
- N - Negotiable - we want details to be negotiable between the developers and the business.
- V - Valuable - the story must have clear and quantifiable value to the business. Refactoring/Architecture/Code cleanup
  is never a story. A story is always something that the business values.
- E - Estimable - must be concrete enough to allow the developers to estimate it.
- S - Small - a user story should be larger than one or two developers can implement in a single iteration.
- T - Testable - the business should be able to articulate tests that will prove that the story has been completed.

There are number of schemes for estimating stories:

- Flying Fingers
- Planning Poker

A spike is a meta-story, or a story for estimating a story. It is a spike because it often requires us to develop a long
but very thin slice through all the layers of the system. FOr example, there is a story you cannot estimate: Print PDF -
you have never used the PDF library. SO you write a new story called Estimate Print PDF - now you estimate that story,
which is easier to estimate.

The goal of each iteration is to produce data by getting stories done. The team should focus on stories rather than
tasks within stories. It is far better to get 80% of the stories done than it is to get each story 80% done. Focus on
driving the stories to completion.

A story cannot be completed without the acceptance tests. If QA continues to miss the midpoint deadline, one iteration
after another, then the ratio of QA engineers to developers is likely wrong. After the midpoint, if all the acceptance
tests are done, QA should be working on the tests for the next iteration.

The definition of done is this: acceptance tests pass.

If we see a positive slope in velocity, it likely does not mean that the team is actually going faster. Rather, it
probably means that the project manager is putting pressure on the team to go faster. ASs that pressure builds, the team
will unconsciously shift the value of their estimates to make it appear that they are going faster. This is simple
inflation. The points are a currency, and the team is devaluing them under external pressure. The lesson is that
velocity is a measurement not an objective. Don't put pressure on the thing you are measuring.

Estimate is not a promise, and the team has not failed if the actual velocity is lower.

The practice of Small Releases suggest that a development team should release their software as often as possible. The
new goal, is Continuous Delivery - the practice of releasing the code to production after every change.

Acceptance Tests - Requirements should be specified by the business.

BDD - Behavior-Driven Development - the goal is to remove the techie jargon from the tests and make the tests appear
more like specifications that businesspeople would appreciate. At first, this was just another attempt at formalizing
the language of testing, in this case using 3 special adverbs: Given, WHen, and Then. 
