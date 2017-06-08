from flask import render_template, request, redirect
from taskmgr import app,db

Users = db.table('usr')
Tasks = db.table('tasks')
SubTasks = db.table('sub_tasks')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/users')
def users():
    return render_template('users.html')

@app.route('/SignUp', methods=['POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        organization = request.form['organization']
        email = request.form['email']
        raw_pwd = request.form['password']
