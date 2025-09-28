from flask import Flask, render_template, request, redirect, session, send_from_directory, flash
import os
from dotenv import load_dotenv

# Load environment variables from .env file (DEMO_PASSWORD)
load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secure secret key for session encryption

# Password loaded from environment variable or default fallback
PASSWORD = os.getenv("DEMO_PASSWORD", "teachme123")

@app.route("/")
def home():
    # Redirect logged in users to index, others to login
    if session.get("logged_in"):
        return redirect("/index")
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        # Check submitted password against PASSWORD
        if request.form.get("password") == PASSWORD:
            session["logged_in"] = True  # Mark user as logged in
            return redirect("/index")
        else:
            # Password incorrect: store error message to show on login page
            error = "Incorrect password, please try again."
    
    # Render login.html with optional error message
    return render_template("login.html", error=error)

@app.route("/logout")
def logout():
    # Clear session to log out the user
    session.clear()
    return redirect("/login")

# List of pages that require authentication
PROTECTED_PAGES = ["index", "data", "analysis", "reports"]

@app.route("/<page>")
def serve_page(page):
    # Only serve
