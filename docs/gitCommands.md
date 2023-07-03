### Git Branch

1. ```bash
   # List all branches in the current repo
   git branch
   # or
   git branch --list
   ```
2. ```bash
   # List all remote branches
   git branch -a
   ```
3. ```bash
   # Create a new branch
   git branch <branch-name>
   ```
4. ```bash
   # Create a new branch and checkout this branch
   git branch -b <branch-name>
   ```
5. ```bash
   # Rename the current branch to <branch-name>
   git branch -m <branch-name>
   ```
6. ```bash
   # Delete merged branches only (safe deletion)
   # Prevent deleting unmerged branches
   git branch -d <branch-name>
   # or
   git branch --delete <branch-name>
   ```
6. ```bash
   # Forcibly delete a branch
   git branch -D <branch-name>
   ```
