"""A simple flask web app"""
from flask import Flask, render_template
from controllers.index_controller import IndexController
from controllers.calculator_controller import CalculatorController
from table import User

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()


@app.route("/calculator", methods=['GET'])
def calculator_get():
    return CalculatorController.get()


@app.route("/calculator", methods=['POST'])
def calculator_post():
    return CalculatorController.post()


@app.route("/table", methods=['GET'])
def table_get():
    users = User.query
    return render_template('table.html')
