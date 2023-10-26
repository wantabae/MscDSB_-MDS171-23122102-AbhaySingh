listnames=[]
def storename(name):
    name=name.strip().title()
    if name in listnames:
        return False
    else:
        listnames.append(name)
        return True

def printnames():
    print("-"*30)
    for name in listnames:
        print(name)
    print("-"*30)

def searchname(name):
    name=name.strip().title()
    flag=False
    for item in listnames:
        if name==item:
            flag=True
            break
    if flag==True:
        print("name found")
    else:
        print("name not found")

while True:
    print("menu options")
    print("*"*30)
    print("1.enter a name")
    print("2.search for a name")
    print("3.list a name")
    print("4.exit")

    choice=int(input("Enter your choice::"))

    if choice==1:
        userinp=input("enter a name")
        retval=storename(userinp)
        if retval==True:
            print("name added")
        else:
            print("name exists")

    elif choice==2:
        userinp=input("enter the name")
        searchname(userinp)
    elif choice==3:
        printnames()
    elif choice==4:
        exit()
    else:
        print("invalid function")