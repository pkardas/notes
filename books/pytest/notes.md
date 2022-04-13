[go back](https://github.com/pkardas/learning)

# Python Testing with Pytest: Simple, Rapid, Effective, and Scalable

Book by Brian Okken

- [Chapter 1: Getting Started with pytest](#chapter-1-getting-started-with-pytest)
- [Chapter 2: Writing Test Functions](#chapter-2-writing-test-functions)
- [Chapter 3: pytest Fixtures](#chapter-3-pytest-fixtures)

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
