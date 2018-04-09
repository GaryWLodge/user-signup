from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

  

@app.route("/", methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    ver_password = request.form['ver_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    ver_password_error = ''
    email_error = ''
    username1 = username
    if username == '' or len(username) < 3 or len(username) > 20 or ' ' in username:
        username_error = 'Enter a valid Username'
        username = username

    if password == '' or len(password) < 3 or len(password) > 20 or ' ' in password:
        password_error = 'Enter a valid Password'
        password = ''
    

    if ver_password != password:
        ver_password_error = 'Passwords do not match'
        ver_password = ''
    
    if email == '':
        email = ''
    else:    
        if '@' not in email or '.' not in email or len(email) < 3 or len(email) > 20: 
            email_error = 'Enter a valid Email'   
            email = email

    if not username_error and not password_error and not ver_password_error and not email_error:   
        return redirect('/valid_login?username='+ username)
    else:
        return render_template('index.html', username=username, password=password, ver_password=ver_password, email=email,
    username_error=username_error, password_error=password_error, ver_password_error=ver_password_error, email_error=email_error)    

    

@app.route("/")
def index():
    
    
    return render_template('index.html')


@app.route('/valid_login')
def valid_login():
    username = request.args.get('username')
    return render_template('welcome.html',username=username)   

app.run()    