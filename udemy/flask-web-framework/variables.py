from flask import Flask


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    return "hello world", 200


@app.route('/getname', methods=["GET"])
def get_name() -> str:
    return "Leonardo Anjos"


@app.route('/name/<name>', methods=["GET"])
def name(name):
    return 'hello %s' % name


@app.route('/age/<int:age>', methods=["GET"])
def get_age(age):
    return "your age is %d" % age, 500


if __name__ == "__main__":
    app.run(port=5500)
