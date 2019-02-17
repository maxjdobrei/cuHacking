from flask import Flask, render_template, request, session
from cuSchedulingParser import *

session = {}
session['scheduleIndex'] = 0
session['schedules'] = [[
        {
            'days': ["Tuesday","Thursday"],
            'startTime': (8,35),
            'endtime': (9,55),
            'name': 'COMP1406',
            'location': "Azreili Theater"

        }
        ],
        [

    ]]
session['schedules'] = [[]]

app = Flask(__name__)

@app.route("/main", methods=['GET','POST'])
def hello():

    days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    courses = []

    if request.method == 'POST':
        if request.form['form'] == 'generate':
            term = request.form['term']

            myBreak = request.form['break']
            if myBreak != "":
                addT = 0
                if(myBreak[-2:-1] == "PM"):
                    addT = 12
                myBreak = str(int(myBreak[:2])+addT)+":"+myBreak[3:5]

            timePreference = request.form['time-preference']

            for i in range(1,7,1):
                if request.form['course'+str(i)] != "":
                    courses.append(request.form['course'+str(i)])

            session['schedules'] = superMain(term,courses,myBreak,timePreference)
            session['scheduleIndex'] = 0

        if request.form['form'] == 'previous':
            session['scheduleIndex'] -= 1
            if session['scheduleIndex'] < 0:
                session['scheduleIndex'] = len(session['schedules'])-1

        if request.form['form'] == 'next':
            session['scheduleIndex'] += 1
            if session['scheduleIndex'] > len(session['schedules'])-1:
                session['scheduleIndex'] = 0
    
    return render_template("main.html",days = days, schedule = session['schedules'][session['scheduleIndex']])

if __name__ == '__main__':
    app.run(debug=True)