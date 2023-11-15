from flask import Flask, render_template, request, jsonify
import time
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route("/", methods=['GET', 'POST'])
def send():
    return render_template('home.html')

@app.route('/api')
def api():
    response = {'message': 'Hello, World!'}
    return response

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080)