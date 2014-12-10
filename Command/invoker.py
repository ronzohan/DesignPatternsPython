from receiver import LsReceiver, TouchReceiver, RmReceiver
from command import LsCommand, TouchCommand, RmCommand


class Invoker(object):
    def __init__(self, create_file_commands, delete_file_commands):
        self.create_file_commands = create_file_commands
        self.delete_file_commands = delete_file_commands
        self.history = []

    def create_file(self):
        print 'Creating file...'

        for command in self.create_file_commands:
            command.execute()
            self.history.append(command)

        print 'File created.\n'

    def delete_file(self):
        print 'Deleting file...'

        for command in self.delete_file_commands:
            command.execute()
            self.history.append(command)
        print 'File deleted.\n'

    def undo_all(self):
        print 'Undo all...'

        for command in reversed(self.history):
            command.undo()

        print 'Undo all finished.'

if __name__ == "__main__":
    # Client

    # List files in the Directory
    ls_receiver = LsReceiver()
    ls_command = LsCommand(ls_receiver)

    # Create file
    touch_receiver = TouchReceiver('test_file')
    touch_command = TouchCommand(touch_receiver)

    # Delete created file
    rm_receiver = RmReceiver('test_file')
    rm_command = RmCommand(rm_receiver)

    create_file_commands = [ls_command, touch_command, ls_command]
    delete_file_commands = [ls_command, rm_command, ls_command]

    invoker = Invoker(create_file_commands, delete_file_commands)

    invoker.create_file()
    invoker.delete_file()
    invoker.undo_all()