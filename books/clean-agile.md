[go back](https://github.com/pkardas/learning)

# Clean Agile: Back to Basics

Book by Robert Cecil Martin

- [Chapter 1: Introduction to Agile](#chapter-1-introduction-to-agile)
- [Chapter 2: The Reasons For Agile](#chapter-2-the-reasons-for-agile)
- [Chapter 3: Business Practices](#chapter-3-business-practices)
- [Chapter 4: Team Practices](#chapter-4-team-practices)
- [Chapter 5: Technical Practices](#chapter-5-technical-practices)
- [Chapter 6: Becoming Agile](#chapter-6-becoming-agile)
- [Chapter 7: Craftsmanship](#chapter-7-craftsmanship)
- [Chapter 8: Conclusion](#chapter-8-conclusion)
- [Afterword](#afterword)

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
screwed we are. The reason we want to know this as early as possible is so that we can manage the situation. Managers
manage software projects by gathering data and then making the best decisions they can base on that data.

Managers do this by making changes to the scope, the schedule, the staff, and the quality:

- Changing the Schedule - ask stakeholders if we can delay the project. Do this as early as possible.
- Adding Staff - in general, business is simply not willing to change the schedule. When new staff is added,
  productivity plummets for a few weeks as the new people suck the life out of the old people. Then, hopefully, the new
  people start to get smart enough to actually contribute. Of course, you need enough time, and enough improvement, to
  make up for the initial loss.
- Decrease Quality - everyone knows that you can go much faster by producing crap. WRONG. There is no such thing as
  quick and dirty. Anything dirty is slow. **The only way to go fast, is to go well**. If we want to shorten our
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
      obvious remedy for shipping bad code.
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
      him if he goes down. It is your responsibility to make sure that one or more of your teammates can cover for you.
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
    - Developers are entitled to precision in requirements and in the importance of those requirements. This right
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
      particular job or task. It may be that the developer does not feel confident in their ability to complete the
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
aren't even making the promise to try get 30 points done. This is nothing more than their best guess as to how many
points will be complete by the end of the iteration.

The Four-Quadrant Game (The Highest Return of Investment) - the stories that are valuable but cheap will be done right
away. Those that are valuable but expensive will be done later. Those that are neither valuable nor expensive might get
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
but very thin slice through all the layers of the system. For example, there is a story you cannot estimate: Print PDF -
you have never used the PDF library. So you write a new story called Estimate Print PDF - now you estimate that story,
which is easier to estimate.

The goal of each iteration is to produce data by getting stories done. The team should focus on stories rather than
tasks within stories. It is far better to get 80% of the stories done than it is to get each story 80% done. Focus on
driving the stories to completion.

A story cannot be completed without the acceptance tests. If QA continues to miss the midpoint deadline, one iteration
after another, then the ratio of QA engineers to developers is likely wrong. After the midpoint, if all the acceptance
tests are done, QA should be working on the tests for the next iteration.

The definition of done is this: acceptance tests pass.

If we see a positive slope in velocity, it likely does not mean that the team is actually going faster. Rather, it
probably means that the project manager is putting pressure on the team to go faster. As that pressure builds, the team
will unconsciously shift the value of their estimates to make it appear that they are going faster. This is simple
inflation. The points are a currency, and the team is devaluing them under external pressure. The lesson is that
velocity is a measurement not an objective. Don't put pressure on the thing you are measuring.

Estimate is not a promise, and the team has not failed if the actual velocity is lower.

The practice of Small Releases suggest that a development team should release their software as often as possible. The
new goal, is Continuous Delivery - the practice of releasing the code to production after every change.

Acceptance Tests - Requirements should be specified by the business.

BDD - Behavior-Driven Development - the goal is to remove the techie jargon from the tests and make the tests appear
more like specifications that businesspeople would appreciate. At first, this was just another attempt at formalizing
the language of testing, in this case using 3 special adverbs: Given, When, and Then.

## Chapter 4: Team Practices

A metaphor can provide a vocabulary that allows the team to communicate effectively. On the other hand, some metaphors
are silly to the point of being offensive to the customer.

DDD solved the metaphor problem. Eric Evans coined the term _Ubiquitous Language_. What the team needs is a model of the
problem domain, which is described by a vocabulary that everyone (the programmers, QA, managers, customers, users)
agrees on.

The Ubiquitous Language is used in all parts of the project. It is a thread of consistency that interconnects the entire
project during every phase of its lifecycle.

A software project is not a marathon, not a sprint, nor a sequence of sprints. In order to win, you must pace yourself.
If you leap out of the blocks and run full speed, you will run out of energy long before you cross the finish line.

You must run at a Sustainable Pace. If you try to run faster than the pace you can sustain, you will have to slow down
and rest before you reach the finish line. Managers may ask you to run faster than you should. You must not comply. It
is your job to husband your resources to ensure that you endure the end.

> Working overtime is not a way to show your dedication to your employer. What it shows is that you are a bad planner,
> that you agree to deadlines to which you shouldn't agree, that you make promises you shouldn't make, that you are a
> manipulable laborer and not a professional. This is not to say that all overtime is bad, nor that you should never
> work overtime. There are extenuating circumstances for which the only option is to work overtime. But they should be
> extremely rare. And you must be aware that the cost of that overtime will likely be greater than the time you save on
> the schedule.

The most precious ingredient in the life of a programmer is sufficient sleep. Make sure you know how many hours of sleep
your body needs, and then prioritize those hours. Those hours will more than pay themselves back.

No one owns the code in an Agile project. The code is owned by the team as a whole. Any member of the team can check and
improve any module in the project at any time. The team owns the code collectively. Collective Ownership does not mean
that you cannot specialize. However, even as you specialize, you must also generalize. Divide your work between your
specialty and other areas of the code. Maintain your ability to work outside your specialty.

The continuous build should never break.

Standup Meeting:

- This meeting is optional. Many teams get by just fine without one.
- It can be less often than daily. Pick the schedule that makes sense to you.
- It should take ~10 minutes, even for large teams.
- This meeting follows a simple formula.

The basic idea is that the team members stand in a circle and answer 3 questions:

1. What did I do since the last meeting?
2. What will I do until the next meeting.
3. What is in my way?
4. [Optional] Whom do you want to thank?

No discussion. No Posturing. No deep explanations. No complaints. Everybody gets 30 seconds to answer those 3 questions.

## Chapter 5: Technical Practices

Without TDD, Refactoring, Simple Design and Pari Programming, Agile becomes an ineffective flaccid shell of what it was
intended to be.

TEST-DRIVEN DEVELOPMENT. Every required behavior should be entered twice: once as a test, and then again as production
code that makes the test pass.

The 3 rules of TDD:

1. Do not write any production code until you have first written a test that fails due to the lack of that code.
2. Do not write more of a test that is sufficient to fail - and failing to compile counts as a failure.
3. Do not write more production code that is sufficient to pass the currently failing test.

The tests are a form of documentation that describe the system being tested. This documentation is written in a language
that the programmers know fluently. It is utterly unambiguous, it is so formal it executes, and it cannot get out of
sync with the application code. The test are the perfect kind of documentation for programmers: code.

Remember that function that is hard to test after the fact? The function is hard to test because you did not design it
to be easy to test. You wrote the code first, and you are now writing the tests as and afterthought. By writing the
tests first, you will decouple the system in ways that you had never thought about before. The whole system will be
testable, therefore, the whole system will be decoupled.

REFACTORING. Refactoring is the practice of improving the structure of the code without altering the behavior, as
defined by tests. In other words, we make changes to the names, the classes, the functions and the expressions without
breaking any of the tests.

Red/Green/Refactor:

1. We create a test that fails.
2. Then we make the test pass.
3. Then we clean up the code.
4. Return to step 1.

The word Refactoring should never appear on a schedule. Refactoring is not the kind of activity that appears on a plan.
We do not reserve time for refactoring. Refactoring is simply part of our minute-by-minute, hour-by-hour approach to
writing software.

Sometimes the requirements change is such a way that you realize the current design and architecture of the system is
suboptimal, and you need to make a significant change to the structure of the system. Such changes are made within the
Red/Green/Refactor cycle. We do not create a project specifically to change the design. We do not reserve time in the
schedule for such large refactorings. Instead, we migrate the code one small step at a time, while continuing to add new
features during normal Agile cycle.

SIMPLE DESIGN. The practice of Simple Design is one of the goals of Refactoring. Simple Design is the practice of
writing only the code that is required with a structure that keeps it simplest, smallest, and the most expressive.

Rules of Simple Design:

1. Pass all the tests.
2. Reveal the intent - It should be easy to read and self-descriptive. This is where we apply many of the simpled and
   more cosmetic refactorings. We also split large functions into smaller, better-named functions.
3. Remove duplication.
4. Decrease elements - Once we have removed all the duplication, we should strive to decrease the number of structural
   elements, such as classes, functions, variables.

The more complex the design, the greater the cognitive load placed on the programmers. That cognitive load is Design
Weight. The greater the weight of that design, the more time and effort are required for the programmers to understand
and manipulate the system.

PAIR PROGRAMMING. Pairing is the act of two people working together on a single programming problem. Any configuration
is fine (the same workspace, sharing the screen, keyboard, ping-pong, ...). We pair so that we behave like a team. When
a member of a team goes down, the other team members cover the hole left by that member and keep making progress towards
the goal. **Pairing is the best way, by far, to share knowledge between team members and prevent knowledge silos from
forming. It is the best way to make sure that nobody on the team is indispensable.**

The word "pair" implies that there are just 2 programmers involved in a pairing session. While this is typically true,
it is not a rule.

Generally, managers are pleased to see programmers collaborating and working together. It creates the impression that
work is being done.

**Never, ever, ever, ask for permission to pair. Or test. Or refactor. Or... You are the expert. You decide.**

## Chapter 6: Becoming Agile

Agile Values:

1. Courage - It is reckless to conform to a schedule by sacrificing quality. The belief that quality and discipline
   increase speed is a courageous belief because will constantly be challenged by powerful but naive folks who are in a
   hurry.
2. Communication - A team that sits together and communicates frequently can work miracles. We value direct and frequent
   communication that crosses channels. Face-to-face, informal, interpersonal conversations.
3. Feedback - Maximize the frequency and quantity of feedback. They allow us to determine when things are going wrong
   early enough to correct them. They provide massive education about the consequences of earlier decisions.
4. Simplicity - Numbers of problems should be reduced to minimum. Therefore, indirection can be kept to a minimum.
   Solutions can be simple. This applies to the software, but it also applies to the team. Passive aggression is
   indirection. Keep the code simple. Keep the team simpler.

These values are diametrically opposed to the values of large organisations who have invested heavily in
middle-management structures that value safety, consistency, command-and-control, and plan execution.

It is not really possible to transform such an organisation to Agile.

Agile coaches are members of the team whose role is to defend the process within the team. In the heat of development,
developers may be tempted to go off process. Perhaps they inadvertently stop pairing, stop refactoring, or ignore
failures in the continuous build. The coach acts as the team's conscience, always reminding the team of the promises
they made to themselves and the values they agreed to hold. This role typically rotates from one team member to the next
on an informal schedule and based on need. A mature team working steadily along does not require a coach. On the other
hand, a team under some kind of stress (schedule, business or interpersonal) may decide to ask someone to fill the role
temporarily.

Every member of an Agile team needs to understand the values and techniques of Agile. Therefore, if one member of the
team is trained, all members of the team should be trained.

Agile is for small- to medium-sized teams. period. It works well for such teams. Agile was never intended for large
teams. The problem of large teams is a problem societies and civilizations. And large teams are a solved problems.

Agile was invented because we did not know how to effectively organize a relatively small group of programmers to be
effective. Software development needed its own process because software is really like nothing else.

The answer to the question of Agile in the large is simply to organize your developers into small Agile teams, then use
standard management and operations research techniques to manage those teams.

Great tools do the following:

- Help people accomplish their objectives
- Can be learned "well enough" quickly
- Become transparent to users
- Allow adaptation and exaptation
- Are affordable

Git is an example of a great tool.

Your team should establish the pattern of work compatible with their specific context first, and then consider using
tools that support their workflow. Workers use and control tools, tools don't control and use people. You don't want to
get locked into other people's process flows.

ALM - Agile Lifecycle Management systems despite being feature rich and commercially successful, ALM tools utterly fail
at being great.:

- ALMs tend to be complicated, usually demanding up-front training.
- These tools often require constant attention.
- ALM tools aren't always easily adapted.
- ALM tools can be expensive.
- ALM does rarely work the way your team does, and often their default mode is at odds with Agile methods. For example
  many ALM tools assume that team members have individual work assignments, which makes them nearly unusable for teams
  who work together in a cross-functional way.

You can try different forms of Agile practices and check which one is the most relevant to your team's needs:

- Kanban - making the work visible, limiting work in progress and pulling work through the system.
- Scrum and XP - short daily meetings, a product owner, a process facilitator (Scrum Master), retrospectives, a
  cross-functional team, user stories, small releases, refactoring, writing tests first, and pair programming.
- Align team events - when the team events across multiple teams (standups, retrospectives) are aligned in time, it is
  possible to then roll up daily and systematic impediments via an escalation tree.
- Escalation trees - if it makes sense to always work on items that produce the highest value, then it makes sense to
  escalate impediments immediately via a well-defined escalation path.
- Regular interteam interaction - regular interaction between the Scrum Masters, Product Owners and team members who are
  working together toward a common deliverable.
- Portfolio Kanban - sets work in progress limits at the initiative level in order to ensure that the organization is
  focused on the highest-value work at all times.
- Minimum Viable Increments - what is the shortest path to producing the highest value in the shortest time. A growing
  number of organizations are taking this to extreme by implementing Continuous Delivery - releasing small updates on a
  frequent basis, sometimes as frequently as multiple times per day.

Enablers of multiteam coordination:

- SOLID - especially useful for simplifying multiteam coordination by dramatically reducing dependencies.
- Small, valuable user stories - limit the scope of dependencies, which simplifies multiteam coordination.
- Small, frequent releases - whether these releases are delivered to the customer or not, the practice of having a
  releasable product across all the teams involved helps to surface coordination and architectural issues so that the
  root cause can be found and addressed.
- Continuous Integration - calling for integration across the entire product after every checkin.
- Simple Design - one of the hardest practices to learn and apply because it is one of the most counter-intuitive
  practices. When coordinating the work of massive dependencies between teams, monolithic, centralized, preplanned
  architectures create massive dependencies between teams that tend to force them to work in lock step, thus defeating
  much of the promise of Agile. Simple Design, especially when used with practices such as a microservices architecture,
  enables Agility in large.

## Chapter 7: Craftsmanship

Many companies misunderstood Agile. Managers are willing to push developers to work faster and are using the full
transparency of the process to micromanage them. Developers are pushed hard to fit their estimates into the imposed
milestones. Failing to deliver all story points in a sprint means developer must work harder in the next sprint to make
up the delay. If the product owner thinks developers are spending too much time on things like automated tests,
refactoring, or pairing they simply tell them to stop doing it.

Strategic technical work has no place in _their_ Agile process. There is no need for architecture or design. The order
is to simply focus on the highest-priority item in the backlog and get it done as fast as possible. This approach
results in a long sequence of iterative tactical work and accumulation of technical debt. Bugs are accumulating,
delivery time goes up, people start to blame one another.

> Companies are still not mature enough to understand that technical problems are in fact business problems.

A group of developers met in November 2008 in Chicago to create a new movement: Software Craftsmanship.

Manifesto:

As aspiring Software Craftsmen, we are raising the bar or professional software development by practicing it and helping
others learn the craft. Through this work we have come to value:

- Not only working software, but also well-crafted software.
- Not only responding to change, but also steadily adding value.
- Not only individuals and interactions, but also a community of professionals.
- Not only customer collaboration, but also productive partnership.

The Software Craftsmanship manifesto describes an ideology, a mindset. It promotes professionalism through different
perspectives.

**Well-crafted software** - code that is well-designed and well tested. It is code that we are not scared to change and
code that enables business to react fast. It is code that is both flexible and robust.

**Steadily adding value** - no matter what we do, we should always be committed to continuously provide increasing value
to our clients and customers.

**A community of professionals** - we are expected to share and learn with each other, raising the bar of our industry.
We are responsible for preparing the next generation of developers.

**Productive partnership** - we will have a professional relationship with our clients and employers. We will always
behave ethically and respectfully, advising and working with our clients and employers in the best way possible. We will
expect a relationship of mutual respect and professionalism.

We will look at our work not as something we need to do as part of a job but as a professional service we provide. We
will take ownership of our own careers, investing our own time and money to get better at what we do. Craftspeople
strive to do the best job they can, not because someone is paying, but based on a desire to do things well.

Developers should not ask for authorization for writing tests. They should not have separate tasks for unit testing or
refactoring. These technical activities should be factored into the development of any feature. They are not optional.
Managers and developers should only discuss what is going to be delivered and when, not how. Every time developers
volunteer details of how they work, they are inviting managers to micromanage them. Developers should be able to clearly
describe how they work and the advantages of working that way to whomever is interested. What developers should not do
is to let other people decide how they work.

Conversations between developers and business should be about why, what and when - not how.

Craftsmanship promotes software development as a profession. A profession is part of who we are. A job is a thing that
we do but is not part of who we are. A profession is something we invest in. It is something we want to get better at.
We want to gain more skills and have a long-lasting and fulfilling career.

Combining Agile and Craftsmanship is the perfect way to achieve business agility.

## Chapter 8: Conclusion

This book covered basics of Agile.

## Afterword

Ask the developers in an "Agile organization" what Agile is, and you will likely get a very different answer than if you
ask anyone beyond the level of a software development manager.

Developers understand Agile to be a methodology for streamlining the development process and for making software
development more predictable, more practicable, and more manageable.

Many developers are blissfully unaware of management's use of the metrics provided by the implementation of Agile
practices and the data it produces.
