from flask import Flask, render_template, request
import mysql.connector
import os

app = Flask(_name_)

# =========================
# DATABASE CONNECTION
# =========================
def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        database=os.environ.get("DB_NAME"),
        port=int(os.environ.get("DB_PORT", 3306))
    )

# =========================
# HOME PAGE
# =========================
@app.route("/")
def home():
    return render_template("index.html")

# =========================
# REGISTER FORM
# =========================
@app.route("/register", methods=["POST"])
def register():
    name = request.form["name"]
    phone = request.form["phone"]
    email = request.form["email"]

    db = get_db_connection()
    cursor = db.cursor()

    sql = "INSERT INTO registrations (name, phone, email) VALUES (%s, %s, %s)"
    values = (name, phone, email)

    cursor.execute(sql, values)
    db.commit()

    cursor.close()
    db.close()

    return render_template("success.html")

# =========================
# RUN APP
# =========================
if _name_ == "_main_":
    app.run(debug=True)
