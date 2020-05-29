from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    try:
        12/0
    except ZeroDivisionError as err:
        return "some server side error happened ", str(err)
    except:
        return "base exception class"


@app.errorhandler(500)
def server_error(error):
    return render_template("error_demo.html")


if __name__ == "__main__":
    app.run()
