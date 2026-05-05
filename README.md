# Git Project Setup Documentation

## 📌 Objective

This guide walks through setting up a new Git project, adding code, and pushing it to a remote repository (e.g., GitHub).

---

## 🛠️ Step 1: Create a New Project Folder

```bash
mkdir my-python-project
cd my-python-project
```
- <img width="437" height="259" alt="image" src="https://github.com/user-attachments/assets/ee605168-fc44-48eb-8bc7-aedebb55d637" />

---

## 🔧 Step 2: Initialize a Git Repository

```bash
git init
```

This creates a new `.git` directory to track your project.

---

## 📝 Step 3: Create a Python File

Create a file named `app.py`:

```bash
touch app.py
```

Add sample Python code:

```python
print("Hello, Git!")
```

---

## 🔍 Step 4: Check Git Status

```bash
git status
```

This shows untracked files and changes.

---

## ➕ Step 5: Stage the File

```bash
git add app.py
```

---

## 💾 Step 6: Commit Changes

```bash
git commit -m "Initial commit: added app.py with basic Python code"
```

---

## 🌐 Step 7: Create a Remote Repository

* Go to GitHub (or similar platform)
* Click **New Repository**
* Name it (e.g., `my-python-project`)
* Do NOT initialize with README (since you already have local files)

---

## 🔗 Step 8: Add Remote Origin

```bash
git remote add origin https://github.com/your-username/my-python-project.git
```

---

## ✅ Step 9: Verify Remote Configuration

```bash
git remote -v
```

You should see:

```
origin  https://github.com/your-username/my-python-project.git (fetch)
origin  https://github.com/your-username/my-python-project.git (push)
```

---

## 🚀 Step 10: Push Code to Remote Repository

```bash
git branch -M main
git push -u origin main
```

---

## 🎉 Result

Your code is now successfully pushed to the remote repository.

---

## 📚 Summary of Commands

```bash
mkdir my-python-project
cd my-python-project
git init
touch app.py
git status
git add app.py
git commit -m "Initial commit"
git remote add origin <repo-url>
git remote -v
git branch -M main
git push -u origin main
```

---

## 🧠 Tips

* Always check `git status` before committing
* Use meaningful commit messages
* Keep your repository organized

---

Happy Coding! 🚀
