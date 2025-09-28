from flask import Flask, render_template, request, redirect, session, send_from_directory
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)

PASSWORD = os.getenv("DEMO_PASSWORD", "teachme123")

@app.route("/")
def home():
    if session.get("logged_in"):
        return redirect("/index")
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form.get("password") == PASSWORD:
            session["logged_in"] = True
            return redirect("/index")
        return "Wrong password", 401
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

PROTECTED_PAGES = ["index", "data", "analysis", "reports"]

@app.route("/<page>")
def serve_page(page):
    if page not in PROTECTED_PAGES:
        return "Page not found", 404
    if not session.get("logged_in"):
        return redirect("/login")
    return send_from_directory("content/protected", f"{page}.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

