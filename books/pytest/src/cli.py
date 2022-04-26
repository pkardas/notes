"""Command Line Interface (CLI) for cards project."""
import os
import pathlib
from contextlib import contextmanager
from io import StringIO
from typing import List

import rich
import typer
from rich.table import Table

import src.api as cards

app = typer.Typer(name="cards", add_completion=False)


@app.command()
def version():
    """Return version of cards application"""
    print(cards.__version__)


@app.command()
def add(
        summary: List[str], owner: str = typer.Option(None, "-o", "--owner")
):
    """Add a card to db."""
    summary = " ".join(summary) if summary else None
    with cards_db() as db:
        db.add_card(cards.Card(summary, owner, state="todo"))


@app.command()
def delete(card_id: int):
    """Remove card in db with given id."""
    with cards_db() as db:
        try:
            db.delete_card(card_id)
        except cards.InvalidCardId:
            print(f"Error: Invalid card id {card_id}")


@app.command("list")
def list_cards(
        owner: str = typer.Option(None, "-o", "--owner"),
        state: str = typer.Option(None, "-s", "--state"),
):
    """
    List cards in db.
    """
    with cards_db() as db:
        the_cards = db.list_cards(owner=owner, state=state)
        table = Table(box=rich.box.SIMPLE)
        table.add_column("ID")
        table.add_column("state")
        table.add_column("owner")
        table.add_column("summary")
        for t in the_cards:
            owner = "" if t.owner is None else t.owner
            table.add_row(str(t.id), t.state, owner, t.summary)
        out = StringIO()
        rich.print(table, file=out)
        print(out.getvalue())


@app.command()
def update(
        card_id: int,
        owner: str = typer.Option(None, "-o", "--owner"),
        summary: List[str] = typer.Option(None, "-s", "--summary"),
):
    """Modify a card in db with given id with new info."""
    summary = " ".join(summary) if summary else None
    with cards_db() as db:
        try:
            db.update_card(
                card_id, cards.Card(summary, owner, state=None)
            )
        except cards.InvalidCardId:
            print(f"Error: Invalid card id {card_id}")


@app.command()
def start(card_id: int):
    """Set a card state to 'in prog'."""
    with cards_db() as db:
        try:
            db.start(card_id)
        except cards.InvalidCardId:
            print(f"Error: Invalid card id {card_id}")


@app.command()
def finish(card_id: int):
    """Set a card state to 'done'."""
    with cards_db() as db:
        try:
            db.finish(card_id)
        except cards.InvalidCardId:
            print(f"Error: Invalid card id {card_id}")


@app.command()
def config():
    """List the path to the Cards db."""
    with cards_dbz() as db:
        print(db.path())


@app.command()
def count():
    """Return number of cards in db."""
    with cards_db() as db:
        print(db.count())


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """
    Cards is a small command line task tracking application.
    """
    if ctx.invoked_subcommand is None:
        list_cards(owner=None, state=None)


def get_path():
    db_path_env = os.getenv("CARDS_DB_DIR", "")
    if db_path_env:
        db_path = pathlib.Path(db_path_env)
    else:
        db_path = pathlib.Path.home() / "cards_db"
    return db_path


@contextmanager
def cards_db():
    db_path = get_path()
    db = cards.CardsDB(db_path)
    yield db
    db.close()
