from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def home():
    app.logger.debug("Home route accessed")
    return "Welcome to the Flask Calculator API!"

@app.route('/add', methods=['GET'])
def add():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    app.logger.debug(f"Addition: {a} + {b} = {a + b}")
    return jsonify(result=a + b)

@app.route('/subtract', methods=['GET'])
def subtract():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    app.logger.debug(f"Subtraction: {a} - {b} = {a - b}")
    return jsonify(result=a - b)

@app.route('/multiply', methods=['GET'])
def multiply():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    app.logger.debug(f"Multiplication: {a} * {b} = {a * b}")
    return jsonify(result=a * b)

@app.route('/divide', methods=['GET'])
def divide():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    if b == 0:
        app.logger.error("Division by zero attempted")
        return jsonify(error="Division by zero is not allowed"), 400
    app.logger.debug(f"Division: {a} / {b} = {a / b}")
    return jsonify(result=a / b)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
