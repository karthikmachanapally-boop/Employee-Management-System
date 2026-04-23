def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    role = input("Enter Role: ")
    salary = input("Enter Salary: ")

    file = open("employees.txt", "a")
    file.write(emp_id + "," + name + "," + role + "," + salary + "\n")
    file.close()

    print("Employee Added Successfully")




def view_employee():
    file = open("employees.txt", "r")
    data = file.readlines()
    file.close()

    if len(data) == 0:
        print("No Employees Found")
        return

    print("\nID      Name           Role              Salary")
    print("-" * 50)

    for line in data:
        line = line.strip()

        if line == "":
            continue

        parts = line.split(",")

        if len(parts) >= 4:
            print(f"{parts[0]:<8}{parts[1]:<15}{parts[2]:<18}{parts[3]:<10}")




def search_employee():
    search_id = input("Enter Employee Id to search : ")


    file = open("employees.txt", "r")
    data = file.readlines()

    found = False

    for line in data:
        parts = line.strip().split(",")

        if parts[0] == search_id:
            print("Employee Found:")
            print(line.strip())
            found = True 
            break 

    if found == False:
        print("Employee Not Found") 

    file.close()





def update_employee():
        update_id = input("Enter Employee Id to update:")
        
        file = open("employees.txt", "r")
        data = file.readlines()
        file.close()

        new_data = []
        found = False 


        for line in data:
            parts = line.strip().split(",")


            if parts[0] == update_id:
                name = input("Enter New Name:")
                role = input("Enter New role:")
                Salary = input("Enter New Salary")

                updated_lines = (update_id + "," + name + "," + role + "," + Salary + "\n")

                new_data.append(updated_lines)

                found = True 

            else: 
                new_data.append(line)


        file = open("employees.txt", "w")
        file .writelines(new_data)
        file .close()

        if found:
            print("updated Sucessfully")
        else:
            print("Employees Not Found")


def delete_employee():
    delete_id = input("Enter Employee ID to Delete: ")
    file  = open("employees.txt", "r")
    data = file.readlines()
    file.close()


    new_data = []
    found = False


    for line in data:
        parts = line.strip().split(",")


        if parts[0] == delete_id:
            found = True 
        else:
            new_data.append(line)


    file = open("employees.txt", "w")
    file. writelines(new_data)
    file. close()


    if found:
        print("Employee Deleted Sucessfully")

    else:
        print("Employee Not found")











while True:
    print("\n--- Employee Management System ---")
    print("1. Add Employee")
    print("2. View Employee")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee   wqw")
    print("6. Exit")
    
    choice = input("Enter Choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
         view_employee()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        update_employee()

    elif choice == "5":
        delete_employee()

    elif choice == "6":
        print("Thank You")
        break

    else:
        print("Invalid Choice")