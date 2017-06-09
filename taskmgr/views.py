from flask import render_template, request, redirect,session,url_for,json
from taskmgr import app,db
from tinydb import Query,where

# Users Model
Users = db.table(name='usr')

# Tasks Model
Tasks = db.table(name='tasks')

# SubTasks Model
SubTasks = db.table(name='sub_tasks')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/users')
def users():
    return render_template('users.html')


@app.route('/SignUp', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        message = None
        name = request.form['name']
        organization = request.form['organization']
        email = request.form['email']
        raw_pwd = request.form['password']

        if name and email and organization and raw_pwd:
            User = Query()
            if Users.search(User.email == email):
                message = "This User already exists."
            else:
                Users.insert({
                    'name': name,
                    'org': organization,
                    'email': email,
                    'password': raw_pwd
                })
                message = "User has been created successfully"
            return render_template('index.html', message=message)
        return render_template('users.html', message="Missing Credentials")
    return render_template('users.html')


@app.route('/SignIn', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        message = None
        email = request.form['email']
        raw_pwd = request.form['password']

        if email and raw_pwd:
            User = Query()
            if User.search((where('email') == email) & (where('password') == raw_pwd)):
                user = str(User['name'])
                message = "You're Logged in as" + user
                return render_template('index.html', message=message)
            else:
                message = "Incorrect Credentials. Try Again!!"
                return render_template('users', message=message)
        return render_template('users.html', message="Missing Credentials")
    return render_template('users.html')


@app.route('/dashboard', methods=['POST', 'GET'])
def dashboard():
    return render_template('dashboard.html')
