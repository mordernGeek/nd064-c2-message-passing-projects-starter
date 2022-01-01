
from flask import request

ask = request.get('http://localhost:5000/new')

if ask.status_code == 200:
    print(ask.json())