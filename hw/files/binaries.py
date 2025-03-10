from files import File

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
