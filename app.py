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
            # (item0, item1, item2, item3, item4) = convert_to_dropdown(search_list)
            r_template = convert_to_dropdown(search_list) #render_template('home.html', rslt_l_0=item0, rslt_l_1=item1, rslt_l_2=item2, rslt_l_3=item3, rslt_l_4=item4)
            return r_template
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

def convert_to_dropdown(search_list):

    def switch(s_list):
        if len(s_list) == 0:
            return render_template('home.html', rslt_l_0="No results found...")
        elif len(s_list) == 1:
            return render_template('home.html', rslt_l_0=s_list[0])
        elif len(s_list) == 2:
            return render_template('home.html', rslt_l_0=s_list[0], rslt_l_1=s_list[1])
        elif len(s_list) == 3:
            return render_template('home.html', rslt_l_0=s_list[0], rslt_l_1=s_list[1], rslt_l_2=s_list[2])
        elif len(s_list) == 4:
            return render_template('home.html', rslt_l_0=s_list[0], rslt_l_1=s_list[1], rslt_l_2=s_list[2], rslt_l_3=s_list[3])
        elif len(s_list) == 5:
            return render_template('home.html', rslt_l_0=s_list[0], rslt_l_1=s_list[1], rslt_l_2=s_list[2], rslt_l_3=s_list[3], rslt_l_4=s_list[4])


    return switch(search_list)

    # items = ()

    # for idx in range(0,5):
    #     if (idx < len(search_list)):
    #         items = items + (search_list[idx],)
    #     else:
    #         items = items + (None,)

    # return items

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080)