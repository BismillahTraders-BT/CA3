from flask import Flask

def add(a,b):
    return (a+b)

def mul(a, b):
    return a * b

def sub(a, b):
    result = a - b
    return result

app = Flask(_name_)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/add/<int:a>/<int:b>")
def add(a,b):
    return (a+b)

@app.route("/sub/<int:a>/<int:b>")
def sub(a, b):
    result = a - b
    return result

@app.route("/mul/<int:a>/<int:b>")
def mul(a, b):
    return a * b

if _name_ == "_main_":
    app.run(host="0.0.0.0")