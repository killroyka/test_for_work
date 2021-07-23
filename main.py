import os

from flask import Flask
from tinydb import TinyDB, Query
from flask_restful import reqparse, abort, Api, Resource
import API

app = Flask(__name__)
api = Api(app)
api.add_resource(API.GetName, '/getform')


@app.route('/')
def hello():
    return 'Hello, World!'


def main():
    global admins
    admins = [1]
    port = int(os.environ.get("PORT", 5002))
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()
