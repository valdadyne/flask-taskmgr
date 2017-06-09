from flask import Flask
from tinydb import TinyDB

app = Flask(__name__)
app.secret_key = 'some_secret'
db = TinyDB('db.json')

from taskmgr import models, views
