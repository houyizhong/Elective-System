# onwer:houyizhong
import pickle

class School(object):
    def __init__(self,school_site):
        self.school_site = school_site

    def set_course(self):
        enter_course = input('course:')
        enter_price = input('price')
        enter_cycle = input('cycle')
        return Course(enter_course,self.school_site,enter_price,enter_cycle)

    def set_class(self):
        enter_name = input('class name:')
        enter_course = input('course:')
        enter_price = input('price:')
        enter_cycle = input('cycle:')
        return The_Class(self.school_site,enter_course,enter_price,enter_cycle,enter_name)

class Course(School):
    def __init__(self,course_name,school_site,price,cycle):
        School.__init__(self,school_site)
        self.course = course_name
        self.price = price
        self.cycle = cycle

class The_Class(Course):
    def __init__(self,school_site,course_name,price,cycle,class_name):
        Course.__init__(self,course_name,school_site,price,cycle)
        self.class_name = class_name

    def set_teacher(self):
        enter_teacher = input('teacher:')
        return Teacher(self.school_site,self.course,self.price,self.cycle,self.class_name,enter_teacher)

    def set_student(self):
        enter_student = input('student:')
        return Student(self.school_site,self.course,self.price,self.cycle,self.class_name,enter_student)

class Teacher(The_Class):
    def __init__(self,school_site,course_name,price,cycle,class_name,teacher):
        #class_name = self.class_name
        #teacher = self.teacher
        #course = self.course
        The_Class.__init__(self,school_site,course_name,price,cycle,class_name)
        self.teacher = teacher

    def manager_class(self):
        pass

    def view_student_list(self):
        pass

    def edit_student_results(self):
        pass

class Student(The_Class):
    def __init__(self,school_site,course,price,cycle,class_name,student_name):
        The_Class.__init__(self,school_site,course,price,cycle,class_name)
        self.student_name = student_name

    def pay_tuition(self):
        pass


def write_to_file(file,data):
    f=open(file,'wb')
    pickle.dump(data,f)
    f.close()

#Teacher1=Teacher('beijing','class_1','wang','python')
#print(Teacher1.teacher)

#Student1=Student('beijing','class_1','wang','python','hou')
#print(Student1.course,Student1.teacher)

Beijing = School('beijing')
Shanghai = School('shanghai')

#print(Beijing.school_site,Shanghai.school_site)

Python = Course('python','beijing',10000,8)
#print(Python.course_name,Python.school_site,Python.price,Python.cycle)

Linux = Course('linux','beijing',8000,6)
#print(Linux.course_name,Linux.school_site,Linux.price,Linux.cycle)
Go = Course('go','shanghai',11000,8)
#print(Go.course_name,Go.school_site,Go.price,Go.cycle)

members = [Beijing,Shanghai]
for member in members:
    #member_course=member.set_course()
    member_class = member.set_class()
    member_teacher = member_class.set_teacher()
    #print(member_course.school_site,member_course.course_name,member_course.price,member_course.cycle)
    print(member_teacher.teacher)
