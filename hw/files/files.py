from pathlib import Path

class File:
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
    def __new__(cls, path):
        path = Path(path)  # Ensure it's a Path object
        
        if not path.exists():
            if __package__:
                from .non_exist_file import NonExistFile
            else:
                from non_exist_file import NonExistFile
            return super().__new__(NonExistFile)
        
        if path.is_dir():
            if __package__:
                from .directory import Directory
            else:
                from directory import Directory
            return super().__new__(Directory)
        
        suffix = path.suffix.lower().lstrip('.')
        
        # Define specialized subclasses based on suffix
        if suffix in {"txt", "md"}:
            if __package__:
                from .textfile import TextFile
            else:
                from textfile import TextFile
            return super().__new__(TextFile)
        elif suffix in {".json", ".yaml", ".yml"}:
            if __package__:
                from .jsonfile import JSONFile
            else:
                from jsonfile import JSONFile
            return super().__new__(JSONFile)
        
        return super().__new__(cls)  # Default to File class
    
    def __init__(self, path):
        self.path = Path(path)

    def read(self):
        return self.path.read_text()

    def write(self, content):
        self.path.write_text(content)

    def check_type(self):
        from directory import Directory
        from jsonfile import JSONFile
        from non_exist_file import NonExistFile
        from textfile import TextFile
        return type(self)

    @property
    def name(self):
        return self.path.name

    @name.setter
    def name(self, s):
        p = Path(s)
        

if __name__ == '__main__':
    print(File('hw').check_type())
    # import doctest
    # doctest.testmod()