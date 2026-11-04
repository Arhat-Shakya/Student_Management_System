import json
import string
import secrets
import os

if os.path.getsize("student.json") > 0 :
    with open("student.json","r") as f:
        lst_student = json.load(f)
        if lst_student != "":
            lst = lst_student
else:
    lst=[]                    

if os.path.getsize("subject.json") > 0 :
    with open("subject.json","r") as f:
        lst_subject = json.load(f)
        if lst_subject != "":
            lst1 = lst_subject
else:
    lst1=[]

#Student management system starts
class student_name_register:
    def __init__(self,name,id,age,email,phone_no,enroll_date):
        self.name = name
        self.id = id
        self.age = age
        self.email = email
        self.phone_no = phone_no
        self.enroll_date = enroll_date

    def register(self):
        self.dit = {}
        for val in lst:
            if self.name == val["name"] :
                val["name"] = self.name
                val["id"] = self.id
                val["age"] = self.age
                val["email"] = self.email
                val["phone"] = self.phone_no
                val["enroll_date"] = self.enroll_date
                return f"Data of {self.name} was updated!"
        else:
            self.dit["name"] = self.name
            self.dit["id"] = self.id
            self.dit["age"] = self.age
            self.dit["email"] = self.email
            self.dit["phone"] = self.phone_no
            self.dit["enroll_date"] = self.enroll_date
            lst.append(self.dit)
            return f"New student {self.name} was added!"

class student_name_remove:
    def __init__(self,name):
        self.name = name 
    def remove(self):
        for val in lst:
            if self.name == val["name"] :
                lst.remove(val)
                return f"{self.name} was removed!"
        else:
            return f"{self.name} wasn't found!"

class student_data_view:
    def __init__(self,id):
        self.id = id
    def view(self) :
        for val in lst:
            if self.id == val["id"] :
                return f"Name = {val['name']}\nAge = {val['age']}\nEmail = {val['email']}\nPhone number = {val['phone']}\nDate of enroll = {val['enroll_date']}\n"
        else:
            return f"ID wasn't found!"

class student_data_update:
    def __init__(self,name,change,value):
        self.change = change
        self.name = name
        self.value = value
    def update(self):
        for val in lst:
            if self.name == val["name"] :
                val[self.change] = self.value
            return f"Data was updated!"
        else:
            return f"Student wasn't found!"
#Student management system ends

#-------------------------------------------------------------------------------------------------------------

#subject management system starts

class subject_add:
    def __init__(self,name,mark,id):
        self.mark = mark
        self.name = name
        self.id = id 
    def add(self):
        self.dit = {}
        for val in lst1:
            if self.name == val["name"] :
                val["name"] = self.name
                val["mark"] = self.mark
                val["id"] = self.id
                return f"{val['name']} was updated1"
        else:
            self.dit["name"] = self.name
            self.dit["mark"] = self.mark
            self.dit["id"] = self.id
            lst1.append(self.dit)
            return f"{self.name} was added!"

class subject_remove:
    def __init__(self,name):
        self.name = name
    def remove(self):
        for val in lst:
            if self.name == val["name"] :
                lst1.remove(val)
        else:
            return f"{self.name} wasn't found!"

class subject_update :
    def __init__(self,name,change,data):
        self.name = name
        self.change = change
        self.data = data
    def update(self):
        for val in lst1:
            if self.name == val["name"] :
                val[self.change] = self.data
            return f"{self.name} was updated!"
        else:
            return f"{self.name} was not found!"

class subject_view:
    def __init__(self,name):
        self.name = name
    def view(self):
        for val in lst1:
            if self.name == val["name"] :
                return f"Name = {val['name']}\nFull Mark = {val['mark']}\nID = {val['id']}\n"
        else:
            return f"{self.name} wasn't found!"


# subject management system ends 



print("student management/subject management/examination and marks/attendence management/academic report")
answer1 = input("Which you want to access?").lower().strip().replace(" ","")


if answer1 == "studentmanagement" :
    register1= input("Do you want to register the student or remove?(register/remove/none)").lower()
    if register1 == "register" :
        register = "y"
        while register == "y":
            character = string.ascii_letters + string.digits
            name = input("Enter student name").lower()
            id = secrets.choice(character)
            age = int(input("Enter the age"))
            email = input("Enter email of student").lower()
            phone = int(input("Enter the phone number"))
            enroll_date = input("Enter the enrollment date")
            student_register = student_name_register(name,id,age,email,phone,enroll_date)
            print(student_register.register())
            register = input("Do you want to add more?(y/n)").lower()
    elif register1 == "remove":
        remove = "y"
        while remove == "y" :
            name = input("Enter the student name that you want to remove :").lower()
            student_remove = student_name_remove(name)
            print(student_remove.remove())
            remove = input("Do you want to remove more?(y/n)").lower()

    elif register1 =="none":
        print("None was selected!")


    view = input("Do you want to check a student data?(y/n)").lower()
    while view == "y" :
        name = input("Enter student name").lower()
        for val in lst:
            if name == val["name"] :
                print("Student ID is :",val["id"])
        else:
            print("Student wasn't found!")
        id = input("Enter the ID :")
        student_view = student_data_view(id)
        print(student_view.view())
        view = input("Do you want to check a student data again?(y/n)").lower()


    update = input("Do you want to update the student data(y/n)").lower()
    while update == "y" :
        name = input("Enter student name").lower()
        change = input("What do you want to change?(name,id,age,email,phone_no,enroll_date)").lower()
        if change == "age" or change == "phone_no" :
            new_change = int(input(f"Enter new {change}"))
            student_update = student_data_update(name,change,new_change)
            print(student_update.update())
            update = input("Do you want to update the student data again ?(y/n)").lower()
        elif change == "name" or change =="id" or change =="email" or change == "enroll_date" :
            new_change = input(f"Enter new {change}")
            student_update = student_data_update(name,change,new_change)
            print(student_update.update())
            update = input("Do you want to update the student data again ?(y/n)").lower()
elif answer1 == "subjectmanagement" :
    subject1 = input("(add/remove/view/update) subjects in the academic curriculum?").lower()

    if subject1 == "add":
        while subject1 == "add" :
            name = input("Enter the subject name").lower()
            max_mark = int(input("Enter the full mark of this subject"))
            character = string.ascii_letters + string.digits
            id = secrets.choice(character)
            sub_add = subject_add(name,max_mark,id)
            print(sub_add.add())
            add2 = input("Do you want to add more subjects?(y/n)").lower()
            if add2 == "y":
                subject1 = "add"
            else:
                subject1 = "no"


    elif subject1 == "remove" :
        while subject1 == "remove":
            name = input("Enter the subject name").lower()
            sub_remove = subject_remove(name)
            print(sub_remove.remove())
            remove1 = input("Do you want to remove other subjects also?(y/n)").lower()
            if remove1 == "y":
                subject1 = "remove"
            else:
                subject1 = "no"

    elif subject1 == "update":
        while subject1 == "update" :
            change = input("what do you want to update?(name/mark/id)").lower()
            name = input("what is the name of subject you want to change").lower()
            if change == "mark" :
                value = int(input("Enter new mark :"))
            elif change == "name" or change == "id" :
                value = input(f"Enter new {change}")
            sub_update = subject_update(name,change,value)
            print(sub_update.update())
            update2 = input("Do you want to update again?(y/n)").lower()
            if update2 == "y" :
                subject1 = "update"

            else:
                subject1 = "no"
    elif subject1 == "view" :
        while subject1 == "view" :
            name = input("Enter the name of the subject").lower()
            sub_view = subject_view(name)
            print(sub_view.view())
            view1 = input("Do you want to view other subjects also?(y/n)").lower()
            if view1 == "y" :
                subject1 = "view"

            else:
                subject1 = "no"