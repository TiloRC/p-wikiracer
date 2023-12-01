from flask import Flask, render_template, request, jsonify
import time
from flask_cors import CORS, cross_origin
import wikipediaapi
import wikipedia

app = Flask(__name__)
CORS(app)

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route("/", methods=['GET', 'POST'])
def send():
    return render_template('home.html')

@app.route('/api')
@cross_origin()
def api():
    
    searchTerm = request.args.get("textInput")

    response = {'searchResult': get_searches(searchTerm,5)}

    return jsonify(response)


def get_searches(text, count):
    return wikipedia.search(text, results=count)

def stringfy_path_list(path_list):

    retStr = ""

    for elem in path_list[:-1]:
        retStr += elem + " -> "

    retStr += path_list[-1]

    return retStr


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080)




