from flask import Flask, jsonify
import pyodbc
import os

app = Flask(__name__)

def get_connection():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        f'SERVER={os.environ.get("SQL_SERVER")};'
        f'DATABASE={os.environ.get("DB_NAME")};'
        f'UID={os.environ.get("DB_USER")};'
        f'PWD={os.environ.get("DB_PASSWORD")}'
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
        "Connection Timeout=30;"
    )

@app.route('/users')
def users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, username, email FROM users")

    rows = cursor.fetchall()

    return jsonify([
        {
            "id": r[0],
            "name": r[1],
            "username": r[2],
            "email": r[3]
        }
        for r in rows
    ])

if __name__ == "__main__":
    app.run()