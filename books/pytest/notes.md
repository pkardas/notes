[go back](https://github.com/pkardas/learning)

# Python Testing with Pytest: Simple, Rapid, Effective, and Scalable

Book by Brian Okken

- [Chapter 1: Getting Started with pytest](#chapter-1-getting-started-with-pytest)
- [Chapter 2: Writing Test Functions](#chapter-2-writing-test-functions)

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
