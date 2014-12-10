import abc
import os


history = []


class Command(object):
    """The command interface"""

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def execute(self):
        """Method to execute the command"""
        pass

    @abc.abstractmethod
    def undo(self):
        """A method to undo the command"""


class LsCommand(Command):
    """Concrete command that emulates ls unix command behavior"""

    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        """The command delegates the call to its receiver."""
        self.receiver.show_current_dir()

    def undo(self):
        """Can not undo ls command."""


class TouchCommand(Command):
    """Concrete command that emulates touch unix command behavior"""

    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.create_file()

    def undo(self):
        self.receiver.delete_file()


class RmCommand(Command):
    """Concrete command that emulates rm unix command behavior"""
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.delete_file()

    def undo(self):
        self.receiver.undo()