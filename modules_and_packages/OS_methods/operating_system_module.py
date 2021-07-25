"""
Create a simple python class OperatingSystem with following methods Hint: Use OS module
1. show_directories(“path”) -> This function should print list of directories in a given
path. Example: show_directories(“C://myfolder") should list files inside myfolder of
C drive.
2. get_current_working_directory() -> This function should print the current working
directory.
3. copyFile(source, destination) -> This function should copy a file from a given
source path to given destination path. For example: source : C:/talentpy/test.txt
and destination is D:/talent/myfolder. Then this function should copy test.txt to D:/
talent/myfolder.
Create another file runner.py and import OperatingSystem class and call show_directories,
get_current_working_directory and copyFile methods.
"""

import os,shutil
from os import path

class OperatingSystem:
    def show_directories(file_path):
        if(path.isdir(file_path)):
            print(os.listdir(file_path))

    def get_current_working_directory():
        print(os.getcwd())

    def copyFile(source,destination):
        shutil.copyfile(source,destination)
