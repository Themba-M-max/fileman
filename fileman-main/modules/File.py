
from hashlib import new
from os import listdir,path,rename
import magic
from bs4 import BeautifulSoup
import codecs

class File: 
    
    def __init__(self, filename, size): 
        self.filename = filename 
        self.size = size
    def checkExtension(old_file,new_file):
        pos_old_ex = old_file.index('.')
        pos_new_ex =  new_file.index('.')
        
    def rename(old_name, new_name): 
        if path.exists(new_name) or path.isdir(new_name):
            return False
        else:
            rename(old_name,new_name)
            return True
        
    def get_size(self): 
        return self.size
    def open_file(filename):
        allowed_mime =['text/csv','text/html','	application/json','text/plain','application/xml','text/xml']
        
        if path.exists(filename) and not path.isdir(filename) and file_mime in allowed_mime:
            file_mime =  magic.from_file(filename, mime=True)
            if file_mime == 'text/html' or file_mime=='application/xml' or file_mime=='text/xml':
                html_file = codecs.open(filename,'r')
                return html_file.read()
            elif file_mime == 'text/plain':
                text_file = open(filename,'r')
                return text_file.read()
            else:
                return ""
        else:
            return ""

    def get_files(file_path):
        files = []
        folders = []
        for file in listdir(file_path):
            if not path.isdir(path.join(file_path,file)):
                current_file = file
                # print(f"MIME of {file} is ",magic.from_file(path.join(file_path,file), mime=True))
                files.append(current_file)
            else:
                folders.append(file)
        return folders,files
    