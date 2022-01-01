
from flask import request

ask = request.get('http://127.0.0.1:5000/new')

if ask.status_code == 200:
    print(ask.json())