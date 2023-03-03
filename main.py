from flask import Flask, jsonify, render_template, request
from forms import AddNumbersForm
import os
import math

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


def addit(num1, num2):
    
    dayendcount=num1
    
    calRSValue=num2

    levelDist={}
    keyval="R"

    for i in range(0,2):
        testval=dayendcount
        for j in range(1,4):
            Sqrt=math.sqrt(int(testval))
            diskey=keyval+str(j)
            if i == 0:
                val1=Sqrt + float(calRSValue)
            elif i == 1:
                val1=Sqrt - float(calRSValue)
            
            ret=val1 * val1
            testval=ret
            
            levelDist[diskey]=ret
            # print(ret)
        keyval="S"
    print(levelDist)
    return str(levelDist)


@app.route('/', methods=['GET', 'POST'])
def add_numbers():
    num1 = None
    num2 = None
    op = None
    form = AddNumbersForm()

    if request.method == 'POST':
        num1 = form.num1.data
        num2 = form.num2.data
        op = addit(num1, num2)

    return render_template('addNumbers.html', form=form, sum=op)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
