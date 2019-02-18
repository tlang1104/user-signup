from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/", methods=['POST'])
def verify_email():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''

# valid username arguments
    if len(username) < 1:
        username_error = "You can't leave your Username blank!"
        username = username
        password = ''
        verify_password = ''
        email = email
        return render_template('index.html', username_error=username_error, username=username, email=email)
    elif ' ' in username:
        username_error = "No spaces in your Username allowed"
        username = username
        password = ''
        verify_password = ''
        email = email
        return render_template('index.html', username_error=username_error, username=username, email=email)
    elif len(username) < 3:
        username_error = "Your Username must be more than 3 characters"
        username = username
        password = ''
        verify_password = ''
        email = email
        return render_template('index.html', username_error=username_error, username=username, email=email)
    elif len(username) > 20:
        username_error = "Your Username must be less than 20 characters"
        username = username
        password = ''
        verify_password = ''
        email = email
        return render_template('index.html', username_error=username_error, username=username, email=email)
    elif username == "me":
        username_error = "'Me' is not a valid username"
        username = username
        password = ''
        verify_password = ''
        email = email
        return render_template('index.html', username_error=username_error, username=username, email=email)

# valid password arguement     
    if len(password) < 1:
        password_error = "You can't leave your Password blank!"
        username = username
        password = ''
        verify_password = ''
        email = email
        return render_template('index.html', password_error=password_error, username=username, email=email)
    elif ' ' in password:
        password_error = "No spaces allowed in your password"
        username = username
        password = ''
        verify_password = ''
        return render_template('index.html', password_error=password_error, username=username, email=email)
    elif len(password) < 3:
        password_error = "Your Password must be more than 3 characters"
        username = username
        password = ''
        verify_password = ''
        email = email
        return render_template('index.html', password_error=password_error, username=username, email=email)
    elif len(password) > 20:
        password_error = "Your Password must be less than 20 characters"
        username = username
        password = ''
        verify_password = ''
        email = email
        return render_template('index.html', password_error=password_error, username=username, email=email)
    elif password == "me":
        password_error = "'Me' is not a valid password"
        username = username
        password = ''
        verify_password = ''
        email = email
        return render_template('index.html', password_error=password_error, username=username, email=email)

# verify password
    if verify_password != password:
        verify_password_error = "Your passwords don't match"
        username = username
        password = ''
        verify_password = ''
        email = email
        return render_template('index.html', verify_password_error=verify_password_error, username=username, email=email)

# verify email
    if email is '':
        return render_template('welcome.html', username=username)
    elif ' ' in password:
        email_error = "No spaces allowed in your email"
        username = username
        password = ''
        verify_password = ''
        email = email
        return render_template('index.html', email_error=email_error, username=username, email=email)
    elif len(email) < 3:
        email_error = "Your email must be more than 3 characters"
        username = username
        password = ''
        verify_password = ''
        email = email
        return render_template('index.html', email_error=email_error, username=username, email=email)
    elif len(email) > 20:
        email_error = "Your email must be less than 20 characters"
        username = username
        password = ''
        verify_password = ''
        email = email
        return render_template('index.html', email_error=email_error, username=username, email=email)
    elif '@' not in email:
        email_error = "Your email must contain an @ symbol"
        username = username
        password = ''
        verify_password = ''
        email = email
        return render_template('index.html', email_error=email_error, username=username, email=email)
    elif '.' not in email:
        email_error = "Your email must contain an @ symbol"
        username = username
        password = ''
        verify_password = ''
        email = email
        return render_template('index.html', email_error=email_error, username=username, email=email)
    
    return render_template('welcome.html', username=username)

@app.route('/welcome', methods=['POST'])
def welcome():
    encoded_error = request.args.get("error")
    return render_template("welcome.html")
   
@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template("index.html")

app.run()