import tkinter as tk
import sys
import os

class IDE:
    def __init__(self):
        self.path = sys.executable
        self.platform = sys.platform
        
        self.check_installs()
        self.get_system_info()
        self.load_settings()
        self.run()

    def check_installs(self):
        if os.system('python dont_worry_about_this_error') == 2:
            print('Python installed.')
            print('Working.')
        else:
            print('')
            print('Python not installed (ERROR:P100)')
            input()
            exit()

    def get_system_info(self):
        print(self.path)
        print(self.platform)

    def load_settings(self):
        pass

    def run(self):
        while True:
            pass

if __name__ == '__main__':
    ide = IDE()
