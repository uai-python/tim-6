import flask
from flask import render_template

app = flask.Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html', title='home')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
