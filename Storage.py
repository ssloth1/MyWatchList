# James Bebarski
# December 13, 2022
# CS 5003: Recitation for CS 5001
# Final Project
# Storage.py

import ast

class Storage:
    
    def __init__(self, file):
        '''
        PARAMETERS: 
            - self
            - file - (The .txt file for the storage of all the items we are tracking.)
        
        ATTRIBUTES:
            - self.file - Attribute of Storage is the .txt file for the storage of all the items we are tracking.
        '''
        self.file = file
    
    # String method for Storage class.
    def __str__(self):
        '''
        class Storage
            Description: 
            - Displays the contents of the storage file'''
        with open(self.file, 'r') as file:
            
            if not file.readable():
                raise PermissionError("You do not have permission to read", file)
            
            lines = file.readlines()
            return print(lines)

    # Adds a new item to the storage file.
    def addItem(self, item_dict):
        '''
        class Storage
            Description: 
            - Adds a new item to the storage file.
        '''
        with open(self.file, "a") as file:
            
            if not file.writable():
                raise PermissionError("You do not have permission to append to", file)
            
            file.write(str(item_dict) + "\n")
        return
        
    # Removes an item from the storage file.
    def removeItem(self, my_key):
        '''
        class Storage
            Description:
            - Removes an item from the storage file.
        '''
        with open(self.file, "r") as file:
            
            if not file.readable():
                raise PermissionError("You do not have permission to read", file)
            
            lines = file.readlines()
        
        with open(self.file, 'w') as file:
            
            if not file.writable():
                raise PermissionError("You do not have permission to write to", file)
            
            for line in lines:
                if my_key not in line:
                    file.write(line)
        return
    
    # Prints all stored items.         
    def displayItems(self):
        '''
        class Storage
            Description:
            - Prints all stored items in file.
        '''
        with open(self.file, 'r') as file:
            
            if not file.readable():
                raise PermissionError("You do not have permission to read", file)
            
            for line in file:
               dictionary = ast.literal_eval((line.strip()))
               for key in dictionary:
                   if key != None:
                    print(key)  
        return      
    
    # Returns the links of an item as a list of strings, used by the Scrape class.
    def getLinks(self, my_key):
        '''
        class Storage
            Description:
            - Returns the links associated with an item as a list of strings.
        '''
        item_links = []
        with open(self.file, "r") as file:
            
            if not file.readable():
                raise PermissionError("You do not have permission to read", file)
            
            for line in file:
                dictionary = ast.literal_eval((line.strip()))
                for keys, values in dictionary.items():
                    for value in values:
                        if my_key in keys:
                            item_links.append(str(value))    
        return item_links          
        
    # Prints all links for an item.    
    def displayLinks(self, my_key):
        '''
        class Storage
            Description:
            - Prints all links associated with an item. 
        '''
        with open(self.file, "r") as file:
            
            if not file.readable():
                raise PermissionError("You do not have permission to read", file)
            
            for line in file:
                dictionary = ast.literal_eval((line.strip()))
                for keys, values in dictionary.items():
                    for value in values:
                        if my_key in keys:
                            print(str(value))                  
        return        
        
            
                
        
               

                    
                    
                     
                  
        

                    
       
        
    
        
            
    

