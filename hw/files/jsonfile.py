import json

if __package__:
    from .textfile import TextFile
else:
    from textfile import TextFile
    
class JSONFile(TextFile):
    def parse(self):
        if self.path.suffix == ".json":
            return json.loads(self.read())
        raise NotImplementedError("Parsing not supported for this file type.")

if __name__ == '__main__':
    print(f"Executing {__name__}")