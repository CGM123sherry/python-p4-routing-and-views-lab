#!/usr/bin/env python3

from flask import Flask

# initialize the Flask app
app = Flask(__name__)

# route for the index
@app.route("/")
def index():
    return """<h1>Python Operations with Flask Routing and Views</h1>"""

# route to print the string in the console and display in the browser
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print (parameter)
    return parameter

#  route to display a range of numbers
@app.route('/count/<int:parameter>')
def count(parameter):
    # Join numbers with '\n' to match the test case expectations
    return '\n'.join(str(i) for i in range(parameter)) + '\n'


@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation", 400  # Return an error if the operation is invalid

    # Return only the result, not the full equation
    return str(result)



if __name__ == '__main__':
    app.run(port=5555, debug=True)

