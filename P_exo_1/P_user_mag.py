employeeID = 0
employeeName = ""
employeeAge = 0
employeeSalary = 0.0
employeeBonus = 0.0
yearsOfExperience = 0
employeePhoneNumber = 0
status = ""
CH = 0
A = 0


def main():
    global A
    A = 1

    while A == 1:
        print("---------------------------------")
        print("\t**USER MANAGEMENT**")
        print("---------------------------------")
        print("\n\t1. Create a new user\n\t2. Read the users\n\t3. Exit\n\n\nChoice : ")
        CH = int(input())

        if CH == 1:
            create_user()
            save_user()
        elif CH == 2:
            read_user()
        elif CH == 3:
            print("Exiting the program...")
            return
        else:
            print("Invalid choice /!\\n")

        print("\n\n")
        print("-----------------------------------------------")
        print("**DO YOU WANT TO KEEP USING THE PROGRAMME **")
        print("-----------------------------------------------")
        print("\n\n\t1. YES\n\t2. NO\n\n\nChoice : ")
        A = int(input())

    print("Exiting the program...")


def create_user():
    global status, employeeID, employeeName, employeeAge, employeeSalary, employeeBonus, yearsOfExperience, employeePhoneNumber, CH
    print("\n\n")
    print("---------------------------------")
    print("\tEmployee Details")
    print("---------------------------------")
    print("1. Interne\n2. Externe\n\n\nChoice : ")
    CH = int(input())

    if CH == 1:
        status = "Interne"
    elif CH == 2:
        status = "Externe"
    else:
        print("Invalid choice\n")
        return

    employeeID = int(input("Enter employee ID: "))
    employeeName = input("Enter employee name: ")
    employeeAge = int(input("Enter employee age: "))
    employeeSalary = float(input("Enter employee salary: "))
    employeeBonus = float(input("Enter employee bonus: "))
    yearsOfExperience = int(input("Enter years of experience: "))
    employeePhoneNumber = int(input("Enter employee phone number: "))


def print_user():
    global employeeID, status, employeeName, employeeAge, employeeSalary, employeeBonus, yearsOfExperience, employeePhoneNumber
    print("---------------------------------")
    print("Employee Details")
    print("---------------------------------")
    print("ID: ", employeeID)
    print("Status: ", status)
    print("Name: ", employeeName)
    print("Age: ", employeeAge)
    print("Salary: ", employeeSalary)
    print("Bonus: ", employeeBonus)
    print("Years of Experience: ", yearsOfExperience)
    print("Phone Number: ", employeePhoneNumber)


def save_user():
    global employeeID, status, employeeName, employeeAge, employeeSalary, employeeBonus, yearsOfExperience, employeePhoneNumber
    with open("employee_details.txt", "w") as file:
        file.write("======================================\n")
        file.write("Employee Details :\n")
        file.write("------------------\n")
        file.write("ID: {}\n".format(employeeID))
        file.write("Status: {}\n".format(status))
        file.write("Name: {}\n".format(employeeName))
        file.write("Age: {}\n".format(employeeAge))
        file.write("Salary: {:.2f}\n".format(employeeSalary))
        file.write("Bonus: {:.5f}\n".format(employeeBonus))
        file.write("Years of Experience: {}\n".format(yearsOfExperience))
        file.write("Phone Number: {}\n".format(employeePhoneNumber))
        file.write("======================================\n")

    print("Employee details saved successfully.")


def read_user():
    try:
        with open("employee_details.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Unable to open the file.")


if __name__ == "__main__":
    main()
