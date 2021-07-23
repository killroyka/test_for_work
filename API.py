from datetime import datetime
from time import strptime
from email_validator import validate_email, EmailNotValidError
from flask import jsonify
from flask_restful import reqparse, abort, Api, Resource
from pprint import pprint
from tinydb import TinyDB, Query


class GetName(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("fields", required=True, action='append')

    def post(self):
        args = self.parser.parse_args()['fields']
        dict_args = {}
        db = TinyDB('db.json')
        for x in range(len(args)):
            args[x] = args[x].split("=")
            dict_args[args[x][0]] = args[x][1]
            date = False
            for format in ['%d.%m.%Y', '%Y.%m.%d', '%d-%m-%Y', '%Y-%m-%d']:
                try:
                    date = strptime(args[x][1], format)
                except:
                    pass
            try:
                valid = validate_email(args[x][1])
            except EmailNotValidError as e:
                valid = False
            if date:
                dict_args[args[x][0]] = "date"
            elif args[x][1][:2] == "+7" and len(args[x][1]) == 12:
                dict_args[args[x][0]] = "number"
            elif valid:
                dict_args[args[x][0]] = "email"
            else:
                dict_args[args[x][0]] = "text"
        all_templates = db.all()
        for x in all_templates:
            for y in x.keys():
                if y != "name" and y in list(dict_args.keys()) and x[y] == dict_args[y]:
                    pass
                elif y == 'name':
                    pass
                else:
                    break
            else:
                return jsonify({'name': x["name"]})
        return jsonify(dict_args)
