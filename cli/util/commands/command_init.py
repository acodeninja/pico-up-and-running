import os
from termcolor import cprint
from .base import CommandBase


class CommandInit(CommandBase):
    description = 'initialise a python pico project in the current directory'

    @staticmethod
    def execute(arguments=None):
        cprint('creating settings file', 'blue')
        try:
            f = open("settings.py", "x")
            f.write("screen = 'unicorn'\n")
            f.close()
        except FileExistsError:
            cprint('settings file already exists', 'red')

        cprint('creating main entrypoint', 'blue')
        try:
            f = open("main.py", "x")
            f.write("print('Hello!')\n")
            f.close()
        except FileExistsError:
            cprint('main.py file already exists', 'red')

        cprint('creating application module', 'blue')
        try:
            os.mkdir('app')
        except FileExistsError:
            cprint('app directory already exists', 'red')

        try:
            f = open("app/__init__.py", "x")
            f.write("\n")
            f.close()
        except FileExistsError:
            cprint('app module file already exists', 'red')
