[go back](https://github.com/pkardas/learning)

# The Pragmatic Programmer: journey to mastery, 20th Anniversary Edition

Book by David Thomas and Andrew Hunt

- [Chapter 1: A Pragmatic Philosophy](#chapter-1-a-pragmatic-philosophy)
- [Chapter 2: A Pragmatic Approach](#chapter-2-a-pragmatic-approach)
- [Chapter 3: The Basic Tools](#chapter-3-the-basic-tools)
- [Chapter 4: Pragmatic Paranoia](#chapter-4-pragmatic-paranoia)
- [Chapter 5: Bend, or Break](#chapter-5-bend-or-break)

## Chapter 1: A Pragmatic Philosophy

**You Have Agency.** It is your life. You own it. You run it. You create it. This industry gives you a remarkable set of
opportunities. Be proactive, and take them.

The team needs to be able to trust you and rely on you, and you need to be comfortable relying on each of them as well.
In a healthy environment based in trust, you can safely speak your mind, present your ideas, and rely on your team
members who can in turn rely on you.

**Provide options, don't make lame excuses.** Instead of excuses provide options. Don;t say it can't be done: explain
what can be done to salvage the solution. When you find yourself saying "_I don't know_" be sure to follow it up with
"_--but I'll find out_". It is a great way to admit what you don;t know, but then take responsibility like a pro.

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
for.Develop it well. Once you have got it, show people, and let them marvel. Sit back and wait for them to start asking
you to add the functionality you originally wanted. Show them a glimpse of the future, and you will get them to rally
around.

**Remember the Big Picture.** Constantly review what is happening around you, not just what you personally are doing.
Projects slowly and inexorably get totally out of hand.Most software disasters start out too small to notice, and most
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
   another organization may be aligned with your won, or not.
3. What is the context? - everything occurs in its own context. Good for someone, doesn't mean it is good for you.
4. WHy is this a problem? - is there an underlying model? How does the underlying model work?

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

- Keep your code decoupled - write shy modules, modules that don;t reveal anything unnecessary to other modules and that
  don't rely on other modules' implementations.If you need to change an object's state, get the other object to do it
  for you.
- Avoid global data - in general, your code is easier to understand and maintain if you explicitly pass any required
  context into your modules.
- Avoid similar functions - duplicate code is a symptom of structural problems.

**There are no final decisions.** The mistake lies in assuming that any decision is cast in stone - and not in preparing
for the contingencies that might arise. Think of decisions as being written in the sand at the beach. A big wave can
come along and wipe them out at any time.

**Forgo following fads.** Choose architecture based on fundamentals, not fashion. No one knows what the future may hold.

**Use tracer bullets to fin the target.** Look for important requirements, the one that define the system. Look for
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
for someone who has been in a similar situation in teh past. See how their problems got resolved.

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

Tools amplify your talent. The better your tools, and the better your tools, and the better you know how to use them,
the more productive you can be.

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

Publish/Subscribe generalizes the observed pattern, at the same time solving the problems of coupling and performance.

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
