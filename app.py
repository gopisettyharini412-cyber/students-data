from flask import Flask, render_template, request
import mysql.connector
import os

app = Flask(__name__)

# =========================
# DATABASE CONNECTION
# =========================
def get_db_connection():
    print("DB HOST:", os.environ.get("DB_HOST"))
    try:
        return mysql.connector.connect(
            host=os.environ.get("DB_HOST"),
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASSWORD"),
            database=os.environ.get("DB_NAME"),
            port=int(os.environ.get("DB_PORT", 3306))
        )
    except Exception as e:
        print("DB Connection Error:", e)
        return None

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
    course = request.form["course"]

    db = get_db_connection()
    cursor = db.cursor()

    sql = "INSERT INTO registrations (name, phone, email, course) VALUES (%s, %s, %s, %s)"
    values = (name, phone, email, course)

    cursor.execute(sql, values)
    db.commit()

    cursor.close()
    db.close()

    return render_template("success.html")

# =========================
# RUN APP
# =========================
if __name__ == "__main__":
    app.run(debug=True)
