"""A simple flask web app"""
from flask import Flask
from app.controllers.calculator_controller import CalculatorController
from app.controllers.index_controller import IndexController

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/", methods=['GET'])
def index_get():
    """R"""
    return IndexController.get()


@app.route("/calculator", methods=['GET'])
def calculator_get():
    """R"""
    return CalculatorController.get()


@app.route("/calculator", methods=['POST'])
def calculator_post():
    """R"""
    return CalculatorController.post()


# @app.route("/table", methods=['GET'])
# def table_get():
#     users = User.query
#     return render_template('table.html')
