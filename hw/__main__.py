if __debug__:
    breakpoint()

from .startup import *
from .filter import Filter

if __name__ == '__main__':
    # print(PROGRAM)
    log.info(f'Executing {PROGRAM} ...')
    
    p = Filter()
    
    # log.info(f'Execution complete.')
