from flask import Flask, render_template
from flask import request
from flask_bootstrap import Bootstrap
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

bootstrap = Bootstrap(app)
