from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Harini@08",
        database="academy",
        port=3306
    )

@app.route("/")
def home():
    return render_template("index.html")


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
    
if __name__ == "__main__":
    app.run(debug=True)