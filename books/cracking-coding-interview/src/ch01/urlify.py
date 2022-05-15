import pytest


def urlify_pythonic(url: str) -> str:
    return ' '.join(url.split()).replace(' ', "%20")


def urlify_array(url: str) -> str:
    result_url = ""
    last_appended_character = None

    for ch in url:
        if ch == ' ' and last_appended_character is None:
            # Do not duplicate '%20' in the URL
            continue
        elif ch == ' ' and last_appended_character:
            last_appended_character = None
            result_url += "%20"
        else:
            last_appended_character = ch
            result_url += ch

    if last_appended_character is None:
        return result_url[:-3]

    return result_url


@pytest.mark.parametrize("url, expected_url", [
    # @formatter:off
    ("Mr John Smith",     "Mr%20John%20Smith"),
    ("Mr John  Smith",    "Mr%20John%20Smith"),
    ("    Mr John Smith", "Mr%20John%20Smith"),
    ("Mr John Smith    ", "Mr%20John%20Smith"),
    ("Mr ",               "Mr"),
    ("M ",                "M"),
    ("  ",                ""),
    ("",                  ""),
    # @formatter:on
])
@pytest.mark.parametrize("function", [
    urlify_pythonic,
    urlify_array,
])
def test_algorithm(function, url, expected_url):
    assert function(url) == expected_url
