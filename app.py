from flask import Flask, render_template, request;



app = Flask(__name__)

start = "Pomona"
end = "Tilo"

@app.route('/')
def home():

    

    return render_template('home.html', start=start, end=end, path=frontBackConnectionTest(start,end))



def frontBackConnectionTest(start, end):
        
    return start + "-> connecting path -> " + end


@app.route('/set-start', methods=['POST'])
def setStart():
    global start 
    global end
    start = request.form['start_input']
    return render_template('home.html', start=start, end=end, path=frontBackConnectionTest(start,end))

@app.route('/set-end', methods=['POST'])
def setEnd():
    global start
    global end 
    end = request.form['end_input']
    return render_template('home.html', start=start, end=end, path=frontBackConnectionTest(start,end))