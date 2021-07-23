from requests import post
from tinydb import TinyDB, Query
from pprint import pprint

db = TinyDB('db.json')
pprint(db.all())

print("проверка, когда все поля совпадают")
a = post("http://localhost:5002/getform", params={
    'fields': ['email_field=killerbeesexy@gmail.com', 'password_field=sakhabiev213', 'phone_number_field=+79274580307',
               'username_field=killroyka']})
print(a.json())
print("роверка, когда есть лишние поля")
a = post("http://localhost:5002/getform", params={
    'fields': ['email_field_1=killerbeesexy@gmail.com', 'email_field_2=killerbeesexy@gmail.com',
               'email_field_3=killerbeesexy@gmail.com', 'email_field_4=killerbeesexy@gmail.com',
               'email_field_5=killerbeesexy@gmail.com']})
print(a.json())
print("проверка, когда записи вообще нет в бд")
a = post("http://localhost:5002/getform", params={
    'fields': ['test=проверка исключения< когда нет формы в бд', 'email_field_1=killerbeesexy@gmail.com',
               'phone_number_field=+79274580307']})
print(a.json())
