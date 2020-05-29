from flask import Flask, request


app = Flask(__name__)


@app.route('/', methods=["POST"])
def index():
    if request.data:
        return _read_data(request.data)


def _read_data(data):
    return data['name']


if __name__ == "__main__":
    app.run(port=5500)
