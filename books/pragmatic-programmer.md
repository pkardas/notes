[go back](https://github.com/pkardas/learning)

# The Pragmatic Programmer: journey to mastery, 20th Anniversary Edition

Book by David Thomas and Andrew Hunt

- [Chapter 1: A Pragmatic Philosophy](#chapter-1-a-pragmatic-philosophy)
- [Chapter 2: A Pragmatic Approach](#chapter-2-a-pragmatic-approach)
- [Chapter 3: The Basic Tools](#chapter-3-the-basic-tools)
- [Chapter 4: Pragmatic Paranoia](#chapter-4-pragmatic-paranoia)
- [Chapter 5: Bend, or Break](#chapter-5-bend-or-break)
- [Chapter 6: Concurrency](#chapter-6-concurrency)
- [Chapter 7: While you are coding](#chapter-7-while-you-are-coding)
- [Chapter 8: Before the Project](#chapter-8-before-the-project)
- [Chapter 9: Pragmatic Projects](#chapter-9-pragmatic-projects)
- [Postface](#postface)

## Chapter 1: A Pragmatic Philosophy

**You Have Agency.** It is your life. You own it. You run it. You create it. This industry gives you a remarkable set of
opportunities. Be proactive, and take them.

The team needs to be able to trust you and rely on you, and you need to be comfortable relying on each of them as well.
In a healthy environment based in trust, you can safely speak your mind, present your ideas, and rely on your team
members who can in turn rely on you.

**Provide options, don't make lame excuses.** Instead of excuses provide options. Don't say it can't be done: explain
what can be done to salvage the solution. When you find yourself saying "_I don't know_" be sure to follow it up with
"_--but I'll find out_". It is a great way to admit what you don't know, but then take responsibility like a pro.

_Entropy_ - a term from physics that refers to the amount of "disorder" in a system. The entropy in the universe tends
toward a maximum. When disorder increases in software, we call it "software rot". Some folks might call it by the more
optimistic term "_technical debt_" (with the implied notion that they will pay it back someday, they probably will not).

**Don't live with broken windows.** Bad designs, wrong decisions, or poor code. Fix each one as soon as it is
discovered. If there is no sufficient time to fix it properly, board it up. Take some action to prevent further damage
and to show that you are on top of the situation. Don't let entropy win. If you find yourself working on a project with
quite a few broken windows, it is all to easy to slip into the mindset of "_All the rest of this code is crap, I will
just follow suit._". By the same token, if you find yourself on a project where the code is beautiful, well-designed,
and elegant - you will likely take extra special care not to mess it up.

Idea: Help strengthen your team by surveying your project neighbourhood. Choose two or three broken windows and discuss
with your colleagues what the problems are and what could be done to fix them.

**Be a catalyst for change.** You may be in a situation where you know exactly what needs doing and how to do it. People
will form committees, budgets will need approval, and things will get complicated. Work out what can you reasonably ask
for. Develop it well. Once you have got it, show people, and let them marvel. Sit back and wait for them to start asking
you to add the functionality you originally wanted. Show them a glimpse of the future, and you will get them to rally
around.

**Remember the Big Picture.** Constantly review what is happening around you, not just what you personally are doing.
Projects slowly and inexorably get totally out of hand. Most software disasters start out too small to notice, and most
projects overruns happen a day at a time. It is often the accumulation of small things that breaks morale and teams.

Situational awareness (is there anything out of context, anything that looks like it doesn't belong), a technique
practiced by folks ranging from Boy and Girl Scouts and Navy SEALs. Get in a habit of really looking and noticing your
surroundings.

**Make quality a requirements issue.** Involve your users in determining the project's real quality requirements.

> An investment in knowledge always pays the best interest ~ Benjamin Franklin

**Invest regularly in your knowledge portfolio.** Your knowledge and experience are your most important day-to-day
professional assets. Knowledge may become out of date, as the value of your knowledge declines, so does your value to
your company or client.

1. Invest regularly - invest in knowledge regularly, even small amounts.
2. Diversify - the more different things you know, the more valuable you are.
3. Manage risk - don't put all your technical eggs in one basket.
4. Buy low, sell high - learning an emerging technology before it becomes popular can be just as hard as finding an
   undervalues stock, but the payoff can be just as rewarding.
5. Review and rebalance - that hot technology you started investing last month might be stone-cold by now.

Goals:

- learn at least one programming language per year - by learning several approaches, you can broaden your thinking
- read a technical book each month
- read nontechnical books too - don't forget the human side of the equation, as that requires an entirely different
  skill set
- take classes - look for interesting courses at local or online college
- participate in local user groups and meetups - isolation can be deadly to your career, find out what people are
  working on outside of your company
- experiment with different environments - try Linux, Windows, Mac, a new IDE, ...
- stay current - read news and posts online on technology different from that of your current project

**Critically analyze what you read and hear.** You need to ensure that the knowledge in your portfolio is accurate and
unswayed by either vendor or media hype.

_Critical Thinking Tutorial:_

1. Ask the "Five Whys" - ask why at least 5 times. Ask a question and get an answer. Dig deeper by asking "why".
2. Who does this benefit? - "follow the money" can be a very helpful path to analyze. The benefits to someone else or
   another organization may be aligned with your own, or not.
3. What is the context? - everything occurs in its own context. Good for someone, doesn't mean it is good for you.
4. Why is this a problem? - is there an underlying model? How does the underlying model work?

**English is just another programming language.** Having the best ideas, the finest code, or the most pragmatic thinking
is ultimately sterile unless you can communicate with other people.

**It is both what you say and the way you say it.** There is no point in having great ideas if you don't communicate
them effectively. The more effective communication, the more influential you become.

**Build documentation in, don't bolt it on.** It is easy to produce good-looking documentation from the comments in
source code, and we recommend adding comments to modules and exported functions to give other developers a leg up when
they come to use it. Restrict your non-API commenting to discussing why something is done, its purpose and its goal. The
code already shows how it is done, so commenting on this is redundant - and is a violation of the DRY principle.

## Chapter 2: A Pragmatic Approach

**Good design is easier to change than bad design.** A thing is well-designed if it adapts to the people who use it.
Code should be Easy To Change. That's why SRP, decoupling, naming, ... are important, because of ETC.

**DRY - Don't Repeat Yourself.** Every piece of knowledge must have a single, unambiguous, authoritative representation
within a system.

Most people maintenance begins when an application is released, that maintenance means fixing bugs and enhancing
features. This is wrong. Programmers are constantly in maintenance mode. Maintenance is not a discrete activity, but a
routine part of the entire development process. When we perform maintenance, we have to find and change the
representation of things. It is easy to duplicate knowledge in the specifications, processes, and programs we develop,
and when we do so, we invite a maintenance nightmare.

DRY is about the duplication of knowledge, of intent. It is about expressing the same thing in two different places,
possibly in two totally different ways.

Code may be the same, but the knowledge they represent may be different, and this is not a duplication, that is a
coincidence.

> All services offered by a module should be visible through a uniform notation, which does not betray whether they are
> implemented through storage of through computation.

**Make it easy to reuse.** You should foster an environment where it is easier to find and reuse existing stuff than to
write it yourself. If it isn't easy, people will not do it. And if you fail to reuse, you risk duplicating knowledge.

Two or more things are orthogonal if changes in one do not affect any of the others. In a well-designed system, the
database code will be orthogonal to the user interface - you can change the interface without affecting the database,
and swap databases without changing the interface. Non-orthogonal systems are more complex to change and control.

**Eliminate effects between unrelated things.** We want to design components that are self-contained - independent and
with a single, well-defined purpose.

When components are well isolated from one another, you know that you can change one without having to worry about the
rest. As long as you don't change that component's external interfaces, you can be confident that you will not cause
problems that ripple through the entire system.

Modular, component-based, layered systems -> these are orthogonal systems.

- Keep your code decoupled - write shy modules, modules that don't reveal anything unnecessary to other modules and that
  don't rely on other modules' implementations. If you need to change an object's state, get the other object to do it
  for you.
- Avoid global data - in general, your code is easier to understand and maintain if you explicitly pass any required
  context into your modules.
- Avoid similar functions - duplicate code is a symptom of structural problems.

**There are no final decisions.** The mistake lies in assuming that any decision is cast in stone - and not in preparing
for the contingencies that might arise. Think of decisions as being written in the sand at the beach. A big wave can
come along and wipe them out at any time.

**Forgo following fads.** Choose architecture based on fundamentals, not fashion. No one knows what the future may hold.

**Use tracer bullets to find the target.** Look for important requirements, the one that define the system. Look for
areas where you have doubts, and where you see the biggest risks. Then prioritize your development so that these are the
first areas you code. Benefits of the tracer code:

- Users get to see something working early.
- Developers build a structure to work in.
- You have an integration platform.
- You have something to demonstrate.
- You have a better feel for progress.

Prototyping generates disposable code. Tracer code is lean but complete, and forms part of the skeleton of the final
system. Think of prototyping as the reconnaissance and intelligence gathering that takes place before a single tracer
bullet is fired.

Prototypes are designed to answer just a few questions, so they are much cheaper and faster to develop than applications
that go into production. You can prototype: architecture, new functionality in an existing system, structure or contents
of external data, third-party tools or components, performance issues, user interface design.

**Prototype to learn.** Prototyping is a learning experience. Its value lies not in the code produced, but in the lesson
learned. That's really the point of prototyping. It is easy to become mislead by the apparent completeness of a
demonstrated prototype, and project sponsors or management may insist on deploying the prototype. Remind them that you
can build a great prototype of a new car out of balsa wood and duct tape, but you wouldn't try to drive it in rush-hour
traffic.

If you feel there is a strong possibility in your environment or culture that the purpose of prototype code may be
misinterpreted, you may be better off with the tracer bullet approach.

**Program close to the problem domain.** Try to write code using the vocabulary of the application domain.

**Estimate to avoid surprises.** Estimate before you start. You will spot potential problems up front.

Basic estimating trick: ask someone who's already done it. Before you get too committed to model building, cast around
for someone who has been in a similar situation in the past. See how their problems got resolved.

Model building can be both creative and useful in the long term. Often, the process of building the model leads to
discoveries of underlying patterns and processes that weren't apparent on the surface. Building the model introduces
inaccuracies into the estimating process.

_PERT - Program Evaluation Review Technique_ - an estimating methodology, every PERT task has an optimistic, a most
likely, and a pessimistic estimate. Using a range of values like this is a great way to avoid one of the most common
causes of estimation error - padding a number because you are unsure.

**Iterate the schedule with the code.** Make the management understand that the team, their productivity, and the
environment will determine the schedule. By formalizing this, and refining the schedule as part of each iteration, you
will be giving them the most accurate scheduling estimates you can.

## Chapter 3: The Basic Tools

Tools amplify your talent. The better your tools, and the better you know how to use them, the more productive you can
be.

**Keep knowledge in plain text.** Text will not become obsolete. Make plain text understandable to humans.

**Always use version control.** Make sure that everything is under version control: documentation, phone number lists,
memos to vendors, makefiles, build and release procedures - everything.

**Fix the problem, not the blame.** It doesn't really matter whether the bug is your fault or someone else's.

**Don't panic.** The first rule of debugging. Don't waste a single neutron on the train of thought that begins "but that
can't happen" because clearly it can, and has.

**Failing test before fixing code.** We want a bug that can be reproduced with a single command. It is a lot harder to
fix a bug if you have to go through 15 steps to get to the point where the bug shows up.

**Read the damn error message.** Most exceptions tell both what failed and where it failed.

Binary search can be used for finding releases that caused the error, determining minimal subset of values that cause
program to fail.

**Select isn't broken.** It is possible that a bug exists in the OS, the compiler, or a third-party product - but this
should not be your first thought. It is much more likely that the bug exists in the application code under development.

**Don't assume it - prove it.** Don't gloss over a routine or piece of code involved in the bug because you "know" it
works. Prove it. Prove it in this context, with this data, with these boundary conditions.

## Chapter 4: Pragmatic Paranoia

**You can't write perfect software.** Perfect software doesn't exist. Pragmatic Programmers don't trust themselves.
Knowing that no one writes perfect code, including themselves. Pragmatic Programmers build in defenses against their own
mistakes.

**Design with contracts.** Be strict in what you will accept before you begin, and promise as little as possible in
return. Remember, if your contract indicates that you will accept anything and promise the world in return, you have got
a lot of code to write.

**Crash early.** Don't catch or rescue all exceptions, re-raising them after writing some kind of message. Do not
eclipse code by the error handling. Without exception handling code is less coupled. Crashing often is the best thing
you can do. The Erland and Elixir languages embrace this philosophy.

When your code discovers that something that was supposed to be impossible just happened, your program is no longer
viable. Anything it does from this point forward becomes suspect, so terminate it as soon as possible.

**Use assertions to prevent the impossible.** Whenever you find yourself thinking "but of course that could never
happen" add code to check it. Assertions are also useful checks on an algorithm's operation. Assertions check for things
that should never happen. LEAVE ASSERTIONS TURNED ON.

**Finish what you start.** It simply means that the function or object that allocates a resource should be responsible
for deallocating it.

**Take small steps - always.** Always take small, deliberate steps, checking for feedback and adjusting before
proceeding. Consider that the rate of feedback is your speed limit. You never take on a step or a task that is "too big"
. The more you have to predict what the future will look like, the more risk you incur that you will be wrong. Instead
of wasting effort designing for an uncertain future, you can always fall back on designing your code to be replaceable.

Making code replaceable will also help with cohesion, coupling, and DRY, leading to a better design overall.

## Chapter 5: Bend, or Break

Decoupling shows how to keep separate concepts separate, decreasing coupling. Coupling is the enemy of change, because
it links together things that must change in parallel.

When you are designing bridges, you want them to hold their shape - you need them to be rigid. But when you are
designing software that you will want to change, you want exactly the opposite - you want it to be flexible.

**Decoupled code is easier to change.**

**Tell, don't ask.** (The Law of Demeter) You shouldn't make decisions based on the internal state of an object abd then
update the object. Doing so totally destroys the benefits of encapsulation, and, in doing so, spreads the knowledge of
the implementation thought the code.

A method defined in a class C should only call:

- Other instance methods
- Its parameters
- Methods in objects it creates
- Global variables

**Don't chain method calls.** (Something simpler than the Law of Demeter.) Try not to have more than one "." when you
access something. The rule doesn't apply if the things you are changing are really unlikely to change (e.g. libraries
that come with the language).

**Avoid global data.** It is like adding extra parameter to every method.

**If it is important enough to be global, wrap it in an API.** Any mutable external resource is global data (database,
file system, service API, ...). Always wrap these resources behind code that you control.

Keeping your code shy - having it deal with things it directly knows about, will help keep you applications decoupled,
and that will make them more amenable to change.

Publish/Subscribe generalizes the observer pattern, at the same time solving the problems of coupling and performance.

Streams let us treat events as if they were a collection of data. It's as if we had a list of events, which got longer
when new events arrive. We can treat streams like any other collection (manipulate, filter, combine).

Baseline for reactive event handling: reactivex.io

**Programming is about code, but programs are about data.** Start designing using transformations (unix-like pipelines).
Using pipelines means that you are automatically thinking in terms of transforming data.

**Don't hoard state, pass it around.** Functions greatly reduce coupling. A function can be used (and reused) anywhere
its parameters match the output of some other function. There is still a degree of coupling, but it is more manageable
than the OO-style of command and control.

Thinking of code as a series of nested transformations can be a liberating approach to programming. It takes a while to
get used to, but once you have developed the habit you will find your code becomes cleaner, your functions shorter, and
your designs flatter.

**Don't pay inheritance tax.** Inheritance is coupling. Not only is the child class coupled to the parent, the parent's
parent, and so on, but the code that uses the child is also coupled to al the ancestors.

Alternatives to inheritance:

- interfaces and protocols - these declarations create no code. We can use them to create types, and any class that
  implements the appropriate interface will be compatible with that type.
- delegation - has-a is better than is-a. If parent has 20 methods, and the subclass wants to make use of just 2 of
  them, its objects will still have the other 18 just lying around and callable.
- mixins and traits - use them to share functionality. The basic ide is simple, we want to be able to extend classes and
  objects with new functionality without using inheritance. So we create a set of these functions, give that set a name,
  and then somehow extend a class with them.

**Prefer interfaces to express polymorphism.** Interfaces and protocols give us polymorphism without inheritance.

**Parametrize your app using external configuration.** When code relies on values that may change after the application
has gone live, keep those values external to the app. Keep the environment and customer-specific values outside the
app (credentials, logging levels, IP addresses, validation parameters, external rates - e.g. tax rates, formatting
details, license keys).

While static configuration is common, we currently favor a different approach. We still want configuration data kept
external to the application, but rather than in a flat file ro database, we would like to see it stored behind a service
API.

## Chapter 6: Concurrency

Concurrency - when the execution of two or more pieces of code act as if they run at the same time (context switching).
Parallelism is when they do run at the same time (multiple cores).

Temporal coupling - coupling in time. Temporal coupling happens when your code imposes a sequence on things that is not
required to solve the problem.

**Analyze workflow to improve concurrency.** Find out what can happen at the same time, and what must happen in a strict
order. One way to do this is to capture the workflow using a notation such as the activity diagram.

**Shared state is incorrect state.** A semaphore is a thing that only one person can own at a time. You can create a
semaphore and the use it to control some other resource.

**Random failures are often concurrency issues.** Whenever tow or more instances or your code can access some resource
at the same time, you are looking at a potential problem.

**Use actors for concurrency without shared state.** Actors execute concurrently, asynchronously and share nothing. An
actor is an independent virtual processor with its own local state. Each actor has a mailbox. When a message appears in
the mailbox and the actor is idle, it kicks into life and processes the message. When it finishes processing, it
processes another message in the mailbox, or goes back to sleep.

**Use blackboards to coordinate workflow.** Order of data arrival is irrelevant - when a fact is posted it can trigger
the appropriate rules. The output of any rules can post to the backboard and cause the triggering of yet more applicable
rules.

## Chapter 7: While You Are Coding

**Listen to your inner lizard.** When it feels like your code is pushing back, it is really your subconscious trying to
tell you something is wrong.

Learning to listen to your gut feeling when coding is an important skill to foster. But it applies to the bigger picture
as well. Sometimes a design just feels wrong, or some requirements makes you feel uneasy. Stop and analyze these
feelings. If you are in a supportive environment, express them out loud. Explore them.

**Don't program by coincidence.** Don't rely on luck and accidental success.

- Always be aware of what you are doing.
- Can you explain the code, in detail, to a more junior programmer? If not, perhaps you are relying on coincidences.
- Don't code in dark. If you are not sure why it works, you will not know why it fails.
- Proceed from a plan.
- Don't depend on assumptions. If you can't tell something is reliable, assume the worst.
- Document your assumptions.
- Don't just test your code, but test your assumptions as well. Don't guess, try it. Write an assertion to test your
  assumptions. If your assertion is right, you have improved the documentation in your code. If you discover your
  assumption is wrong, then count yourself lucky.
- _Don't be a slave to history. Don't let existing code dictate future code. All code can be replaced if it is no longer
  appropriate._

**Estimate the order of your algorithms.** Estimate the resources that algorithms use - time, processor, memory, and so
on. When you write anything containing loops or recursive calls, check the runtime and memory requirements. When a more
detailed analysis is needed - use Big-O notation.

Think of the _O_ as meaning _on the order of_. Big-O is never going to give you actual numbers for time of memory of
whatever - it simply tells you how these values will change as the input changes.

Common sense estimation:

- simple loops - _O(n)_
- nested loops - _O(n^2)_
- binary chop - _O(log n)_
- divide and conquer - _O(n log n)_
- combinatorics - running time might run out of time, _O(n!)_

**Test your estimates.** The fastest one is not always the best for the job. Given a small input set, a straightforward
insertion sort will perform just as well as a quicksort, and will take less time to write and debug.

Be wary of _premature optimisation_. It is always a good idea to make sure an algorithm really is a bottleneck before
investing your precious time trying to improve it.

Refactoring: As a program evolves, it will become necessary to rethink earlier decisions and rework portions of code.
This process is perfectly natural. Code needs to evolve - it is not a static thing.

The most common metaphor for software development is building construction. Rather than a construction, software is more
like a gardening - it is more organic than concrete.

Refactoring is not intended to be a special, high-ceremony, once-in-a-while activity. Refactoring is a day-to-day
activity, taking low risk small steps. It is a targeted, precise approach to help keep the code easy to change. You need
good, automated unit testing that validates the behavior of the code.

Any number of things may cause code to qualify for refactoring:

- duplication
- non-orthogonal design - change to one thing affects the other
- outdated knowledge
- usage - some features may be more important than originally thought
- performance
- the test pass - when you have added a small amount of code, and that extra test passes, you have a great opportunity
  to dive in and tidy up what you just wrote.

**Refactor early, refactor often.** Time pressure is often used as an excuse for not refactoring. Fail to refactor now,
and there will be a far greater time investment to fix the problem down the road.

**Explain this principle to others by using a medical analogy: think of the code that needs refactoring as "a growth".
Removing it requires invasive surgery. You can go in now, and take it out while it is still small. Or, you could wait
while it grows and spreads - but removing it then will be both more expensive and more dangerous. Wait even longer, and
you may lose the patient entirely.**

How to refactor without doing more harm than good:

1. Don't try to refactor and add functionality at the same time.
2. Make sure you have good tests before you begin refactoring. Run the tests as often as possible.
3. Take short, deliberate steps. Refactoring often involves making many localized changes that result in a larger-scale
   change.

Don't live with broken windows.

**Testing is not about finding bugs.** Major benefits of testing happen when you think about and write the tests, not
when you run them.

**A test is the first user of your code.** Testing is vital feedback that guides your coding. _A function or method that
is tightly coupled to other code is hard to test, because you have to set up all that environment._ Making your stuff
testable also reduces its coupling.

**Build end-to-end, not top-down or bottom up.** Build small pieces of end-to-end functionality, learning about the
problem as you go.

Like our hardware colleagues, we need to build testability into the software from the very beginning, and test each
piece thoroughly before trying to wire them together. Chip-level testing for hardware is roughly equivalent to unit
testing in software. Write test cases that ensure a given unit honors its contract. We want to test that the module
delivers the functionality it promises.

**Design to test.** Start thinking about testing before you write a line of code.

Approaches:

- Test first - TDD - probably the best choice in most circumstances.
- Test during - a good fallback when TDD is not useful or convenient.
- Test never - the worst choice.

**Test your software, or your users will.** Make no mistake, testing is part of programming. It is not something left to
other departments or staff. Testing, design, coding - it is all programming.

**Use property-based tests to validate your assumptions.** Property-based tests will try things you never thought to
try, and exercise your code in ways it wasn't meant to be used. For python use _Hypothesis_ framework. Hypothesis gives
you a minilanguage for describing the data it should generate.

**Keep it simple and minimize attack surfaces.** Bear in mind these security principles:

1. Minimize Attack Surface Area
    1. Code complexity makes the attack surface larger, with more opportunities for unanticipated side effects. Think of
       complex code as making the surface area more porous and open to infection. Simple, smaller code is better.
    2. Never trust data from an external entity, always sanitize it before passing it on to a database, view rendering,
       or other processing.
    3. Unauthenticated services are an attack vector. Any user anywhere in the world cal call unauthenticated services.
    4. Keep the number of authenticated users at an absolute minimum. Cull unused, old, or outdated users and services.
       If an account with development services is compromised, your entire product is compromised.
    5. Don't give too much information about an error in the response.
2. Principle of Least Privilege - Every program and every privileged user of the system should operate using the least
   amount of privilege necessary to complete the job.
3. Don't leave personally identifiable information, financial data, passwords, or other credentials in plain text. Don't
   check in secrets, API keys, SSH keys, encryption passwords or other credentials alongside your code in version
   control.
4. Apply security patches quickly. The largest data breaches in history were caused by systems that were behind on their
   updates.

You don't want to do encryption yourself. Even the tiniest error can compromise everything. Rely on reliable things.
Take the more pragmatic approach and let someone else worry about it and use a third party authentication provider.

**Name well, rename when needed.** Things should be named according to the role they play in your code. Honor the local
culture (snake_case vs CamelCase vs ...). Every project has its own vocabulary - jargon words that have a special
meaning to the team. It is important everyone on the team knows what these words mean. One way is to encourage a lot of
communication, another way is to have a project glossary.

When you see a name that no longer expresses the intent, or is misleading or confusing, fix it.

## Chapter 8: Before the Project

**No one knows exactly what they want.** Requirements rarely lie on the surface. Normally, they are buried deep beneath
layers of assumptions, misconceptions, and politics.

**Programmers help people understand what they want.** Our job is to help people understand what they want.

**Requirements are learned in a feedback loop.** Your role is to interpret what the client says and to feed back to them
the implications. This is both an intellectual proces and a creative one. Your job is to help the client understand the
consequences of their stated requirements.

**Work with the user to think like a user.** There is a simple technique for getting inside your client's heads: become
a client.

**Policy is metadata.** Don't hardcode policy into a system, instead express it as metadata used by the system.

**Use a project glossary.** Create and maintain a project glossary - one place that defines all the specific terms and
vocabulary used in a project. It is hard to succeed on a project if users and developers call the same thing by
different names.

**Don't think outside the box - find the box.** When faced with an impossible problem, identify the real constraints.
Ask yourself: Does it have to be done this way? Does it have to be done at all?

Sometimes you find yourself working on a problem that seems much harder than you thought it should be. You may think
this particula problem is "impossible". This is an ideal time to do something else for a while. Sleep on it, go walk the
dog. People who were distracted did better on a complex problem-solving task than people who put in conscious effort. If
you are not willing to drop the problem for a while, the next best thing is probably finding someone to explain it to (
rubber duck).

Conway's Law: "_Organizations which design systems are constrained to produce designs which are copies of the
communication structures of these organizations_".

**Don't go into code alone.**

Pair programming - the inherited peer-pressure of a second person helps against moments of weakness and bad habits of
naming variables such as foo and such. You are less inclined to take a potentially embarrassing shortcut when someone is
actively watching, which also results in higher-quality code.

Mob programming - it is an extension of pair programming that involves more than just two developers. You can think of
mob programming as tight collaboration with live coding.

**Agile is not a noun, agile is how you do things.** Agile is an adjective. Remember the values from the manifesto:

1. Individuals and interactions over processes and tools
2. Working software over comprehensive documentation
3. Customer collaboration over contract negotiation
4. Responding to change over following a plan

Agility is all about responding to change, responding to the unknowns you encounter after you set out.

Recipe for working in an agile way:

1. Work out where you are.
2. Make the smallest meaningful step towards where you want to be.
3. Evaluate where you end up, and fix anything you broke (this requires a good design, because it is easier to fix good
   design).

## Chapter 9: Pragmatic Projects

**Maintain small, stable teams.** A pragmatic team is small, under 10-12 or so members. Members come and go rarely.
Everyone knows everyone well, trust each other, and depends on each other.

Quality is a team issue. The most diligent developer placed on a team that just doesn't care will find it difficult to
maintain the enthusiasm needed to fix niggling problems. Teams as a whole should not tolerate broken windows - those
small imperfections that no one fixes.

**Schedule to make it happen.** If your team is serious about improvement and innovation, you need to schedule it.
Trying to get things done "whenever there is a free moment" means they will never happen. Whatever sort of backlog or
task list or flow you are working with, don't reserve it for only feature development. The team works on more than just
new features:

- old systems maintenance
- process reflection and refinement - continuous improvement can only happen when you take the time to look around
- new tech experiments - try new stuff and analyze results
- learning and skill improvements - brown bags, training sessions

**Organize fully functional teams.**

There is a simple marketing trick that helps teams communicate as one - generate a brand. When you start a project, come
up with a name for it, ideally off-the-wall. Spend 30 minutes coming up with a zany logo, and use it, but it gives your
team an identity to build on, and the world something memorable to associate with your work.

Good communication is key to avoiding problems. You should be able to ask a question of team members and get a
more-or-less instant reply. If you have to wait for a week for the team meeting to ask your question or share your
status, that is an awful lot of friction.

**Do what works, not what is fashionable.** Ask yourself, why are you even using that particular development
method/framework/whatever? Does it work well for you? Or it was adopted just because it was being used by the latest
internet-fueled story?

You want to take the best pieces from any particular methodology and adapt the for use. No one fits for all, and current
methods are far from complete, so you will need to look at more than just one popular method. That is very different
mindset from "but Scrum/Lean/Kanban/XP/agile does it this way...".

The goal isn't to do Scrum/do agile/ do Lean or what-have-you. The goal is to be in a position to deliver working
software that gives the users some new capability at a moment's notice. Not weeks, months, or years from now. If you are
delivering in years, they shorten the cycle to months. From months, cut it down to weeks. From a four-week sprint, try
two. From a two-week sprint, try one. Then daily. Then, finally, on demand. Note that being able to deliver on demand
deos not mean you are forced to deliver every minute of every day. You deliver when the users need it, when it makes
business sense to do so.

**Deliver when users need it.** In order to move to this style of continuous development, you need to a rock-solid
infrastructure.

Once your infrastructure is in order, you need to decide how to organize the work. Beginners might want to start with
Scrum for project management. More disciplined and experienced teams might look to Kanban and Lean techniques. But
investigate it first. Try these approaches for yourself.

**Use version control to drive builds, tests and releases.** Build, test, and deployment are triggered via commits or
pushes version control, and built in a container in the cloud. Release to staging or production is specified by using a
tag in your version control system.

**Test early, test often, test automatically.** A good project may well have more test code than production code. The
time it takes to produce this test code is worth the effort. It ends up being much cheaper in the long run, and you
actually stand a chance of producing a product with close to zero defects.

**Coding ain't done till all the tests run.** The automatic build runs all available tests. It is important to aim to "
test for real" - the test environment should match the production environment closely. The build may cover several major
types of software testing: unit testing, integration testing, validation and verification and performance testing.

**Use Saboteurs to test your testing.** Because we can't write perfect software, we can't write perfect tests. We need
to test the tests. After you have written a test to detect a bug, cause the bug deliberately and make sure the test
complains. If you are really serious about testing, take a separate branch, introduce bugs on purpose and verify that
the tests will catch them. At a higher level, you can use something like Netflix's Chaos Monkey.

**Test state coverage, not code coverage.** Even if you happen to hit every line of code, that is not whole picture.
What is important is the number of states that your program may have. States are not equivalent to lines of code. A
great wat to explore how your code handles unexpected states is to have a computer generate those states (property-based
testing).

**Find bug once.** Once a human tester finds a bug, it should be the last time a human tester finds that bug. If a bug
slips through the net of existing tests, you need to add a new test to trap it next time.

**Don't use manual procedures.** Tracking down differences of any one component usually reveals a surprise. People
aren't as repeatable as computers are. Nor should we expect them to be. Everything should depend on automation. Project
build, deployment, ... Once you introduce manual steps, you have broken a very large window.

**Delight users, don't just deliver code.** If you want to delight your client, forge a relationship with them where you
can actively help solve their problems. Be a _Problem Solver_ (not Software Engineer/Developer). That is the essence of
a Pragmatic Programmer.

**Sign your work.** If we are responsible for a design, or a piece of code, we do a job we can be proud of. Artisans of
an earlier age were proud to sign their work. You should be, too.

However, you shouldn't jealously defend your code against interlopers, by the same token, you should treat other
people's code with respect. Mutual respect among the developers is critical to make this tip work.

We want to see pride in ownership "_I wrote this, and I stand behind my work_". Your signature should come to be
recognized as an indicator of quality. People should see your name on a piece of code and expect it to be solid, well
written, tested and documented.

A really professional job. Written by a professional. A Pragmatic Programmer.

## Postface

We have a duty to ask ourselves two questions about every piece of code we deliver:

1. Have I protected the user?
2. Would I use this myself?

**First, do no harm.** Would I be happy to be a user of this software? Do I want my details shared? Do I want my
movements to be given to retail outlets? Would I be happy to be driven by this autonomous vehicle? Am I comfortable
doing this? If you are involved in the project, you are just as responsible as the sponsors.

**Don't enable scumbags.**

**It is your life. Share it. Celebrate. Build It. AND HAVE FUN.** You are building the future. Your duty is to make a
future that we would all want to inhabit. Recognize when you are doing something against this ideal, and have courage to
say no.
