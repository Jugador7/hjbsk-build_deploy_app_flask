from flask import Flask, render_template, request
from Maths.mathematics import summation, subtraction, multiplication
from flask_cors import CORS

app = Flask("Mathematics Problem Solver")
CORS(app)


@app.route("/sum")
def sum_route():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        result = summation(num1, num2)
        return str(result)
    except ValueError:
        return {"message": "Invalid input. Please enter numeric values."}, 400

@app.route("/sub")
def sub_route():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        result = subtraction(num1, num2)
        return str(result)
    except ValueError:
        return {"message": "Invalid input. Please enter numeric values."}, 400

@app.route("/mul")
def mul_route():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        result = multiplication(num1, num2)
        return str(result)
    except ValueError:
        return {"message": "Invalid input. Please enter numeric values."}, 400

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.errorhandler(404)
def api_not_found(error):
    return {"message": "API not found"}, 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
