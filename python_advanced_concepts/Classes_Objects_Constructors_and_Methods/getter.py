"""
Create a class Student with parameterised constructor name and gender. Create a getter which
returns name in the format Mr. <<name>> if the gender is Male, Ms. <<name>> if the gender is
Female.
"""

class Student:
    def __init__(self,name,gender):
        self.gender = gender
        self.student_name = name
        


    @property
    def student_name(self):
        return self.__name

    @student_name.setter
    def student_name(self,n):
        if self.gender == "M":
            self.__name ="Mr." + n
        else:
            self.__name ="Ms." + n

s = Student("Mohammed","M")
print(s.student_name)
<<<<<<< HEAD
        

"""
OUTPUT
------

Mr.Mohammed
"""
=======
        
>>>>>>> f4a432e43e1c420deba039be95be3d5c36c7b43a
