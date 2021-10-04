
# Assignment No: 1
# Problem Statement: Student Database Management
# Roll No: 3460






# Write a Python program to create a Student Database  using any Data Sequences

class Student:
    database={}

    def addRecord(self):
        try:
            roll=int(input("Enter the roll no"))
            if(self.database.get(roll) is None):
                firstname=input("Enter the first name")
                lastname=input("Enter the lastname")
                self.database[roll]={'firstname':firstname,'lastname':lastname}
            else:
                print("Record already exists")
        except:
            print("Provide proper values")

    def displayAllRecords(self):
        print("----------------")
        print('Roll No    FirstName   LastName ')
        for i in self.database:
            print(i,'       ',self.database[i]['firstname'],'   ',self.database[i]['lastname'])
        print("----------------")
        

    def displayRecord(self):
        try:
            roll=int(input("Enter roll no for displaying particular record"))
            print("----------------")
            print('Roll No    FirstName   LastName ')
            print(roll,'       ',self.database[roll]['firstname'],'   ',self.database[roll]['lastname'])
            print("----------------")

        except:
            print("No such record")

    def deleteRecord(self):

        try:
            roll=int(input("Enter roll no for deleting particular record"))
            del self.database[roll]
            print("Successfully deleted the record")
        except:
            print("No such record")

    def updateRecord(self):

        try:
            roll=int(input("Enter roll no for updating a particular record"))
            fname=input("Enter firstname")
            lname=input("Enter lastname")
            self.database[roll]={'firstname':fname,'lastname':lname}
            print("Updated successfully")
        except:
            print("No such record")


y=True
while(y):
    print("1.Add a record\n2.Display all records\n3.Display a particular record\n4.Delete a record\n5.Update a record\n6.Exit")
    ch=int(input("Enter your choice"))
    s1=Student()
    if(ch==1):
        s1.addRecord()
    elif(ch==2):
        s1.displayAllRecords()
    elif(ch==3):
        s1.displayRecord()
    elif(ch==4):
        s1.deleteRecord()
    elif(ch==5):
        s1.updateRecord()
    elif(ch==6):
        break



# output:
# 1.Add a record
# 2.Display all records        
# 3.Display a particular record
# 4.Delete a record
# 5.Update a record
# 6.Exit
# Enter your choice1
# Enter the roll no1101
# Enter the first nameSrushti
# Enter the lastnameSulgudle
# 1.Add a record
# 2.Display all records        
# 3.Display a particular record
# 4.Delete a record
# 5.Update a record
# 6.Exit
# Enter your choice1
# Enter the roll no1102
# Enter the first nameShruti
# Enter the lastnamePatil
# 1.Add a record
# 2.Display all records
# 3.Display a particular record
# 4.Delete a record
# 5.Update a record
# 6.Exit
# Enter your choice1
# Enter the roll no1103
# Enter the first nameHarsh 
# Enter the lastnameTidke
# 1.Add a record
# 2.Display all records
# 3.Display a particular record
# 4.Delete a record
# 5.Update a record
# 6.Exit
# Enter your choice1
# Enter the roll no1104
# Enter the first namePrashant
# Enter the lastnamePatil
# 1.Add a record
# 2.Display all records
# 3.Display a particular record
# 4.Delete a record
# 5.Update a record
# 6.Exit
# Enter your choice1
# Enter the roll no1101
# Record already exists
# 1.Add a record
# 2.Display all records
# 3.Display a particular record
# 4.Delete a record
# 5.Update a record
# 6.Exit
# Enter your choice2
# ----------------
# Roll No    FirstName   LastName
# 1101         Srushti     Sulgudle
# 1102         Shruti     Patil
# 1103         Harsh     Tidke
# 1104         Prashant     Patil
# ----------------
# 1.Add a record
# 2.Display all records
# 3.Display a particular record
# 4.Delete a record
# 5.Update a record
# 6.Exit
# Enter your choice3
# Enter roll no for displaying particular record1103
# ----------------
# Roll No    FirstName   LastName
# 1103         Harsh     Tidke
# ----------------
# 1.Add a record
# 2.Display all records
# 3.Display a particular record
# 4.Delete a record
# 5.Update a record
# 6.Exit
# Enter your choice4
# Enter roll no for deleting particular record1103
# Successfully deleted the record
# 1.Add a record
# 2.Display all records
# 3.Display a particular record
# 4.Delete a record
# 5.Update a record
# 6.Exit
# Enter your choice2
# ----------------
# Roll No    FirstName   LastName
# 1101         Srushti     Sulgudle
# 1102         Shruti     Patil
# 1104         Prashant     Patil
# ----------------
# 1.Add a record
# 2.Display all records
# 3.Display a particular record
# 4.Delete a record
# 5.Update a record
# 6.Exit
# Enter your choice5
# Enter roll no for updating a particular record1102
# Enter firstnameShravani
# Enter lastnameDeshmukh
# Updated successfully
# 1.Add a record
# 2.Display all records
# 3.Display a particular record
# 4.Delete a record
# 5.Update a record
# 6.Exit
# Enter your choice2
# ----------------
# Roll No    FirstName   LastName
# 1101         Srushti     Sulgudle
# 1102         Shravani     Deshmukh
# 1104         Prashant     Patil
# ----------------
# 1.Add a record
# 2.Display all records
# 3.Display a particular record
# 4.Delete a record
# 5.Update a record
# 6.Exit
# Enter your choice6



# --------- Extra ----------
# Write a Python Program to Accept n numbers from users and display average, sum
# of these numbers 

n=int(input("How many numbers you want to add"))
list=[]
for i in range(0,n):
    list.append(int(input()))
sum=0
for i in range(0,n):
    sum=sum+list[i]
print("Sum is : ",sum, " Average is : ",sum/n)

# Output:
# How many numbers you want to add2
# 12
# 23
# Sum is :  35  Average is :  17.5