from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('nsw.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    return "TfNSW Shift Manager API is running."

@app.route("/shifts")
def shifts():
    conn = get_db_connection()
    shifts = conn.execute("SELECT * FROM shifts").fetchall()
    conn.close()
    return jsonify([dict(row) for row in shifts])
