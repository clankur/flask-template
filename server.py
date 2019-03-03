from flask import Flask, redirect, render_template, request
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template("index.html")
    
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)