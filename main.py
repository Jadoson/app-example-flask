from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Test 2"

if __name__ == "__main__":
    port = 8080
    app.run(debug=True,host='0.0.0.0',port=port)
