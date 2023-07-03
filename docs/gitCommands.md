#### Create

1. ```bash
   # Create a new branch
   git branch <branch-name>
   ```
2. ```bash
   # Create a new branch and checkout this branch
   git branch -b <branch-name>
   ```
3. ```bash
   # Create a remote branch automatically if pushing a new local branch to remote repo
   git push <repo-name> <branch-name>
   ```

#### Retrieve

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

#### Update
   
1. ```bash
   # Rename the current branch to <branch-name>
   git branch -m <branch-name>
   ```

#### Delete

1. ```bash
   # Delete merged branches only (safe deletion)
   # Prevent deleting unmerged branches
   git branch -d <branch-name>
   # or
   git branch --delete <branch-name>
   ```
2. ```bash
   # Forcibly delete a branch
   git branch -D <branch-name>
   ```
3. ```bash
   # Delete a branch from a remote repo
   git push <repo-name> --delete <branch-name>
   # or
   git push <repo-name> !<branch-name>
   ```
