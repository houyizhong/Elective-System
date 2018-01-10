class School(object):
    def __init__(self,school_site):
        self.school_site = school_site

class Course(School):
    def __init__(self,school_site,price,cycle):
        School.__init__(self,school_site)
        self.price = price
        self.cycle = cycle

class The_Class(Course):
    def __init__(self,teacher,course):
        self.teacher = teacher
        self.course = course

class Teacher(The_Class):
    def __init__(self,teacher_name,school_site):
        School.__init__(self,school_site)
        self.teacher_name = teacher_name

    def manager_class():
        pass

    def view_student_list():
        pass

    def edit_student_results():
        pass

class Student(The_Class):
    def __init__(self,school_site,class):
        School.__init__(self,school_site)
        self.class = class

    def pay_tuition():
        pass

Beijing = School('beijing')
Shanghai = School('shanghai')

Linux = Course('beijing',8000,6)
Python = Course('beijing',10000,8)
Go = Course('shanghai',11000,8)
