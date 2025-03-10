if __package__:
    from .files import File
else:
    from files import File

class NonExistFile(File):
    def __init__(self, path):
        super().__init__(path)
    
    def create(self, dirs=False):
        """Creates an empty file at the given path. 
        
        Args:
            dirs (bool): If True, create missing parent directories.
        """
        if dirs:
            self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.touch()
        return File(self.path)  # Reinstantiate as the correct subclass

