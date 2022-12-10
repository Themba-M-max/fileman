import sys 
import os  

class Account_Holder: 
    
    def __init__(self, name, surname, email, password):   
        self.name = name 
        self.surname = surname 
        self.password = password 
        self.email = email 
    
    def get_password(self): 
        return self.password
        
        
    def check_password(self, entered_password): 
        if self.password == entered_password: 
            return True 
        else: 
            return False 
        
