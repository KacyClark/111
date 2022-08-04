 from flask import Flask

 app = Flask(__name__)
 @app.route("/aboutMe")  
 def aboutMe():
    me = {
        "first_name": "Kacy",
        "last_name": "Clark",
        "hobby": "raise dogs",
        "former_job": "critical_care_RN"
    }
    return me

@app.route("/dream_mate")
def mate():
    he = {
        "height": "tall",
        "build": "muscular",
        "skin": "dark",
        "educated": "hard_knocks"
    }    
    return he
