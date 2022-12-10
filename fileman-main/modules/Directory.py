from genericpath import exists
import os
from flask import session

class Directory: 
    
    def __init__(self): 
        self.files = [] 
        
    def add_file(self, file): 
        self.files.append(file) 
         
        
    def rename(old_name,new_name):
        current_filename  =os.path.join(session['cwd'],old_name) 
        new_filename = os.path.join(session['cwd'],new_name)
        if os.path.exists(new_filename) and not os.path.isdir(new_filename):
            os.rename(current_filename,new_filename)
            return True
        elif not os.path.exists(new_filename):
            os.rename(current_filename,new_filename)
            return True
        else:
            return False
    def up_directory():
        current_working_dir = session['cwd']
        new_path =""
        
        if session['cwd'] == os.path.join(os.getcwd(),'users',session['user']):
            print("Invalid")
            pass
        else:
            split_path = current_working_dir.split("/")
            for i in range(1,len(split_path)-1):
                new_path = os.path.join(new_path,split_path[i])
            new_path = "/"+new_path
            session['cwd'] = new_path
            # print(new_path,': does/not', os.path.exists(new_path) )


            print(split_path)
    def create_directory(file_path,folder_name):
        folder_to_create = os.path.join(file_path,folder_name)
        if os.path.exists(folder_to_create):
            return False
        else:
            os.mkdir(folder_to_create)
            return True
            
    def change_dir(destinationDir):
        potential_destination = os.path.join(session['cwd'],destinationDir)
        if os.path.exists(potential_destination):
            session['cwd'] = potential_destination
        


    def set_current_working_dir(file_path):
        session['cwd'] = file_path

    def get_current_working_dir():
        current_dir =  session["cwd"]
        return current_dir
