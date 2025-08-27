import sqlite3
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('logs.db')
    conn.row_factory = sqlite3.Row  
    return conn

@app.route("/", methods=["GET"])
def capture_info():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    ip = ip.split(',')[0] 
    user_agent = request.user_agent.string

    conn = get_db_connection()
    cursor = conn.cursor()

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("INSERT INTO user_logs (ip, user_agent, timestamp) VALUES (?, ?, ?)", 
                   (ip, user_agent, timestamp))
    conn.commit()

    conn.close()

    return "<h2>Gracias, hemos registrado tu información</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)