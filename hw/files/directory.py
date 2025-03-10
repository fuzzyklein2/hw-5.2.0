if __package__:
    from .files import File
else:
    from files import File

class Directory(File):
    def ls(self):
        """List directory contents."""
        return [item.name for item in self.path.iterdir()]

