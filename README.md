# Git & GitHub Assessment Documentation
**Name:** Niranjan  
**Date:** May 5, 2025  
**Tool:** Git Bash (Windows)  
**Repository:** https://github.com/N8880/devops_herovired

---

## Question 1: Project Initialization & First Push

### Objective
Set up a new Git project and push it to a remote repository.

### Steps Performed

**1. Created project folder and navigated into it**
```bash
mkdir devops_hervierd
cd devops_hervierd
```

**2. Initialized Git repository**
```bash
git init
```

**3. Created `niranjan_app.py` using Vim**
```bash
vim niranjan_app.py
```
Added the following Python code:
```python
def greet(name):
    return f'Hello, {name}!'

print(greet('World'))
```
Saved and exited Vim using `:wq`

**4. Checked Git status**
```bash
git status
```
Output showed `niranjan_app.py` as an untracked file.

**5. Staged the file**
```bash
git add niranjan_app.py
```
> ⚠️ Note: Got warning `LF will be replaced by CRLF` — this is normal on Windows and can be ignored.

**6. Committed with a meaningful message**
```bash
git commit -m "Initial commit: add niranjan_app.py"
```

**7. Created remote repository on GitHub**
- Went to github.com → New Repository
- Named it `devops_herovired`
- Set to Public
- Did NOT initialize with README (to avoid conflicts)

**8. Added remote origin**
```bash
git remote add origin https://github.com/N8880/devops_herovired.git
```

**9. Verified remote configuration**
```bash
git remote -v
```

**10. Pushed code to remote**
```bash
git branch -M main
git push -u origin main
```
Output confirmed:
```
* [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```

---

## Question 2: Working with Changes & History

### Objective
Track code changes and manage commit history properly.

### Steps Performed

**1. Modified `niranjan_app.py` with new functionality**

Opened file in Vim and added a calculator feature:
```python
# Feature 2: Calculator functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

# Simple interactive menu
print("=== Calculator ===")
print(f"Add:      {add(10, 5)}")
print(f"Subtract: {subtract(10, 5)}")
print(f"Multiply: {multiply(10, 5)}")
print(f"Divide:   {divide(10, 5)}")
```

**2. Checked changes before staging**
```bash
git status
```

**3. Viewed differences in the file**
```bash
git diff niranjan_app.py
```
Showed all new lines added in green with `+` prefix.

**4. Staged specific changes interactively**
```bash
git add -p niranjan_app.py
```
Git showed the hunk and prompted `[y,n,q,a,d,e,p,P,?]` — typed `y` to stage.

**5. Committed with a clear message**
```bash
git commit -m "feat: add calculator functions (add, subtract, multiply, divide)"
```

**6. Made another change — added temperature converter**
```python
# Feature 3: Temperature converter
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

print("\n=== Temperature Converter ===")
print(f"25°C = {celsius_to_fahrenheit(25)}°F")
print(f"98.6°F = {fahrenheit_to_celsius(98.6)}°C")
```

**7. Staged all changes**
```bash
git add .
```

**8. Committed again**
```bash
git commit -m "feat: add temperature converter functions"
```

**9. Viewed full commit history**
```bash
git log
```

**10. Viewed compact one-line history**
```bash
git log --oneline
```

---

## Question 3: Branching & Feature Development

### Objective
Work with branches and manage feature development separately.

### Steps Performed

**1. Created a new branch**
```bash
git branch feature-update
```

**2. Switched to the new branch**
```bash
git switch feature-update
```

**3. Verified current branch**
```bash
git branch
```
Output:
```
* feature-update
  main
```

**4. Added new feature — Simple Interest Calculator**
```python
# Feature 4: Simple interest calculator
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

print("\n=== Simple Interest ===")
print(f"SI: {simple_interest(1000, 5, 3)}")
```

**5. Staged and committed the changes**
```bash
git add niranjan_app.py
git commit -m "feat: add simple interest calculator on feature-update branch"
```

**6. Switched back to main**
```bash
git checkout main
```

**7. Merged the feature branch into main**
```bash
git merge feature-update
```

**8. Verified changes are merged**
```bash
git log --oneline
```

**9. Deleted the branch safely**
```bash
git branch -d feature-update
```

**10. Force deleted a dummy branch**
```bash
git branch dummy-branch
git branch -D dummy-branch
```
> `-d` = safe delete (only if merged), `-D` = force delete (even if unmerged)

---

## Question 4: Handling Errors (Stash, Reset, Revert)

### Objective
Manage mistakes and unfinished work without losing progress.

### Steps Performed

**1. Made changes to `niranjan_app.py` without committing**

Added BMI Calculator feature in Vim:
```python
# work in progress
# Feature 5: BMI Calculator
def bmi_calculator(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

print("\n=== BMI Calculator ===")
print(f"BMI: {bmi_calculator(70, 1.75)}")
```

**2. Stashed the changes (including untracked files)**
```bash
git stash push -u -m "wip: adding BMI calculator"
```
> `-u` includes untracked files, `-m` adds a descriptive label

**3. Checked the stash list**
```bash
git stash list
```
Output:
```
stash@{0}: On feature-update: wip: adding BMI calculator
```

**4. Applied the stashed changes back**
```bash
git stash pop
```
> `pop` applies and removes the stash. Use `git stash apply` to keep it in the list.

**5. Committed the changes**
```bash
git add niranjan_app.py
git commit -m "feat: add BMI calculator"
```

**6. Made another commit with incorrect code (simulated bug)**
```bash
git commit -m "bug: accidentally added broken function"
```

**7. Undid the last commit using reset**
```bash
git reset --soft HEAD~1
```
> `--soft` keeps changes staged. `--mixed` unstages. `--hard` discards completely.

**8. Made another commit**
```bash
git add niranjan_app.py
git commit -m "fix: re-commit after reset"
```

**9. Undid a commit using revert**
```bash
git revert HEAD
```
> Creates a new commit that reverses the last one. Safe for shared branches unlike `reset`.

**10. Verified commit history**
```bash
git log --oneline
```

---

## Bonus: File Rename on GitHub

During the assessment, the file was renamed from `nitanjan_app.py` to `niranjan_app.py`.

```bash
# File was manually renamed using mv
mv nitanjan_app.py niranjan_app.py

# Stage the new file
git add niranjan_app.py

# Remove old filename from Git tracking
git rm nitanjan_app.py

# Commit the rename
git commit -m "refactor: rename nitanjan_app.py to niranjan_app.py"

# Push to GitHub
git push origin main
```

---

## Key Git Commands Summary

| Command | Purpose |
|---|---|
| `git init` | Initialize a new Git repository |
| `git status` | Check current state of working directory |
| `git add <file>` | Stage a specific file |
| `git add .` | Stage all changes |
| `git add -p` | Stage changes interactively (hunk by hunk) |
| `git commit -m ""` | Commit with a message |
| `git push origin main` | Push to remote repository |
| `git log --oneline` | View compact commit history |
| `git diff` | View unstaged changes |
| `git branch <name>` | Create a new branch |
| `git switch <name>` | Switch to a branch |
| `git merge <branch>` | Merge a branch into current |
| `git branch -d <name>` | Safely delete a branch |
| `git branch -D <name>` | Force delete a branch |
| `git stash push -u -m ""` | Stash changes with a label |
| `git stash list` | View all stashes |
| `git stash pop` | Apply and remove latest stash |
| `git reset --soft HEAD~1` | Undo last commit, keep changes staged |
| `git revert HEAD` | Create a new commit that undoes last commit |
| `git remote -v` | Verify remote configuration |
| `git rm <file>` | Remove file from Git tracking |

---

## Important Notes

- ⚠️ `LF will be replaced by CRLF` warning on Windows is **normal** — ignore it
- ✅ Always use `git revert` on shared/pushed branches instead of `git reset`
- ✅ Use `git stash` when you need to switch context without committing
- ✅ Meaningful commit messages follow the pattern: `type: short description`
  - `feat:` — new feature
  - `fix:` — bug fix
  - `refactor:` — code restructure
  - `chore:` — maintenance tasks
