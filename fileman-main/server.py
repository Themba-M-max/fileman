from crypt import methods
from urllib import request
from flask import Flask, render_template,redirect,request, send_file,session
from flask_session import Session
from werkzeug.utils import secure_filename
from os import getcwd, path,listdir, urandom
import datetime
from controllers.controller import controller
from controllers.auth_controller import auth_controller


app =Flask(__name__,static_folder='static',)
app.secret_key = 'fileman_secret_key'+str(urandom(24))
app.config['UPLOAD_FOLDER'] = 'uploaded/files'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
server_path = path.abspath(path.dirname(__file__))
file_path = path.join(path.abspath(path.dirname(__file__)),app.config['UPLOAD_FOLDER'])



@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")
@app.errorhandler(405)
def not_allowed(e):
    return render_template("404.html")
@app.route('/',methods=['GET','POST'])
@app.route('/home',methods=['GET','POST'])
def home():
    '''renders the home page using the controller class'''
    return controller.homepage()

@app.route('/upload',methods=['POST'])
def uploadroute():
    '''renders the upload page using a method from the controller class'''
    return controller.upload_page()

@app.route('/directory')
def show_files():
    ''''
    Uses the controller method to get the files from a specific path
    '''
    return controller.current_files(file_path)

@app.route('/login', methods=['GET','POST'])
def login():
    return auth_controller.login()
    
@app.route('/register',methods=['GET','POST'])
def register():
    return auth_controller.register(server_path)

@app.route('/my-files',methods=['GET'])
def get_my_files():
    
    return controller.main_page()

@app.route('/my-files',methods=['POST'])
def post_my_files():
    if not "back" in request.form:
        return controller.create_directory()
    else:
        return controller.go_up_directory()

@app.route('/about',methods=['GET','POST'])
def about():
    return render_template('about.html') 

@app.route('/logout') 
def logout(): 
    return controller.logout()  


@app.route('/search', methods = ["POST","GET"] )
def search_file():
    return controller.search_files()



if __name__ == '__main__':
   app.run('192.168.56.102',debug = True)