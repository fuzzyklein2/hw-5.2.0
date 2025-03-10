## Exiting a Command Loop Using the Cmd Class in Python

### 1. Using `EOF` (`Ctrl+D`)
Jupyter Lab is refusing to show hidden files in the File Browser. The Settings Editor displays:

```python
import cmd

class MyCmd(cmd.Cmd):
    prompt = "(mycmd) "
    
    def do_exit(self, arg):
        """Exit the command loop."""
        print("Exiting...")
        return True  # Returning True exits the loop

    def do_EOF(self, arg):
        """Handle EOF (Ctrl+D) to exit."""
        print("Goodbye!")
        return True  # Exits the loop

if __name__ == "__main__":
    MyCmd().cmdloop()
```

Typing `exit` or pressing `Ctrl+D` will stop the loop.

### 2. Returning `True` from a Command Method
Returning `True` from any `do_*` method causes the command loop to exit.

```python
def do_quit(self, arg):
    """Quit the command loop."""
    return True
```

### 3. Setting `self.stop = True` and Overriding `precmd`
```python
class MyCmd(cmd.Cmd):
    def __init__(self):
        super().__init__()
        self.stop = False

    def do_exit(self, arg):
        """Exit the shell."""
        print("Exiting...")
        self.stop = True
        return True  # Explicitly exit

    def precmd(self, line):
        if self.stop:
            return 'exit'
        return line
```

### 4. Using `sys.exit()` (Not Recommended)
```python
import sys

def do_exit(self, arg):
    """Exit the application."""
    print("Exiting...")
    sys.exit(0)
```

### Best Practice
The cleanest and most recommended way is to return `True` from `do_*` methods like `do_exit`, `do_EOF`, or `do_quit`.
