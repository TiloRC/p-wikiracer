from flask import Flask, render_template, request
import wikipedia
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        start = request.form['start']
        end = request.form['end']
        if (start != "") and (end == ""):
            search_list = get_searches(start, 5)
            return render_template('home.html', searches=search_list)
        if (start != "") and (end != ""):
            path_val = path(start, end)
            return render_template('output.html',path_val=path_val)
    return render_template('home.html')


# will replace by importing backend function 
def path(start, end):
    return ("The final path is " + start + " to " + end)

def get_searches(text, count):
    searches = wikipedia.search(text, results=count)
    return searches

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080)