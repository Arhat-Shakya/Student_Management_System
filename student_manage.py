import json
import string
import secrets
import os

if os.path.exists("student.json") and os.path.getsize("student.json") > 0 :
    with open("student.json","r") as f:
        lst_student = json.load(f)
        if lst_student != "":
            lst = lst_student
else:
    lst=[]                    

if os.path.exists("subject.json") and os.path.getsize("subject.json") > 0 :
    with open("subject.json","r") as f:
        lst_subject = json.load(f)
        if lst_subject != "":
            lst1 = lst_subject
else:
    lst1=[]

if os.path.exists("exam.json") and os.path.getsize("exam.json") > 0 :
    with open("exam.json","r") as f:
        lst_examination = json.load(f)
        if lst_examination != "":
            lst2 = lst_examination
else:
    lst2=[]

if os.path.exists("attendence.json") and os.path.getsize("attendence.json") > 0 :
    with open("attendence.json","r") as f:
        lst_attend = json.load(f)
        if lst_attend != "":
            lst3 = lst_attend
else:
    lst3=[]


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
        for val in lst1:
            if self.name == val["name"] :
                lst1.remove(val)
                return f"{self.name} was removed!"
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

#---------------------------------------------------------------------------------------------------------------------

#examination management system starts

class exam_add:
    def __init__(self,dit):
        self.dit = dit
    def add(self):
        self.dit1 = {}
        self.percent = 0
        self.sum1 = 0
        self.mark = 0
        self.dit1["name"] = self.dit["name"]
        for val in lst2 :
            if self.dit["name"] == val["name"] :
                return f"student marks are already there!"
        else:
            for val in lst1:
                self.dit1[val['name']] = self.dit[val['name']]
                self.sum1 += self.dit[val["name"]]
                self.mark += val["mark"]
            self.percent = (self.sum1/(self.mark))*100
            if self.percent >= 90 :
                self.grade = "A+"
            elif self.percent>=80 :
                self.grade = "A"
            elif self.percent >=70 :
                self.grade = "B+"
            elif self.percent >= 60 :
                self.grade = "B"
            elif self.percent >= 50 :
                self.grade ="C+"
            elif self.percent >=40 :
                self.grade = "C"
            else:
                self.grade = "Fail"
            self.dit1["total"] = self.sum1
            self.dit1["percentage"] = self.percent
            self.dit1["grade"] = self.grade
            lst2.append(self.dit1)
            return f"new marks are added in {self.dit['name']}"

class exam_remove :
    def __init__(self,name):
        self.name = name
    def remove(self):
        for val in lst2:
            if self.name == val["name"] :
                lst2.remove(val)
                return f"student removed!"
        else:
            return f"Student not found!"

class exam_view:
    def __init__(self,name):
        self.name = name
    def view(self):
        for val in lst2:
            if self.name == val["name"] :
                return val
        else:
            return f"Student not found!"

class exam_update:
    def __init__(self,name,subject,mark):
        self.subject= subject
        self.mark = mark
        self.name = name
    def update(self):
        for val in lst2:
            if val["name"] == self.name:
                if self.subject not in [subject["name"] for subject in lst1]:
                    return "Subject not found!"
                val[self.subject] = self.mark
                for subject in lst1:
                    if subject["name"] != self.subject and subject["name"] not in val:
                        return "Marks not entered for all subjects!"
                total = 0
                for subject in lst1:
                    total += val[subject["name"]]
                val["total"] = total
                total_full_marks = 0
                for subject in lst1:
                    total_full_marks += subject["mark"]
                if total_full_marks == 0:
                    return "No subjects registered!"
                percentage = (total / total_full_marks) * 100
                val["percentage"] = percentage
                if percentage >= 90:
                    grade = "A+"
                elif percentage >= 80:
                    grade = "A"
                elif percentage >= 70:
                    grade = "B+"
                elif percentage >= 60:
                    grade = "B"
                elif percentage >= 50:
                    grade = "C+"
                elif percentage >= 40:
                    grade = "C"
                else:
                    grade = "Fail"
                val["grade"] = grade
                return "Examination record updated successfully!"
        return "Student examination record not found!"

#examination management system ends


#attendence management starts here

class attendence_take:
    def __init__(self,dit):
        self.dit = dit
    def take(self) :
        lst3.append(self.dit)
        return f"Todays attendence was added!"

class attendence_remove:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
    def remove(self):
        for val in lst3:
            if self.year == val["year"] and self.month == val["month"] and self.day == val["day"] :
                lst3.remove(val)
                return f"Attendence removed!"
        else:
            return f"attendence not found!"

class attendence_view:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
    def view(self):
        for val in lst3:
            if self.year == val["year"] and self.month == val["month"] and self.day == val["day"] :
                return val
        else:
            return f"attendence not found!"

class attendence_update:
    def __init__(self,year,month,day,name,attend):
        self.year = year
        self.month = month
        self.day = day
        self.attend = attend
        self.name = name
    def update(self):
        for val in lst3:
            if self.year == val["year"] and self.month == val["month"] and self.day == val["day"] :
                val[self.name] = self.attend
                if self.attend == "p":
                    val["total present today "] += 1
                    val["total present today "] -= 1
                else:
                    val["total present today "] += 1
                    val["total present today "] -= 1                  
                return f"updated!"
        else:
            return f"attendence not found!"


#attendence management ends here


#Academic Performance & Reports starts here

class academic_performance_check:
    def __init__(self,lst):
        self.lst = lst
    def check(self):
        self.lst_report = []
        for val in self.lst:
            self.lst_report.append((val["name"],val["percentage"]))
        self.lst_report = sorted(self.lst_report, key=lambda x:x[1], reverse= True)
        i = 1
        for val in self.lst_report:
            print(f"{i}. {val[0]} : {val[1]}\n")
            i += 1

class attendence_percentage:
    def __init__(self,lst_student,lst_attend):
        self.lst_student = lst_student
        self.lst_attend = lst_attend
    def percent(self):
        self.present = []
        for val_attend in self.lst_attend:
            i = 0
            for val in self.lst_student:
                if len(self.present) != len(self.lst_student):
                    if val_attend[val["name"]] == "p":
                        self.present.append(1)
                    else:
                        self.present.append(0)
                else:
                    if val_attend[val["name"]] == "p":
                        self.present[i] += 1
                i += 1
        print("Present percentage of each student :")
        j = 0
        if len(self.present) != 0 :
            for val_student in self.lst_student:
                self.percentage = (self.present[j]/len(self.lst_attend))*100
                print(f"{val_student['name']} : {self.percentage}\n")
                j += 1
        else:
            print("No attendence taken at all !")



#Academic Performance & Reports ends here



print("student management/subject management/examination and mark/attendence management/academic report")
answer1 = input("Which you want to access?").lower().strip().replace(" ","")

#student management system ---------------------------------------------------------------------------------------
if answer1 == "studentmanagement" :
    register1= input("Please select (register/remove/update/view)").lower()

    if register1 == "register" :
        register = "y"
        while register == "y":
            character = string.ascii_letters + string.digits
            name = input("Enter student name").lower()
            id = ""
            for _ in range(8):
                id += secrets.choice(character)
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



    elif register1 == "view" :
        view ="y" 
        while view == "y" :
            name = input("Enter student name").lower()
            for val in lst:
                if name == val["name"] :
                    print("Student ID is :",val["id"])
                    break
            else:
                print("Student wasn't found!")
            id = input("Enter the ID :")
            student_view = student_data_view(id)
            print(student_view.view())
            view = input("Do you want to check a student data again?(y/n)").lower()


    elif register1 == "update" :
        update = "y"
        while update == "y" :
            name = input("Enter student name").lower()
            change = input("What do you want to change?(name,id,age,email,phone,enroll_date)").lower()
            if change == "age" or change == "phone" :
                new_change = int(input(f"Enter new {change}"))
                student_update = student_data_update(name,change,new_change)
                print(student_update.update())
                update = input("Do you want to update the student data again ?(y/n)").lower()
            elif change == "name" or change =="id" or change =="email" or change == "enroll_date" :
                new_change = input(f"Enter new {change}")
                student_update = student_data_update(name,change,new_change)
                print(student_update.update())
                update = input("Do you want to update the student data again ?(y/n)").lower()
    elif register1 =="none":
        print("None was selected!")



#subject management -------------------------------------------------------------------------------------------------------------

elif answer1 == "subjectmanagement" :
    subject1 = input("(add/remove/view/update) subjects in the academic curriculum?").lower()

    if subject1 == "add":
        while subject1 == "add" :
            name = input("Enter the subject name").lower()
            max_mark = int(input("Enter the full mark of this subject"))
            character = string.ascii_letters + string.digits
            id = ""
            for _ in range(5) :
                id += secrets.choice(character)
            sub_add = subject_add(name,max_mark,id)
            print(sub_add.add())
            subject1 = input("Do you want to add more subjects?(add/n0)").lower()
            


    elif subject1 == "remove" :
        while subject1 == "remove":
            name = input("Enter the subject name").lower()
            sub_remove = subject_remove(name)
            print(sub_remove.remove())
            subject1 = input("Do you want to remove other subjects also?(remove/no)").lower()
            

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
            subject1 = input("Do you want to update again?(update/no)").lower()

            
    elif subject1 == "view" :
        while subject1 == "view" :
            name = input("Enter the name of the subject").lower()
            sub_view = subject_view(name)
            print(sub_view.view())
            subject1 = input("Do you want to view other subjects also?(view/no)").lower()


#examination management system --------------------------------------------------------------------------------
elif answer1 == "examinationandmark" :
    exam1 = input("Do you want to add/remove/update/view the mark?").lower()

    if exam1 == "add" :
        while exam1 == "add" :
            dit = {}
            ans = 0
            name = input("Enter the name of the student :").lower()
            dit["name"] = name
            for val in lst1 : 
                mark = int(input(f"Enter the mark for {val['name']}"))
                if mark <= val["mark"] :
                    dit[val["name"]] = mark
                    ans = 12345
                else:
                    print("Mark that you entered was more than full mark try again please!")
                    ans = 0 
                    break
            if ans == 12345 :
                e_add = exam_add(dit)
                print(e_add.add())
            exam1 = input("Do you want to add more student marks?(add/no)").lower()

    elif exam1 == "remove" :
        while exam1 == "remove" :
            name = input("Enter the name of the student :").lower()
            r_exam = exam_remove(name)
            print(r_exam.remove())
            exam1 = input("Do you want to remove more ? (remove/no)").lower()

    elif exam1 == "view" :
        while exam1 == "view" :
            name = input("Enter the name of the student :").lower()
            v_exam = exam_view(name)
            print(v_exam.view())
            exam1 = input("Do you want to view more students(view/no)").lower()

    elif exam1 == "update":
        while exam1 == "update":
            name = input("Enter the name of the student :").lower()
            lst_update = []
            for val in lst1:
                lst_update.append(val["name"])
            print("which subject do you want to update :",lst_update)
            update1 = input("Enter the name of the subject :")
            mark1 = int(input("Enter the updated mark of the subject :"))
            for val in lst1:
                if update1 == val["name"] :
                    if mark1 <= val["mark"] :
                        up_exam = exam_update(name,update1,mark1)
                        print(up_exam.update())
                        break
                    else:
                        print("Mark was over the full mark try again please")
                        break
            else:
                print("subject not found!")
                break
            exam1 = input("Do you want to update any other too?(update/no)").lower()


#attendence management system ----------------------------------------------------------------------------


elif answer1 == "attendencemanagement" :
    attend = input("do you want to (take/remove/update/view) the attendence").lower()

    if attend == "take" :
        while attend == "take" :
            dit = {}
            year = int(input("Enter the year :"))
            month = input("Enter the month :").lower()
            day = int(input("Enter number day of the month:"))
            present = 0
            absent = 0
            dit["year"] = year
            dit["month"] = month
            dit["day"] = day
            for val in lst:
                attendence = input(f"{val['name']} present or absent (p/a) :").lower()
                dit[val["name"]] = attendence
                if attendence == "p" :
                    present += 1
                elif attendence == "a" :
                    absent += 1
            dit["total present today "] = present
            dit["total absent today "] = absent
            attend_take = attendence_take(dit)
            print(attend_take.take())
            attend = input("Do you want to take more attendence?(take/no)").lower()


    elif attend == "remove" :
        while attend == "remove" :
            year = int(input("Enter the year of which you want to remove :"))
            month = input("Enter the month :").lower()
            day = int(input("Enter the day :"))
            attend_remove = attendence_remove(year,month,day)
            print(attend_remove.remove())
            attend = input("Do you want to remove more?(remove/no)").lower()


    elif attend == "view" :
        while attend == "view" :
            year = int(input("Enter the year of which you want to view :"))
            month = input("Enter the month :").lower()
            day = int(input("Enter the day :"))
            attend_view = attendence_view(year,month,day)
            print(attend_view.view())
            attend = input("Do you want to view more?(view/no)").lower()

    elif attend == "update" :
        while attend == "update" :
            year = int(input("Enter the year of which you want to update :"))
            month = input("Enter the month :").lower()
            day = int(input("Enter the day :"))
            name = input("Enter the name of the student").lower()
            attendence = input("Present or adsent (p/a) :")
            attend_update = attendence_update(year,month,day,name,attendence)
            print(attend_update.update())
            attend = input("Do you want to update more?(update/no)")


#Academic Performance & Reports -------------------------------------------------------------------------------------------

elif answer1 == "academicreport" :
    report1 = input("Do you want to check (class ranking/attendence percentage)").lower().strip().replace(" ","")

    if report1 == "classranking" :
        perform = academic_performance_check(lst2)
        perform.check()


    elif report1 == "attendencepercentage" :
        attend_percent = attendence_percentage(lst,lst3)
        attend_percent.percent()




#data write into the json file ------------------------------------------------------------------

with open("student.json","w") as f:
    json.dump(lst,f,indent=4)

with open("subject.json","w") as f:
    json.dump(lst1,f,indent=4)

with open("exam.json","w") as f:
    json.dump(lst2,f,indent=4)

with open("attendence.json","w") as f:
    json.dump(lst3,f,indent=4)