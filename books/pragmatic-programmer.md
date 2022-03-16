[go back](https://github.com/pkardas/learning)

# The Pragmatic Programmer: journey to mastery, 20th Anniversary Edition

Book by David Thomas and Andrew Hunt

- [Chapter 1: A Pragmatic Philosophy](#chapter-1-a-pragmatic-philosophy)
- [Chapter 2: A Pragmatic Approach](#chapter-2-a-pragmatic-approach)

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
