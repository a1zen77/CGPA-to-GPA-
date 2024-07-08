from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/" , methods=["GET" , "POST"])
def hello_world():
    if request.method == "GET":
        return render_template("cgpa.html")
    elif request.method == "POST":
        x = float(request.form["user_name"])
        value1 = float(x/2.5)
        y=round(value1,2)
        value2 = float(x*9.5)
        z=round(value2,2)
        return render_template("gpa.html" , GPA=y , Percentage=z)
    else:
        print("Error check")
app.run()