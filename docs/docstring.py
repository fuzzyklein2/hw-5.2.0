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

    Example:
    >>> file = File('nonexistent.txt')
    >>> isinstance(file.check_file(), NonExistFile)
    True

    >>> file = File('sample.txt')
    >>> isinstance(file.check_file(), TextFile)
    True

    >>> file = File('sample.json')
    >>> isinstance(file.check_file(), JSONFile)
    True

    >>> file = File('some_directory')
    >>> isinstance(file.check_file(), Directory)
    True
    """

    def __init__(self, path: str):
        self.path = path

    def check_file(self):
        import os
        import json
        
        # Check if path is a directory
        if os.path.isdir(self.path):
            return Directory(self.path)
        
        # Check if file exists
        if not os.path.exists(self.path):
            return NonExistFile(self.path)
        
        # Check if file is a JSON file
        if self.path.endswith('.json'):
            return JSONFile(self.path)
        
        # Check if file is a text file
        if self.path.endswith('.txt'):
            return TextFile(self.path)


class NonExistFile:
    """
    A class representing a file that does not exist.
    """
    def __init__(self, path: str):
        self.path = path


class TextFile:
    """
    A class representing a regular text file.
    """
    def __init__(self, path: str):
        self.path = path


class JSONFile:
    """
    A class representing a JSON file.
    """
    def __init__(self, path: str):
        self.path = path


class Directory:
    """
    A class representing a directory.
    """
    def __init__(self, path: str):
        self.path = path
