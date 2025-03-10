## Jupyter Lab Hidden Files Issue

### Problem:
Jupyter Lab is refusing to show hidden files in the File Browser. The Settings Editor displays:

> Whether to show hidden files. The server parameter `ContentsManager.allow_hidden` must be set to `True` to display hidden files.

### Solution:
1. **Find or Create the Jupyter Config File**
   ```bash
   jupyter server --generate-config
   ```
   This will generate:
   ```
   ~/.jupyter/jupyter_server_config.py
   ```

2. **Edit the Config File**
   ```bash
   nano ~/.jupyter/jupyter_server_config.py
   ```
   Add or modify the following line:
   ```python
   c.ContentsManager.allow_hidden = True
   ```
   Save and exit (`Ctrl + X`, then `Y`, then `Enter`).

3. **Restart Jupyter Lab**
   ```bash
   jupyter lab
   ```
   Hidden files should now be visible.

---

## Best Way to Create an SSH Shortcut in Bash

### 1. Using an SSH Config File (Best Method)
1. Open (or create) `~/.ssh/config`:
   ```bash
   nano ~/.ssh/config
   ```
2. Add an entry:
   ```
   Host myserver
       HostName your.remote.server.com
       User yourusername
       Port 22  # Change if needed
       IdentityFile ~/.ssh/id_rsa  # Adjust if using a different key
   ```
3. Save and exit (`Ctrl + X`, then `Y`, then `Enter`).
4. Connect using:
   ```bash
   ssh myserver
   ```

### 2. Using a Bash Alias (Quick & Simple)
1. Open `~/.bashrc` (or `~/.bash_aliases`):
   ```bash
   nano ~/.bashrc
   ```
2. Add the alias:
   ```bash
   alias myserver="ssh user@your.remote.server.com"
   ```
3. Save and reload Bash:
   ```bash
   source ~/.bashrc
   ```
4. Connect using:
   ```bash
   myserver
   ```

### Which One to Use?
- Use the **SSH config file** for multiple servers and advanced settings.
- Use a **Bash alias** for a quick shortcut to a single server.
