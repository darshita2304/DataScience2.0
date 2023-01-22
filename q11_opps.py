## 15th jan - Task List Assignments
## Author: Darshita Paghadal
## Q11: give 10 different example of polymorphism, encaptulation, data abstraction, overloading, overriding, multiple inheritance

# oevrriding methods - Plymorphism
class test5:
    def test(self):
        return " this is my test meth"

class test6:
    def test(self):
        return "this is my meth from class test 6"

class test7(test5):
    def test(self):
        return  "this is my test from test7"


vtest7 = test7()
print(vtest7.test()) ##method overriding.. call last method which is latest


#excapsulation - excapsulationg data (variables and methods) in a signle unit

class Employee:
    def __init__(self, name, dept, project):
        self.name = name
        self.dept = dept
        self.project = project

    def working(self, name):
        print(f"{name} is working on {self.project} in {self.dept}")

e = Employee('darshita', "development", "AI")
e.working('darshtia')

"""
Abstraction in python is defined as a process of handling complexity by hiding unnecessary 
information from the user"""

class vehicle:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def saycolor(self, brand):
        print(f"{self.brand} has {self.color} available")

class car(vehicle):
    def __init__(self, color, brand, model):
        vehicle.__init__(self, color, brand)
        self.model = model

c = car("red","Hundai","i20")
c.saycolor("Hundai")



