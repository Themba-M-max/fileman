from distutils.log import error
from sqlite3 import connect
from flask import request,redirect,make_response,render_template,url_for,session
from werkzeug.utils import secure_filename
import re
import psycopg2
import psycopg2.extras
from flask_bcrypt import generate_password_hash,check_password_hash
import os
from flask_session import Session
import dotenv
from modules.Directory import Directory




class auth_controller:
    def db_connection():
        """Code taken from: https://www.digitalocean.com/community/tutorials/how-to-use-a-postgresql-database-in-a-flask-application"""
        conn = psycopg2.connect(host='localhost',database='fileman',user=os.environ['DB_USERNAME'],password=os.environ['DB_PASSWORD'])
        return conn
    def validate_email(email):
        pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
        if re.match(pattern,email):
            return True
        return False
    
    def register(parent_path):
        pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
        error_message = ""
        error_check = False
        conn = psycopg2.connect(host='localhost',database='fileman',user=os.getenv('DB_USERNAME'),password=os.getenv('DB_PASSWORD'))
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            confPass = request.form['confpassword']
            if len(password)!=0:
                password_hash =  generate_password_hash(password).decode('utf-8')
            cursor.execute('SELECT * FROM users WHERE email = %s', (username,))

            record =  cursor.fetchone()
            if not re.match(pattern,username) or len(username)==0: # check if email valid
                error_message = "Please enter a valid email address"
                res = make_response(render_template('register.html',error_message=error_message))
            elif password != confPass:
                error_message = "Passwords do not match!"
                res = make_response(render_template('register.html',error_message=error_message))
            elif password==confPass and len(password) < 8 or len(password)==0:
                error_message = "Password length should be atleast 8 characters"
                res = make_response(render_template('register.html',error_message=error_message))
            elif record:
                error_message = "Account already exists!"
                res = make_response(render_template('register.html',error_message=error_message))
            else:
                cursor.execute('INSERT INTO users (email,password) VALUES (%s,%s)',(username,password_hash))
                conn.commit()
                error_message = "Sucessfully registered"
                session["user"] = request.form.get("username")
                if os.path.exists(os.path.join(parent_path,'users')):
                    folder_path = os.path.join(parent_path,'users',username)
                    print('This is the folder path:',folder_path)
                    os.mkdir(folder_path)
                    working_path = os.path.join(os.getcwd(),'users',session['user'])
                    Directory.set_current_working_dir(working_path)
                else:
                    os.mkdir(os.path.join(parent_path,'users'))
                    folder_path = os.path.join(parent_path,'users',username)
                    print('This is the folder path:',folder_path)
                    os.mkdir(folder_path)
                    working_path = os.path.join(os.getcwd(),'users',session['user'])
                    Directory.set_current_working_dir(working_path)
                res = make_response(redirect('/my-files'))
                return res

        res = make_response(render_template('register.html',error_message=error_message))
        return res 
    def login():
        conn = psycopg2.connect(host='localhost',database='fileman',user=os.getenv('DB_USERNAME'),password=os.getenv('DB_PASSWORD'))
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        error_message =""
        if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            password = request.form['password']
            cursor.execute('SELECT * FROM users WHERE email = %s', (username,))
            record =  cursor.fetchone()

            if record:
                current_hash =  record['password']
                if check_password_hash(current_hash,password):
                    session['user'] = request.form.get("username")
                    working_path = os.path.join(os.getcwd(),'users',session['user'])
                    Directory.set_current_working_dir(working_path)
                    res =  make_response(redirect(url_for('get_my_files')))
                   
                    return res
                else:
                    error_message = 'Invalid username/password'
                    res = make_response(render_template('login.html',error_message=error_message))
            else:
                error_message = 'Invalid username/password'
                res = make_response(render_template('login.html',error_message=error_message))

        res = make_response(render_template('login.html',error_message=error_message))
        return res