import os
from os import path,getcwd 
import shutil
from urllib import response
import urllib.parse
import re 
from pathlib import Path
from flask import request,redirect,make_response,render_template,url_for,session,flash,send_file
from werkzeug.utils import secure_filename
from modules.File import File
from modules.Directory import Directory 


class controller:
    
    def homepage():
        '''make the home page response to be sent back by the server'''

        if request.method == 'POST' and 'files' in request.form:
            res = make_response(redirect('/my-files'))
            return res
        elif request.method == 'POST' and 'start' in request.form:
            res = make_response(redirect('/register'))
            return res
        res =  make_response(render_template('home.html'))
        return res
    

    def upload_page():
        '''make the upload page response to be sent back by the server'''

        if request.method == 'POST' and 'upload' in request.form:
            files =  request.files.getlist('file[]')
            for file in files:
                if not file.filename == '':
                    file.save(path.join(session['cwd'],secure_filename(file.filename)))

            return redirect('/my-files')
        res =  make_response(redirect('/my-files'))
        return res 

    def main_page(): 
        '''make the main page response to be sent back by the server'''
        if "user" in session and "pathd" in request.args and "rename" in request.args:   #renaming a folder
            new_folder = urllib.parse.unquote_plus(request.args.get('rename'))
            print("This is the rename arg:",new_folder)
            old_folder = urllib.parse.unquote_plus(request.args.get('pathd'))
            if Directory.rename(old_folder,new_folder):
                print("I am on the true clase of rename in main")
                res = make_response(controller.current_files(session['cwd']))
                return res
            res = make_response(controller.current_files(session['cwd']))
            return res 

        elif "user" in session and "pathd" in request.args and "delete" in request.args:   #deleting a folder 
            dirPath = os.path.join(session['cwd'], request.args.get('pathd'))   
            if path.isdir(dirPath) and path.exists(dirPath):  
                if len(os.listdir(dirPath)) == 0:
                    os.rmdir(dirPath)  
                elif len(os.listdir(dirPath)) != 0: 
                    shutil.rmtree(dirPath)    
            res = make_response(controller.current_files(session['cwd'])) 
            return res   
        elif "user" in session and "pathd" in request.args and "download" in request.args and not request.args.get('pathd') =="":
            Downloaded = False
            folder_name = urllib.parse.unquote_plus(request.args.get('pathd'))
            if path.exists(path.join(session['cwd'],folder_name)):
                shutil.make_archive(path.join(session['cwd'],folder_name),'zip',path.join(session['cwd'],folder_name))
                Downloaded = True
                # @app.after_request(response)
                # def delete(response):
                #     os.remove(path.join(session['cwd'],folder_name+".zip"))
                #     return response
                return send_file(path.join(session['cwd'],folder_name+".zip"),as_attachment=True)
            # if Downloaded:
            #     os.remove(path.join(session['cwd'],folder_name+".zip"))
            res =  make_response(controller.current_files(session['cwd']))
            return res
        elif "user" in session and 'pathd' in request.args:                                #changing directories
            Directory.change_dir(request.args.get('pathd'))
            res = make_response(controller.current_files(session['cwd']))
            return res  

        elif "user" in session and "pathf" in request.args and "download" in request.args: #downloading a file
            pathName = path.join(session['cwd'],request.args.get('pathf'))
            if path.exists(pathName) and not path.isdir(pathName):
                return send_file(pathName, as_attachment=True)
            res = make_response(controller.current_files(session['cwd']))
            return res 

        elif "user" in session and "pathf" in request.args and "rename" in request.args:   #renaming a file
            newFile = urllib.parse.unquote_plus(path.join(session['cwd'],request.args.get('rename')))
            oldFile =  urllib.parse.unquote_plus(path.join(session['cwd'],request.args.get('pathf')))
            print("This is the new file:, ******",urllib.parse.unquote_plus(oldFile))
            if File.rename(old_name=oldFile,new_name=newFile):
                res = make_response(controller.current_files(session['cwd']))
                return res
            res = make_response(controller.current_files(session['cwd']))
            return res

        elif "user" in session and "pathf" in request.args and "delete" in request.args:  #deleting a file
            filePath = path.join(session['cwd'], request.args.get('pathf')) 
            if path.exists(filePath) and not path.isdir(filePath): 
                os.remove(filePath)  
            res = make_response(controller.current_files(session['cwd'])) 
            return res    
        elif "user" in session and 'open' in request.args and not request.args.get('open') =="":
            file =  path.join(session['cwd'],request.args.get('open'))
            # print("This is the file to be open", file)
            data= File.open_file(file)
            if data:
                res = make_response(render_template('codeeditor.html',data=data))
                return res
            else:
                res = make_response(controller.current_files(session['cwd']))
                return res
            
        elif "user" in session:
            res = make_response(controller.current_files(session['cwd']))                 #directing a user to their profile
            return res
        
        else:
            res = make_response(redirect("/login"))
        return res

    def go_up_directory():
        '''move bottom up through directory when user is only in session else redirect to login page as response'''
        if "user"  in session:
            Directory.up_directory()
            res = make_response(controller.current_files(session['cwd']))
            return res
        else:
            res = make_response(redirect('/login'))
            return res 


    def current_files(file_path):
        '''Use the file method to get files in a directory and use that to serve the download page'''
        back = False
        if not session['cwd'] == path.join(getcwd(),'users',session['user']):
            back=True
        folders,files = File.get_files(file_path)
        res = make_response(render_template('main.html', files=files,folders=folders,back=back))
        return res 



    def create_directory():
        '''create new  directory when user creates a new folder to upload'''
        if request.method == 'POST' and "Folder" in request.form:
            folder_name =  request.form['Folder']
            current_path = session['cwd']
            created = Directory.create_directory(current_path,folder_name)
            if created:
                res =  make_response(redirect(url_for('get_my_files')))
                return res
            else:
                flash('folder already exits')
                res =  make_response(redirect(url_for('get_my_files')))
                return res
        res =  make_response(redirect(url_for('get_my_files')))
        return res 

    def logout(): 
        '''pop current user session then redirect to mainpage'''
        session.pop('user', None) 
        return redirect('/')    

    

    
