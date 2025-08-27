from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def capture_info():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    
    ip = ip.split(',')[0]
    
    user_agent = request.user_agent.string
    
    with open("resultado.txt", "a") as f:
        f.write(f"[{datetime.now()}] IP: {ip}, User-Agent: {user_agent}\n")
    
    return "<h2>Gracias, te hemos robado informacion</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)