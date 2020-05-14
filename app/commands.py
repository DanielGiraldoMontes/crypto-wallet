import click
from flask.cli import with_appcontext

from app import db
from .auth.models import Opt, User, Wallet, Transaction
from .wallet.models import Wallet


@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()
