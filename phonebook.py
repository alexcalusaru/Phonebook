def Phonebook():
    rows = int(input("Enter the number of contacts: "))
    cols = 3
    phonebook = []
    print(phonebook)
    for i in range(rows):
        print("\nEnter contact number %d details:" %(i+1))
        temp = []
        for j in range(cols):
            if j == 0:
                temp.append(str(input("Enter name: ")))
            if j == 1:
                temp.append(int(input("Enter number: ")))
            if j == 2:
                temp.append(str(input("Enter address: ")))
        phonebook.append(temp)
    print(phonebook)
    return phonebook

def Choice():
    print("Managing operations performed on a phonebook")
    print("Choose what you want to do\n")
    print("1. Add a new user")
    print("2. Delete a user")
    print("3. Search a user by name and address")
    print("4. Display contacts")
    choice = int(input("Enter your choice: "))
    return choice

def Add(user):
    dip = []
    for i in range(len(user[0])):
        if i == 0:
            dip.append(str(input("Enter name: ")))
        if i == 1:
            dip.append(int(input("Enter number: ")))
        if i ==2:
            dip.append(str(input("Enter address: ")))
    user.append(dip)
    return user

def Delete(user):
    contact = str(input("Enter the contact you want to delete: "))
    temp = 0
    for i in range(len(user)):
        if contact == user[i][0]:
            temp = temp + 1
            print(user.pop(i))
            print("Contact removed")
            return user
    if temp == 0:
        print("Invalid name")
        return user

def Search(user):
    choice = int(input("\nEnter search criteria\n 1. Name\n 2. Address\n"))
    temp = []
    check = -1
    if choice == 1:
        contact = str(input("Enter the name of the contact you want to search: "))
        for i in range(len(user)):
            if contact == user[i][0]:
                check = i
                temp.append(user[i])
    elif choice == 2:
        contact = str(input("Enter the address of the contact you want to search: "))
        for i in range(len(user)):
            if contact == user[i][2]:
                check = i
                temp.append(user[i])
    if check == -1:
        return -1
    else:
        Display(temp)
        return check

def Display(user):
    if not user:
        print("List is empty")
    else:
        for i in range(len(user)):
            print(user[i])


ch = 1
user = Phonebook()
while ch in (1, 2, 3, 4):
    ch = Choice()
    if ch == 1:
        user = Add(user)
    elif ch == 2:
        user = Delete(user)
    elif ch == 3:
        d = Search(user)
        if d == -1:
            print("The contact doesn't exsit")
    elif ch == 4:
        Display(user)
        










