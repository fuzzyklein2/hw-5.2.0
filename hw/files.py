from pathlib import Path

class File(Path):
    """
    A class representing a file or directory.
    
    This class can be used to check for the existence of files, read text files, 
    read and write JSON files, and manage directories.
    
    Attributes:
        path (str): The file or directory path.
    
    Methods:
        __init__(path):
            Initializes the File object with the given path.
    
        check_file():
            Returns an appropriate subclass based on the file's type or existence:
            - NonExistFile: If the file does not exist.
            - TextFile: If the file is a regular text file.
            - JSONFile: If the file is a JSON file.
            - Directory: If the path is a directory.
    
    """
    FILE_TYPES = { 'txt' : 'TextFile',
                   'json' : 'JSONFile',
                   'py' : 'PythonFile',
                   'md' : 'MarkdownFile',
                 }
    
    def __new__(cls, path, *args, **kwargs):
        path = Path(path)
        super().__new__(cls, path, *args, **kwargs)
        if not path.exists():
            return super().__new__(NonExistFile, *args, **kwargs)        
        if path.is_dir():
            return super().__new__(Directory, *args, **kwargs)
        
        suffix = path.suffix.lstrip('.')
        
        # Define specialized subclasses based on suffix
        file_cls_name = cls.FILE_TYPES.get(suffix, None)
        
        if file_cls_name and file_cls_name in globals():
            return super().__new__(globals()[file_cls_name])

        return path
    
    def __init__(self, path):
        super().__init__(path)

    def read(self):
        return self.path.read_text()

    def write(self, content):
        self.path.write_text(content)

    def rename(self, target):
        """Rename the file and return a new instance of the correct subclass."""
        target = super().rename(target)  # This moves the file and returns a new Path object
        return File(target)  # Ensure the correct subclass is returned


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

class Directory(File):
    def __init__(self, path, *args, **kwargs):
        super().__init__(path)
    def ls(self):
        """List directory contents."""
        return [item.name for item in self.iterdir()]

class TextFile(File):
    def __init__(self, path, *args, **kwargs):
        super().__init__(path)
    def to_upper(self):
        return self.read().upper()

class MarkdownFile(TextFile):
    def __init__(self, path, *args, **kwargs):
        super().__init__(path)
    

class SourceFile(TextFile):
    pass

class PythonFile(SourceFile):
    pass

class DataFile(TextFile):
    pass

class JSONFile(DataFile):
    def parse(self):
        if self.path.suffix == ".json":
            return json.loads(self.read())
        raise NotImplementedError("Parsing not supported for this file type.")

class BinaryFile(File):
    """Handles binary files by overriding read/write with read_bytes/write_bytes."""
    
    def read(self):
        return self.path.read_bytes()

    def write(self, content):
        """Writes binary content to the file.
        
        Args:
            content (bytes): The binary content to write.
        """
        self.path.write_bytes(content)


if __name__ == '__main__':
    print(File('hw/driver.py').check_type())
    # import doctest
    # doctest.testmod()