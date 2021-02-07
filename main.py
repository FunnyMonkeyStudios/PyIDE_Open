# Imports
import tkinter as tk # gui lib
import sys # sys lib
import os # os lib

# The GUI class for the window
class GUI: 
    def __init__(self): # This runs at the start of the class
        pass

# The core of the IDE
class IDE:
    def __init__(self): # This runs at the start of the class
        self.path = None # Python path varaible
        self.platform = None # Python path varaible
        
        self.check_installs() # Calls check_installs function
        self.get_system_info() # Calls get_system_info function
        self.load_settings() # Calls load_settings function
        
        self.run() # Main loof of the program

    def check_installs(self): # This checks if python is installed
        if os.system('python dont_worry_about_this_error') == 2: # If os.system('python etc') is 2 then python is installed
            print('Python installed.') # Tells the user py is installed
        else:
            print('') # Spacer
            print('Python not installed (ERROR:P100)') # P100 ERROR code is if python is not installed
            input() # Gets user input
            exit() # Quits

    def get_system_info(self): # This gets the system info function, This will be used to tell if the os linux or window or mac
        self.path = sys.executable # Gets the path of python
        self.platform = sys.platform # Gets the platform aka windows, mac, linux
        print(self.path) # Tells the user python path
        print(self.platform) # Tells the user what os

    def load_settings(self): # This will load settings for IDE
        pass

    def run(self): # Main loop
        while True:
            pass

if __name__ == '__main__':
    ide = IDE() # Makes the IDE class
