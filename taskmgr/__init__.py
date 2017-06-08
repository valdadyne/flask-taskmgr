from flask import Flask
from tinydb import TinyDB

app = Flask(__name__)
db = TinyDB('db.json')

from taskmgr import models, views
