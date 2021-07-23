from tinydb import TinyDB, Query
from pprint import pprint

db = TinyDB('db.json')
pprint(db.all())
