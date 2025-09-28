# Quarto Login-Protected Demo

This is a Quarto website protected by a password using Flask.

---

## ✅ Steps to Test in Codespaces

1. **Open Codespaces in GitHub**
2. Wait for dev container to build
3. Open terminal and run:

```bash
chmod +x .devcontainer/check_versions.sh
quarto render
python scripts/flask_server.py

3. Open port 5000. Login using password from .env.
4. Default password, nginx: teachme123
