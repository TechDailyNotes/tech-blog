#### Create

1. Create a new branch

```bash
git branch <branch-name>
```

2. Create a new branch and checkout this branch

```bash
git branch -b <branch-name>
```

3. Create a remote branch automatically if pushing a new local branch to remote repo

```bash
git push <repo-name> <branch-name>
```

#### Retrieve

1. List all branches in the current repo

```bash
git branch
# or
git branch --list
```

2. List all remote branches

```bash
git branch -a
```

#### Update

1. Rename the current branch to <branch-name>

```bash
git branch -m <branch-name>
```

#### Delete

1. Delete merged branches only (safe deletion) and prevent deleting unmerged branches

```bash
git branch -d <branch-name>
# or
git branch --delete <branch-name>
```

2. Forcibly delete a branch

```bash
git branch -D <branch-name>
```

3. Delete a branch from a remote repo

```bash
git push <repo-name> --delete <branch-name>
# or
git push <repo-name> -d <branch-name>
# or
git push <repo-name> !<branch-name>
```
