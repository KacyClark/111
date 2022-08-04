from flask import Flask  # we imported Flask class 

app = Flask(__name__)# app is an instance

@app.route("/")   #this is a route
def index():    # our view function
    return "<h1>Hello world</h1>"  # return string

@app.route("/about")
def about(): 
    me = {
        "first_name": "Kacy",
        "last_name": "Clark",
        "hobby": "raise dogs",
        "former_job": "critical_care_RN"
    }
    return me

