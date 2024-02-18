# Create a simple app using flask

from flask import Flask,render_template,request,redirect,url_for

# create flask app

app=Flask(__name__)


@app.route('/')
def home():
    return "<h1>It is home page</h1>"

@app.route('/content')
def content():
    return "It is content page"

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/success/<int:score>')
def success(score):
    return f"You have been passed.The score is : {str(score)}"


@app.route('/fail/<int:score>')
def fail(score):
    return f"You have been failed.The score is : {str(score)}"


@app.route('/calculate',methods = ['POST','GET'])
def calculate():
    if(request.method == "GET"):
        return render_template('calculate.html')
    else:
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        history = float(request.form['history'])
        
        averageMarks =(maths + science + history) / 3
        resultantPage = ''
        if averageMarks >= 50:
            resultantPage = 'success'
        else:
            resultantPage = 'fail'
        
        #return redirect(url_for(resultantPage,score = averageMarks))

        #return render_template("result.html",marks = averageMarks)
            
        return render_template("result.html",marks = averageMarks)



if __name__ == "__main__":

    app.run(debug=True)