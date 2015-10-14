from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from models import Result

@app.route('/')
def hello():
    return "Hello world!"

@app.route('/<name>')
def hello_name(name):
    return "hello {}!".format(name)

if __name__ == '__main__':
    app.run()
