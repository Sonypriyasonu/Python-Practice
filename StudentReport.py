'''
Student Grade Tracker: Create a console-based application for tracking student grades
 
The application should allow users to perform various operations such as adding students, 
assigning grades to them, calculating averages, and generating reports. 
Below are the detailed requirements for the application.
 
Add Students: Users should be able to add students to the system by providing their names.
Ensure that duplicate student names are not allowed, and appropriate feedback is provided to the user.
 
Assign Grades: Once students are added, users should be able to assign grades to them. 
Each grade should be associated with a specific student. Grades can be floating-point numbers 
representing scores achieved by students in their assessments.
 
Calculate Averages: The application should calculate the average grade for each student 
based on the grades assigned to them. If a student has no grades assigned, their average 
should be considered as 0.
 
Generate Reports: Users should have the option to generate a report that displays the 
names of all students along with their corresponding average grades. '''

global student, grade,r,report
student={}
grade={}
report={}
r=1

def addstudent():
    global student, grade,r,report
    s=input("Enter student name: ")
    if s.lower() in student.values():
        print("Name is already existed")
        return 0
    else:
        student[r]=s.lower()
        print("Successfully added!")
        r=r+1
        return r-1
        #addgrade()
        
def addgrade(a):
    global student, grade,r,report
    g={"DSA":0,"CNN":0,"DBMS":0,"OP":0,"M3":0}

    for i in g:
        while True:
            try:
                n=float(input("Enter "+i+" marks :"))
                if 0<=n<=100:
                    break
                else:
                    print("Invalid input \n\nPlease enter again")
            except ValueError:
                print("Invalid input. Please enter a number")
        g[i]=n
    grade[a]=g
    print("Grades added successfully!")
        
        
def cal_avg(a):
    global grade,report
    d=grade[a]
    avg=sum(d.values())/len(d)
    report[a]=avg
        
def find_avg(a):
    global report,student
    if a in report:
        print(f"Average grade for {student[a]}: {report[a]}")
    else:
        print("Student not found or grades not calculated.\n")       
            
def studentreport():
    global student, grade,r,report
    while True:
        print("Enter 1 if you want to add student and add grade")
        print("Enter 2 to find average grade of a student")
        print("Enter 3 if you want report of students")
        print("Enter any number to exit")
        n=int(input())
        if n==1:
            a=addstudent()
            if(a!=0):
                addgrade(a)
                cal_avg(a)
        elif n==2:
            a=int(input("Enter student roll number: "))
            find_avg(a)
        elif n==3:
            #print(student)
            #print()
            #print(grade)
            #print()
            #print(report)
            for i in report:
                print(student[i]," : ",report[i])
        else:
            print("Exited")
            break
        
studentreport()
