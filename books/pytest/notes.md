[go back](https://github.com/pkardas/learning)

# Python Testing with Pytest: Simple, Rapid, Effective, and Scalable

Book by Brian Okken

- [Chapter 1: Getting Started with pytest](#chapter-1-getting-started-with-pytest)
- [Chapter 2: Writing Test Functions](#chapter-2-writing-test-functions)
- [Chapter 3: pytest Fixtures](#chapter-3-pytest-fixtures)
- [Chapter 4: Built-in fixtures](#chapter-4-built-in-fixtures)
- [Chapter 5: Parametrization](#chapter-5-parametrization)
- [Chapter 6: Markers](#chapter-6-markers)
- [Chapter 7: Strategy](#chapter-7-strategy)

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

The scope dictates how often the setup and teardown get run whet it is used by multiple test functions:

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
