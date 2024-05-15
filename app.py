from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hellp_world():
    return render_template("index.html")


@app.route('/menu')
def name():
    return render_template("menu.html")


if __name__ == "__main__":
    app.run(debug=True)