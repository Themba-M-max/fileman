import sys 
import os 

class Accounts: 
    
    def __init__(self): 
        self.accounts = [] 
        
    def add_account(self, account): 
        self.accounts.append(account) 
        
    def find_account(self, account): 
        if (account in self.accounts): 
            return True 
        else: 
            return False
