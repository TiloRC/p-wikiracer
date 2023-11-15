from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        start = request.form['start']
        end = request.form['end']
        if (start != "") and (end != ""):
            path_val = path(start, end)
            return render_template('output.html',path_val=path_val)
    return render_template('home.html')


# will replace by importing backend function 
def path(start, end):
    return ("The final path is " + start + " to " + end)


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080)