from flask import render_template, redirect
from taskmgr import app


@app.route('/')
def home():
    return render_template('index.html')
