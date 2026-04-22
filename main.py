def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    role = input("Enter Role: ")
    salary = input("Enter Salary: ")

    file = open("employees.txt", "a")
    file.write(emp_id + "," + name + "," + role + "," + salary + "\n")
    file.close()

    print("Employee Added Successfully")


while True:
    print("\n--- Employee Management System ---")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        print("View feature coming tomorrow")

    elif choice == "3":
        print("Thank You")
        break

    else:
        print("Invalid Choice")