import os
from os.path import join, dirname

from flask.cli import FlaskGroup

from app import create_app


cli = FlaskGroup(create_app=create_app)


# new

if __name__ == '__main__':
    cli()