from pathlib import Path

from files.files import File

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
        log.info(f'Processing file {f.name}...')

if __name__ == "__main__":
    filter_program = Filter()
    filter_program.process_files()
