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

from modules_and_packages.OS_methods.operating_system_module import OperatingSystem

OperatingSystem.show_directories("/home/Desktop")
OperatingSystem.get_current_working_directory()
OperatingSystem.copyFile("/home/mohammed/Downloads/Course/dev/Projects/modules_and_packages/OS_methods/demo_directory/demo_source_file.txt","/home/mohammed/Downloads/Course/dev/Projects/modules_and_packages/OS_methods/demo_directory/demo_destination_file.txt")

"""
OUTPUT:
['Notes', 'Clg']
/home/mohammed/Downloads/Course/dev/Projects
"""