from flask import Flask, render_template, request, redirect, session
import os
import random
import string
import secrets

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Case 1: Static password
STATIC_PASSWORD = "teachme123"

# Case 2: Random password using random module
def generate_random_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.SystemRandom().choice(chars) for _ in range(length))

RANDOM_PASSWORD = generate_random_password()
print(f"[Random Password] Use this password for /login/random : {RANDOM_PASSWORD}")

# Case 3: Secure password using secrets module
def generate_secure_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

SECURE_PASSWORD = generate_secure_password()
print(f"[Secure Password] Use this password for /login/secure : {SECURE_PASSWORD}")

# Home route: redirect to static login by default
@app.route("/")
def home():
    if session.get("logged_in"):
        return redirect("/index")
    return redirect("/login/static")

# Login route with mode argument
@app.route("/login/<mode>", methods=["GET", "POST"])
def login(mode):
    error = None
    if request.method == "POST":
        entered_password = request.form.get("password")

        # Decide which password to check based on mode
        if mode == "static":
            correct_password = STATIC_PASSWORD
        elif mode == "random":
            correct_password = RANDOM_PASSWORD
        elif mode == "secure":
            correct_password = SECURE_PASSWORD
        else:
            error = "Invalid login mode selected."
            return render_template("login.html", error=error, mode=mode)

        if entered_password == correct_password:
            session["logged_in"] = True
            return redirect("/index")
        else:
            error = "Incorrect password, please try again."

    return render_template("login.html", error=error, mode=mode)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login/static")

@app.route("/index")
def index():
    if not session.get("logged_in"):
        return redirect("/login/static")
    return "Welcome to the protected index page!"

if __name__ == "__main__":
    app.run(debug=True)
