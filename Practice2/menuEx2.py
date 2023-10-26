# Create a menu driven program that collects students details
# > Name, Register Number, Email & Phone
# [Use dictionary to store student details]

# Menu Options
# 1. Create Students
# 2. Search for Students
# 3. Print Students

studentDict = {}

def createStudent(name,regno,email,phone):
    student = {
        "Name": name,
        "Email": email,
        "Phone": phone
    }

    studentDict[regno] = student

def colletStudentInfo():
    name = input("Enter Student Name: ")
    regno = input("Enter Student regno: ")
    email = input("Enter Student Email: ")
    phone = input("Enter Student Phone: ")
    return name, regno, email, phone

def printStudents():
    print("Regno\tName\tEmail\tPhone")
    for regno in studentDict.keys():
        print(regno,end="\t")
        for key in studentDict[regno]:
            print(studentDict[regno][key],end='\t')
        print()

while True:
    print("Menu Options")
    print("1. Enter Student Info")
    print("2. List Students")
    print("3. Exit")

    choice = input("Enter the choice").strip()
    if choice == "1":
        name, regno, email, phone = colletStudentInfo()
        createStudent(name, regno, email, phone)
    elif choice == "2":
        printStudents()
    elif choice == "3":
        exit()
    else:
        print("Invalid Choice")
    