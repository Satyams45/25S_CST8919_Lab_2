from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ App is running"

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == "admin" and password == "password":
        app.logger.info(f"SUCCESSFUL LOGIN: {username}")
        return "Login successful", 200
    else:
        app.logger.warning(f"FAILED LOGIN: {username}")
        return "Login failed", 401
