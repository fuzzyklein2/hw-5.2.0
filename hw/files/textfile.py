if __package__:
    from .files import File
else:
    from files import File

class TextFile(File):
    def to_upper(self):
        return self.read().upper()

