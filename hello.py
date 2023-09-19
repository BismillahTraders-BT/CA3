from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/add/<int:a>/<int:b>")
def add(a,b):
    return str(a+b)

@app.route("/sub/<int:a>/<int:b>")
def sub(a, b):
    result = str(a - b)
    return result

@app.route("/mul/<int:a>/<int:b>")
def mul(a, b):
    return str(a * b)

if __name__ == "__main__":
    app.run(host="0.0.0.0")