from flask import Flask, render_template
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return render_template('template.html')
    
@app.route("/hello/<name>")
def hello_person(name):
    return render_template('template.html',my_string=name )
    
@app.route("/jedi/<first>/<last>")
def jedi(last,first):
    return render_template('jedi.html',lst=last[:3], fst=first[:2])
    
if __name__ == "__main__":
    app.run(debug = True, host=environ['IP'],
            port=int(environ['PORT']))
