from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET")

@app.route('/')
def index():
    return render_template('index.html')

# Route for serving static files
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)
