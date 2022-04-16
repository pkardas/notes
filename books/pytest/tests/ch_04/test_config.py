import src as cards
from typer.testing import CliRunner


def run_cards(*params):
    runner = CliRunner()
    result = runner.invoke(cards.app, params)
    return result.output.rstrip()


def test_run_cards():
    assert run_cards("version") == cards.__version__


def test_patch_get_path(monkeypatch, tmp_path):
    def fake_get_path():
        return tmp_path

    monkeypatch.setattr(cards.cli, "get_path", fake_get_path)
    assert run_cards("config") == str(tmp_path)


def test_patch_home(monkeypatch, tmp_path):
    full_cards_dir = tmp_path / "cards_db"

    def fake_home():
        return tmp_path

    monkeypatch.setattr(cards.cli.pathlib.Path, "home", fake_home)
    assert run_cards("config") == str(full_cards_dir)


def test_patch_env_var(monkeypatch, tmp_path):
    monkeypatch.setenv("CARDS_DB_DIR", str(tmp_path))
    assert run_cards("config") == str(tmp_path)
