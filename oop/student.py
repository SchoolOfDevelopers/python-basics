# # # Define Class
# class Student:
#
#     def __init__(self, name, roll_no):
#         self.name = name
#         self.roll_no = roll_no
#
#     def intro(self):
#         print("Hi, I am ", self.name, ". My roll No. is ", self.roll_no)


# INHERITANCE
# A ===> B, C, D


class Person:
    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name

    def print_name(self):
        print(self.first_name, self.last_name)


class Student(Person):
    def __init__(self, first_name, last_name, admission_year):
        super().__init__(first_name, last_name)
        self.admission_year = admission_year

    def print_name(self):
        print(self.first_name, self.last_name, self.admission_year)

    def go_to_class(self):
        print("I am just in the class room")


class Teacher(Person):
    pass


person = Person("Arindam", "Sarkar")
person.print_name()
student = Student("Arindam", "Sarkar", 2006)
student.print_name()
student.go_to_class()
teacher = Teacher("Mr. S", "Sarkar")
teacher.print_name()