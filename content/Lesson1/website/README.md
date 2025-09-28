# Quarto Login Demo

This is a Quarto website protected by a password using Flask.

---

## ✅ Steps to Run in Codespaces

1. Open the repo in GitHub Codespaces or VSCode Dev Container.

2. Wait for the dev container to finish building (this sets up Python, R, Quarto, and your Conda environment).

3. Open a terminal — you should see `(quarto-env)` activated automatically.

4. Run:

```bash
quarto render
python scripts/flask_server.py
Open port 5000 and log in using the password in .env (default: teachme123).
