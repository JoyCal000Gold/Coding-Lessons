# Quarto Login Demo

This is a Quarto website protected by a password using Flask.

---

The terminal will open inside the container with the conda environment activated.

Navigate to your Flask script folder (e.g., /workspaces/Coding-Lessons/content/Lesson1/website/scripts).

Run your Flask app inside the container:

python flask_server.py


Open your host browser to:

http://localhost:5000/


and you will reach your Flask app running inside the container.

If you want auto-reload during development, you can set app.run(debug=True) in your Flask script or run Flask via flask run with environment variables set.

If your Flask app uses environment variables (like .env), make sure those files are mounted into the container (usually happens automatically with devcontainers).
