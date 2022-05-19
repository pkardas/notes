[go back](https://github.com/pkardas/learning)

# Python Testing with Pytest: Simple, Rapid, Effective, and Scalable

Book by Brian Okken

Code here: [click](.)

- [Chapter 1: Getting Started with pytest](#chapter-1-getting-started-with-pytest)
- [Chapter 2: Writing Test Functions](#chapter-2-writing-test-functions)
- [Chapter 3: pytest Fixtures](#chapter-3-pytest-fixtures)
- [Chapter 4: Built-in fixtures](#chapter-4-built-in-fixtures)
- [Chapter 5: Parametrization](#chapter-5-parametrization)
- [Chapter 6: Markers](#chapter-6-markers)
- [Chapter 7: Strategy](#chapter-7-strategy)
- [Chapter 8: Configuration Files](#chapter-8-configuration-files)
- [Chapter 9: Coverage](#chapter-9-coverage)
- [Chapter 10: Mocking](#chapter-10-mocking)
- [Chapter 11: tox and Continuous Integration](#chapter-11-tox-and-continuous-integration)
- [Chapter 12: Testing Scripts and Applications](#chapter-12-testing-scripts-and-applications)
- [Chapter 13: Debugging Test Failures](#chapter-13-debugging-test-failures)
- [Chapter 14: Third-Party Plugins](#chapter-14-third-party-plugins)
- [Chapter 15: Building Plugins](#chapter-15-building-plugins)
- [Chapter 16: Advanced Parametrization](#chapter-16-advanced-parametrization)

## Chapter 1: Getting Started with pytest

Part of pytest execution is test discovery, where pytest looks for `.py` files starting with `test_` or ending
with `_test`. Test methods and functions must start with `test_`, test classes should start with `Test`.

Flag `--tb=no` turns off tracebacks.

Test outcomes:

- PASSED (.)
- FAILED (F)
- SKIPPED (S) - you can tell pytest to skip a test by using `@pytest.mark.skip` or `@pytest.mark.skipif`
- XFAIL (x) - the test was not supposed to pass (`@pytest.mark.xfail`)
- XPASS (X) - the teas was marked with xfail, but it ran and passed
- ERROR (E) - an exception happened during the execution

## Chapter 2: Writing Test Functions

Writing knowledge-building tests - when faced a new data structure, it is often helpful to write some quick tests so
that you can understand how the data structure works. The point of these tests is to check my understanding of how the
structure works, and possibly to document that knowledge for someone else or even for a future me.

`pytest` includes a feature called "_assert rewriting_", that intercepts _assert_ calls and replaces them with something
that can tell you more about why your assertions failed.

`pytest.fail()` underneath raises an exception. When calling this function or raising an exception directly, we don't
get the wonderful "assert rewriting" provided by the `pytest`.

Assertion helper function - used to wrap up a complicated assertion check. `__tracebackhide__ = True` the effect will be
that failing tests will not include this function in the traceback.

Flag `--tb=short` - shorted traceback format.

Use `pytest.raises` to test expected exceptions. You can check error details by using `match`, `match` accepts regular
expressions and matches it with the exception message. You can also use `as exc_info` (or any other variable name) to
interrogate extra parameters.

Arrange-Act-Assert or Given-When-Then patterns are about separating test into stages. A common anti-pattern is to have
more "Arrange-Assert-Act-Assert-Act-Assert-...". Test should focus on testing one behavior.

`pytest` allows to group tests with classes. You can utilize class hierarchies for inherited methods. However, book
author doesn't recommend tests inheritance because they easily confuse readers. Use classes only for grouping.

`pytest` allows to run a subset of tests, examples:

- `pytest ch2/test_classes.py::TestEquality::test_equality`
- `pytest ch2/test_classes.py::TestEquality`
- `pytest ch2/test_classes.py`
- `pytest ch2/test_card.py::test_defaults`
- `pytest ch2/test_card.py`

`-k` argument takes an expression, and tells pytest to run tests that contain a substring that matches the expression,
examples:

- `pytest -v -k TestEquality`
- `pytest -v -k TestEq`
- `pytest -v -k equality`
- `pytest -v -k "equality and not equality_fail"` (_and, or, parenthesis, not_ are allowed to create complex
  expressions)

## Chapter 3: pytest Fixtures

Fixtures are helper functions, run by pytest before (and sometimes after) the actual test functions. Code in the fixture
can do whatever you want it to do. Fixture can be also used to refer to the resource that is being set up by the fixture
functions.

`pytest` treats exceptions differently during fixtures compared to during a test function.

- FAIL - the failure is somewhere in the test function
- ERROR - the failure is somewhere in the fixture

Fixtures help a lot when dealing with databases.

Fixture functions run before the tests that use them. If there is a `yield` in the function, it stops there, passes
control to the tests, and picks up on the next line after the tests are done. The code above `yield` is "setup" and the
code after `yield` is "teardown". The code after `yield`, is guaranteed to run regardless of what happens during the
tests.

Flag `--setup-show` shows us the order of operations of tests and fixtures, including the setup and teardown phases of
the fixtures.

The scope dictates how often the setup and teardown get run when it is used by multiple test functions:

- _function_ - (default scope) run once per test function. The setup is run before each test using the fixture. The
  teardown is run after each test using the fixture.
- _class_ - run once per test class, regardless of how many test methods are in the class.
- _module_ - run once per module, regardless of how many test functions/methods of other fixtures in the module use it.
- _package_ - run once per package, regardless of how many test functions/methods of other fixtures in the package use
  it.
- _session_ - run once per session, all test methods/functions using a fixture of session scope share one setup and
  teardown call.

The scope is set at the definition of a fixture, and not at the place where it is called `@pytest.fixture(scope=...)`.

Fixtures can only depend on other fixtures of their same scope or wider.

`conftest.py` is considered by `pytest` as a "local plugin". Gets read by pytest automatically. Use `conftest.py` to
share fixtures among multiple test files. We can have `conftest.py` files at every level of our test directory. Test can
use any fixture that is in the same test module as a test function, or in a `conftest.py` file in the same directory (or
in the parent directory).

Use `--fixtures` to show list of all available fixtures our test can use.

Use `--fixtures-per-test` to see what fixtures are used by each test and where the functions are defined.

Using multiple stage fixtures can provide some incredible speed benefits and maintain test order independence.

It is possible to set fixture scope dynamically, e.g. by passing a new flag as an argument.

Use `autouse=True` to run fixture all the time. The `autouse` feature is good to have around. But it is more of an
exception than a rule. Opt for named fixtures unless you have a really great reason not to.

`pytest` allows you to rename fixtures with a `name` parameter to `@pytest.fixture`.

## Chapter 4: Built-in fixtures

`tmp path` and `tmp_path_factory` - used to create temporary directories.

- `tmp path`
    - function scope
- `tmp_path_factory`
    - session scope
    - you have to call `mktemp` to get a directory
- `tmpdir_factory`
    - similar to `tmp_path_factory`, but instead of `Path`, returns `py.path.local`

`capsys` - enables the capturing of writes to `stdout` and `stderr`.

- `capfd` - like `capsys`, but captures file descriptors 1 and 2 (stdout and stderr)
- `capsysbinary` - `capsys` captures text, `capsysbinary` captures binary
- `caplog` - captures output written with the logging package

A "monkey patch" is a dynamic modification of a class or module during runtime. "Monkey patching" is a convenient way to
take over part of the runtime environment of the application code and replace it with entities that are more convenient
for testing.

`monkeypatch` - used to modify objects, directories, evn variables. When test ends, the original unpatched code is
restored. It has the following functions:

- `setattr` - sets an attribute
- `delattr` - deletes an attribute
- `setitem` - sets a directory entry
- `delitem` - deletes a directory entry
- `setenv` - sets an env variable
- `delenv` - deletes an env variable
- `syspath_prepend` - prepends, `path` to `sys.path`, which is Python's lis of import locations
- `chdir` - changes the current working directory

If you start using monkey-patching:

- you will start to understand this
- you will start to avoid mocking and monkey-patching whenever possible

DESIGN FOR TESTABILITY. A concept borrowed from hardware designers. Concept of adding functionality to software to make
it easier to test.

More fixtures: https://docs.pytest.org/en/6.2.x/fixture.html or run `pytest --fixtures`.

## Chapter 5: Parametrization

Parametrized tests refer to adding parameters to our test functions and passing in multiple sets of arguments to the
test to create new test cases.

With fixture parametrization, we shift parameters to a fixture, `pytest` will then call the fixture once each for every
set of values we provide.

Fixture parametrization has the benefit of having a fixture run for each set of arguments. This is useful if you have
setup or teardown code that needs to run for each test case - e.g. different database connection, different file
content, ...

`pytest_generate_tests` - hook function. Allows you to modify the parametrization list at test collection time in
interesting ways.

## Chapter 6: Markers

Markers are a way to tell pytest there is something special about a particular test. You can think of them like tags or
labels. If some tests are slow, you can mark them with `@pytest.mark.slow` and have pytest skip those tests when you are
in hurry. You can pick a handful of tests out of a test suite and mark them with `@pytest.mark.smoke`.

Built-in markers:

- `@pytest.mark.filterwarnings(warning)` - adds a warning filter to the given test
- `@pytest.mark.skip(reason=None)` - skip the test with an optional reason
- `@pytest.mark.skipif(condition, ..., *, reason)` - skip the test if any of the conditions are true
- `@pytest.mark.xfail(condition, ..., *, reason, run=True, raises=None, stric=xfail_strict)` - we can expect the test to
  fail. If we want to run all tests, even those that we know will fail, we can use this marker.
- `@pytest.mark.parametrize(argnames, argvalues, indirect, ids, scope)` - call a test function multiple times
- `@pytest.mark.usefixtures(fixturename1, fizxturename2, ...)` - marks tests as needing all rhe specified fixtures

Custom markers - you need to add `pytest.ini` with marker definition, some ideas for markers:

- `@pytest.mark.smoke` - run `pytest -v -m smoke` to run smoke tests only
- `@pytest.mark.exception` - run `pytest -v -m exception` to run exception-related tests only

Custom markers shine when we have more files involved. We can also add markers to entire files or classes. We can even
put multiple markers on a single test.

File-level marker:

```python
pytestmark = [pytest.mark.marker_one, pytest.mark.marker_two]
```

When filtering tests using markers, it is possible to combine markers and use a bit of logic, just like we did with
the `-k` keyword, e.g. `pytest -v -m "custom and exception"`, `pytest -v -m "finish and not smoke"`.

`--strict-markers` - raises an error when mark was not found (by default a warning is raised). Also, an error is raised
at collection time, not at run time - error is reported earlier.

Markers can be used in conjunction with fixtures.

Use `--markers` to list all available markers.

## Chapter 7: Strategy

_Testing enough to sleep at night_: The idea of testing enough so that you can sleep at night may have come from
software systems where developers have to be on call to fix software if it stops working in the middle of the night. It
has been extended to including sleeping soundly, knowing that your software is well tested.

Testing through the API tests most of the system and logic.

Before you create the test cases you want to test, evaluate what features to test. When you have a lot of functionality
and features to test, you have to prioritize the order of developing tests. At least a rough idea of order helps.
Prioritize using the following factors:

1. Recent - new features, new areas of code, recently modified, refactored.
2. Core - your product's unique selling propositions. The essential functions that must continue to work in order for
   the product to be useful.
3. Risk - areas of the application that pose more risk, such as areas important to customers but not used regularly by
   the development team or parts that use 3-rd party code you don't trust.
4. Problematic - functionality that frequently breaks or even gets defect reports against it.
5. Expertise - features or algorithms understood by a limited subset of people

Creating test cases.

- start with a non-trivial, "happy path" test case
- then look at test cases that represent
    - interesting set of inputs
    - interesting starting states
    - interesting end states
    - all possible error states

## Chapter 8: Configuration Files

Non-test files that affect how _pytest_ runs.

- `pytest.ini` - primary pytest configuration file that allows you to change pytest's default behavior. Its location
  also defines the pytest root directory.
- `conftest.py` - this file contains fixtures and hook functions. It can exist in at the root directory or in any
  subdirectory. It is a good idea to stick to only one `conftest.py` file, so you can find fixture definitions easily.
- `__init__.py` - when put into test subdirectories, this file allows you to have identical test file names in multiple
  test directories. This means you can have `api/test_add.py` and `cli/test_add.py` but only if you have `__init__.py`
  in both directories.
- `tox.ini`, `pyproject.toml`, `setup.cfg` - these files can take the place of `pytest.ini`

Example `pytest.ini`:

```
[pytest]              -- including `[pytest]` in `pytest.ini` allows the pytest ini parsing to treat `pytest.ini` and `tox.ini` identically
addopts =             -- enables us to list the pytest flags we always want to run in this project
    --stric-markers   -- raise an error for any unregistered marker
    --strict-config   -- raise an error for any difficulty in parsing config files
    -ra               -- display extra text summary at the end of a test run
    
testpaths = tests     -- tells the python wehere to look for tests

markers =             -- declare markers
    smoke: subset of tests
    exception: check for expected exceptions
```

Example `tox.ini`:

```
[tox]
; tox specific settings

[pytest]
addopts =
    --stric-markers
    --strict-config
    -ra
...
```

Example `pyptoject.toml`:

```
[tool.pytest.ini_options]
addopts = [
  "--stric-markers",
  "--strict-config",
  "-ra"
]

testpaths = tests 

markers =[
  "smoke: subset of tests",
  "exception: check for expected exceptions"
]
```

Example `setup.cfg`:

```
[tool:pytest]
addopts =
    --stric-markers
    --strict-config
    -ra
...
```

Even if you don't need any configuration settings, it is still a great idea to place an empty `pytest.ini` at the top of
your project, because pytest may keep searching for this file.

## Chapter 9: Coverage

Tools that measure code coverage watch your code while a test suite is being run and keep track of which lines are hit
and which are not. That measurement is called "line coverage" = "total number of lines" / "total lines of code".

Code coverage tools can also tell you if all paths are taken in control statements - "branch coverage".

Code coverage cannot tell you if your test suite is good - it can only tell you how much of the application code is
getting hit by your test suite.

`coverage.py` - preferred Python coverage tool, `pytest-cov` - popular pytest plugin (depends on `coverage.py`, so it
will be installed as well).

To run tests with `coverage.py`, you need to add `--cov` flag.

To add missing lines to the terminal report, add the `--cov-report=term-missing` flag.

`coverage.py` is able to generate HTML reports: `docker-compose run --rm book pytest --cov=src --cov-report=html`, to
help view coverage data in more detail.

`# pragra: no cover` - tells `coverage` to exclude either a single line or a block of code.

**Beware of Coverage-Driven Development!** The problem with adding tests just to hit 100% is that doing so will mask the
fact that these lines aren't being used and therefore are not needed by the application. It also adds test code and
coding time that is not necessary.

## Chapter 10: Mocking

The `mock` package is used to swap out pieces of the system to isolate bits of our application code from the rest of the
system. Mock objects are called sometimes _test doubles_, _spies_, _fakes_ or _stubs_.

Typer provides a testing interface. With it, we don't have use `subprocess.run`, which is good, because we can't mock
stuff running in a separate process.

Mocks by default accept any access. If real object allows `.start(index)`, we want our mock objects to
allow `start(index)` as well. Mock objects are too flexible by default - they will also accept `star()` - any misspelled
methods, additional parameters, really anything.

_Mock drift_ - occurs when the interface you are mocking changes, and your mock in your test code doesn't.

Use `autospec=True` - without it, mock will allow you to call any function, with any parameters, even if it doesn't make
sense for the real thing being mocked. Always use _autospec_ when you can.

**Mocking tests implementation, not behavior.** When we are using mocks in a test, we are no longer testing behavior,
but testing implementation. Focusing tests on testing implementation is dangerous and time-consuming.

_Change detector test_ - test that break during valid refactoring. When test fail whenever the code changes, they are
change detector tests, and are usually more trouble than they worth.

Mocking is useful when you need to generate an exception or make sure your code calls a particular API method when it is
supposed to, with the correct parameters.

There are several special-purpose mocking libraries:

- mocking database: `pytest-postgresql`, `pytest-mongo`, `pytest-mysql`, `pytest-dynamodb`
- mocking HTTP servers: `pytest-httpserver`
- mocking requests: `responses`, `betamax`
- other: `pytest-rabbitmq`, `pytest-soir`, `pytest-elasticsearch`, `pytest-redis`

Adding functionality that makes testing easier is part of "design for testability" and can be used to allow testing at
multiple levels or testing at a higher level.

## Chapter 11: tox and Continuous Integration

CI refers to the practice of merging all developers' code changes into a shared repository on a regular basis - often
several times a day.

Before the implementation of CI, teams used version control to keep track of code updates, and different developers
would add a feature/fix on the separate branches. Then code was merged, built, and tested. The frequency of merge varied
from "when your code is ready, merge it" to regularly scheduled merges (weekly, monthly). The merge was called
_integration_ because the code is being integrated together.

With this soft of version control, code conflicts happened often. Some merge errors were not found until very late.

CI tools build and run tests all on their own, usually triggered by a merge request. Because the build and test stages
are automated, developers can integrate more frequently, even several times a day.

CI tools automate the process of build and test.

`tox` - command-line tool that allows you to run complete suite of tests in multiple envs. Great starting point when
learning about CI. `tox`:

1. creates a virtual env in a .tox directory
2. pip installs some dependencies
3. builds your package
4. pip installs your package
5. runs your tests

`tox` can automate testing process locally, but also it helps with cloud-based CI. You can integrate tox with GitHub
Actions.

## Chapter 12: Testing Scripts and Applications

Definitions:

- script - a single file containing Python code that is intended to be run directly from Python
- importable script - a script in which no code is executed when it is imported. Code is executed only when it is run
  directly
- application - package or script that has external dependencies

Testing a small script with `subprcoess.run` works okay, but it does have drawbacks

- we may want to test sections of larger scripts separately
- we may want to separate test code and scripts into different directories

Solution for this is to make a script importable. Add `if __name__ == "__main__"` - this code is executed only when we
call the script with `python script.py`.

## Chapter 13: Debugging Test Failures

pytest includes few command-line flags that are useful for debugging:

- `-lf` / `--last-failed` - runs just the tests that failed last
- `-ff` / `--failed-first` - runs all the test, starting from the last failed
- `-x` / `--exitfirst` - stops the test session after the first failure
- `--maxfail=num` -stops the tests after `num` failures
- `-nf` / `--new-first` - runs all the tests, ordered by the modification time
- `--sw` / `--stepwise` - stops the tests at the first failure, starts the test at the last failure next time
- `--sw-skip` / `--stepwise-skip` - same as `--sw`, but skips the first failure

Flags to control pytest output:

- `-v` / `--verbose` - all the test names, passing or failing
- `--tb=[auto/long/short/line/native/no]` - controls the traceback style
- `-l` / `--showlocals` - displays local variables alongside the stacktrace

Flags to start a command-line debugger:

- `--pdb` - starts an interactive debugging session at the point of failure
- `--trace` - starts the pdb source-code debugger immediately when running each test
- `--pdbcls` - uses alternatives to pdb

`pdb` - Python Debugger - part of the Python standard library. Add `breakpoint()` call, when a pytest hits this function
call, it will stop there and launch `pdb`. There are common commands recognized by `pdb` - full list in the
documentation (or use PyCharm's debugger instead if you can).

## Chapter 14: Third-Party Plugins

The pytest code is designed to allow customisation and extensions, and there are hooks available to allow modifications
and improvements through plugins.

Every time you put fixtures and/or hook functions into a project's `conftest.py` file, you create a local plugin. Only
some extra work is needed to turn these files into installable plugins.

`pytest` plugins are installed with `pip`.

Plugins that change the normal test run flow:

- `pytest-order` - specify the order using marker
- `pytest-randomly` - randomize order, first by file, then by a class, then by test
- `pytest-repeat` - makes it easy to repeat a single/multiple test(s), specific number of times
- `pytest-rerunfailures` - rerun failed tests (helpful for flaky tests)
- `pytest-xdist` - runs tests in parallel, either using multiple CPUs or multiple remote machines

Plugins that alter or enhance output:

- `pytest-instafail` - reports tracebacks and output from failed tests right after the failure
- `pytest-sugar` - shows green checkmarks instead of dots and has nice progress bar
- `pytest-html` - allows for HTML report generation

Plugins for web development:

- `pytest-selenium` - additional fixtures to allow easy configuration of browser-based tests
- `pytest-splinter` - built on top of Selenium, allows Splinter to be used more easily from pytest
- `pytest-django`, `pytest-flask` - make testing Django/Flask apps easier

Plugins for fake data:

- `Faker` - generates fake data, provides `faker` fixture
- `model-bakery` - generates Django models with fake data
- `pytest-factoryboy` - includes fixtures for Factory Boy
- `pytest-mimesis` - generates fake data similarly to Faker, but Mimesis is quite a bit faster

Plugins that extend pytest functionality:

- `pytest-cov` - runs coverage while testing
- `pytest-benchmark` - runs benchmark timing on code within tests
- `pytest-timeout` - doesn't let tests run too long
- `pytest-asyncio` - test async functions
- `pytest-bdd` - BDD-style tests with pytest
- `pytest-freezegun` - freezes time so that any code that reads the time will get the same value during a tests, you can
  also set a particular date or time
- `pytest-mock` - thin wrapper around the `unittest.mock`

Full list of plugins: https://docs.pytest.org/en/latest/reference/plugin_list.html

## Chapter 15: Building Plugins

Hook functions - function entry points that pytest provides to allow plugin developers to intercept pytest behaviour at
certain points and make changes. There are multiple hook functions, example:

- `pytest_configure()` - perform initial config. We can use this function to for example, pre-declare `slow` marker.
- `pytest_addoption()` - register options and settings, e.g. new flag: _--slow_
- `pytest_collection_modifyitems()` - called after test collection, can be used to filter or re-order the test items,
  e.g. to find _slow_ tests

The Node Interface: https://docs.pytest.org/en/latest/reference/reference.html#node

You can transform local `conftest.py` to installable plugin. You can use `Flit` to get help with the `pyproject.toml`
and `LICENSE`.

Plugins are code that needs to be tested just like any other code. `pytester` ias a plugin shipped with `pytest`.
`pytester` creates a temporary directory for each test that uses the `pytester` fixture, there are a bunch of
functions to help populate this directory - https://docs.pytest.org/en/latest/reference/reference.html#pytester

## Chapter 16: Advanced Parametrization

When using complex parametrization values, `pytest` numbers test cases like: `starting_card0, starting_card1, ...`. It
is possible to generate custom identifiers:

```py
card_list = [
    Card("foo", "todo"),
    Card("foo", "in prog"),
    Card("foo", "done"),
]


@pytest.mark.parametrize("starting_card", card_list, ids=str)
```

You can write custom ID function:

```py
def cards_state(card):
    return card.state


@pytest.mark.parametrize("starting_card", card_list, ids=cards_state)
```

Lambda function works as well:

```py
@pytest.mark.parametrize("starting_card", card_list, ids=lambda c: c.state)
```

If you have one wor two parameters requiring special treatment, use `pytest.param` to override the ID:

```py
card_list = [
    Card("foo", "todo"),
    pytest.param(Card("foo", "in prog"), id="special"),
    Card("foo", "done"),
]


@pytest.mark.parametrize("starting_card", card_list, ids=cards_state)
```

You can supply a list to `ids`, instead of a function:

```py
id_list = ["todo", "in prog", "done"]


@pytest.mark.parametrize("starting_card", card_list, ids=id_list)
```

but you have to be extra careful to keep the lists synchronized. Otherwise, the IDs are wrong.

It is possible to write our own function to generate parameter values:

```py
def text_variants():
    # This function can read data from a file/API/database/... as well.
    variants = {...: ...}

    for key, value in variants.items():
        yield pytest.param(value, id=key)


@pytest.mark.parametrize("variant", text_variants())
```

If you want to test all combinations, stacking parameters is the way to go:

```py
@pytest.mark.parametrize("state", states)
@pytest.mark.parametrize("owner", owners)
@pytest.mark.parametrize("summary", summaries)
def test_stacking(summary, owner, state):
```

this will act rather like cascading for loops, looping on the parameters from the bottom decorator to the top.

An _indirect parameter_ is the one that get passed to a fixture before it gets send to the test function. Indirect
parameters essentially let us parameterize a fixture, while keeping the parameter values with the test function. This
allows different tests to use the same fixture with different parameter values.

```py
@pytest.fixture()
def user(request):
    role = request.param
    print(f"Logging in as {role}")
    yield role
    print(f"Logging out {role}")


@pytest.mark.parametrize("user", ["admin", "team_member", "visitor"], indirect=["user"])
def test_access_rights(user):
    ...
```
