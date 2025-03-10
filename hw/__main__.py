if __debug__:
    breakpoint()

from .startup import *
from .driver import Driver

if __name__ == '__main__':
    # print(PROGRAM)
    log.info(f'Executing {PROGRAM} ...')
    
    Driver().run()
    
    # log.info(f'Execution complete.')
