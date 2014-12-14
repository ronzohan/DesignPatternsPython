import os


class LsReceiver(object):
    def show_current_dir(self):
        """The receiver knows how to execute the command."""

        cur_dir = './'

        filenames = []

        for filename in os.listdir(cur_dir):
            if os.path.isfile(os.path.join(cur_dir, filename)):
                filenames.append(filename)

        print 'Content of dir: ', ' '.join(filenames)


class TouchReceiver(object):
    def __init__(self, filename):
        self.filename = filename

    def create_file(self):
        """Actual implementation of unix touch command."""
        with file(self.filename, 'a'):
            os.utime(self.filename, None)

    def delete_file(self):
        """Undo unix touch command. Here we simply delete the file."""
        os.remove(self.filename)


class RmReceiver(object):
    def __init__(self, filename):
        self.filename = filename
        self.backup_name = None

    def delete_file(self):
        """Deletes file with creating backup to restore it in undo method. """
        self.backup_name = '.' + self.filename
        os.rename(self.filename, self.backup_name)

    def undo(self):
        """Restores the deleted file."""
        original_name = self.backup_name[1:]
        os.rename(self.backup_name, original_name)
        self.backup_name = None
