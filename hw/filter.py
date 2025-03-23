from pathlib import Path
import sys

sys.path.insert(0, str(Path.home() / 'Documents/GitHub/files-1.0.0/files'))
from files import *

if __name__ == '__main__':
    from startup import *
    from program import Program
else:
    from .startup import *  # Imports the pre-processed command-line arguments
    from .program import Program

class Filter(Program):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def process_files(self):
        for file in ARGS.args:
            self.process(file)

    def process(self, s):
        f = File(s)
        log.info(f'Processing {type(f)} {f.name}...')
        match f:
            case NonExistFile():
                print(f'File {f.name} does not exist.')
            case Directory():
                for f2 in f.ls(recursive=ARGS.recursive, all=ARGS.all):
                    self.process(f2)
            case PythonFile():
                print(f'File {f.name} is a {type(f)}.')
            case _:
                print(f'File {f.name} is a {type(f)}.')
                    

if __name__ == "__main__":
    filter_program = Filter()
    filter_program.process_files()
