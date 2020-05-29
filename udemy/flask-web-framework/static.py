from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    return "static contents turorials"


@app.route('/static')
def static_method():
    return render_template('static.html')


if __name__ == "__main__":
    app.run()
