from tests.ch_12 import hello


def test_hello(capsys):
    hello.main()
    output = capsys.readouterr().out
    assert output == "Hello world\n"
