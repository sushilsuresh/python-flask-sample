from flask import Flask
application = Flask(__name__)
import os

@application.route("/")
def hello():
    node = os.uname().nodename
    return "Hello World! - from - " + node

if __name__ == "__main__":
    application.run()
