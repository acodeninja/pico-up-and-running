import os
import shutil

from termcolor import cprint

from util.commands.base import CommandBase


class CommandBuild(CommandBase):
    description = 'minify and attempt to compile pico application to bytecodes'

    @staticmethod
    def execute(arguments=None):
        cprint('copying codebase to build', 'blue')
        shutil.rmtree('build')
        os.mkdir('build')
        shutil.copytree('app', 'build/app')
        shutil.copyfile('main.py', 'build/main.py')
        shutil.copyfile('settings.py', 'build/settings.py')
        cprint('minifying codebase', 'blue')
        os.system('pyminify build --in-place')
