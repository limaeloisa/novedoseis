from flask import Flask
from flask import render_template
app = Flask(__name__)
@app.route("/")

def inicio():
    frutas = ['banana', 'maca', 'abacate']
    return render_template("inicio.html", f=frutas)                