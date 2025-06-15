# Simple Arithmetic Calculator

from flask import Flask, render_template, request

main = Flask(__name__)

@main.route('/', methods=['GET', 'POST'])

def home():
    result = None
    if request.method == 'POST':
        x = float(request.form['x'])
        y = float(request.form['y'])
        operation = request.form['operation']

        if operation == '+':
            result = x + y
        elif operation == '-':
            result = x - y
        elif operation == '*':
            result = x * y
        elif operation == '/':
            if y == 0:
                result = "Error: Division by zero"
            else:
                result = x / y
        elif operation == '%':
            result = x % y
        elif operation == '**':
            result = x ** y
        else:
            result = "Invalid operation"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    main.run(debug=True)