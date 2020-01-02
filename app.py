from flask import Flask, render_template
app= Flask(__name__, template_folder="src/templates")

@app.route('/hello')
def hello():
    return "hola"

@app.route('/')
def template():
    return render_template('index.html',name='Raquel')
