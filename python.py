# Employee Management Console Application

employees = []


# Add Employee
def add_employee():
    try:
        emp_id = int(input("Enter Employee ID: "))

        # Check if ID already exists
        for emp in employees:
            if emp["Employee ID"] == emp_id:
                print("Employee ID already exists!")
                return

        name = input("Enter Name: ")
        email = input("Enter Email: ")
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))
        experience = float(input("Enter Experience (Years): "))

        employee = {
            "Employee ID": emp_id,
            "Name": name,
            "Email": email,
            "Department": department,
            "Salary": salary,
            "Experience": experience
        }

        employees.append(employee)
        print("Employee added successfully!")

    except ValueError:
        print("Invalid input! Please enter correct data types.")


# View All Employees
def view_employees():
    if not employees:
        print("No employee records found.")
        return

    print("\n----- Employee Records -----")
    for emp in employees:
        print(f"""
Employee ID : {emp['Employee ID']}
Name        : {emp['Name']}
Email       : {emp['Email']}
Department  : {emp['Department']}
Salary      : {emp['Salary']}
Experience  : {emp['Experience']} Years
------------------------------
""")


# Search Employee by ID
def search_employee():
    try:
        emp_id = int(input("Enter Employee ID to search: "))

        for emp in employees:
            if emp["Employee ID"] == emp_id:
                print("\nEmployee Found:")
                print(emp)
                return

        print("Employee not found!")

    except ValueError:
        print("Invalid Employee ID!")


# Update Employee Details
def update_employee():
    try:
        emp_id = int(input("Enter Employee ID to update: "))

        for emp in employees:
            if emp["Employee ID"] == emp_id:
                print("Leave blank to keep existing value.")

                name = input(f"Name ({emp['Name']}): ")
                email = input(f"Email ({emp['Email']}): ")
                department = input(f"Department ({emp['Department']}): ")
                salary = input(f"Salary ({emp['Salary']}): ")
                experience = input(f"Experience ({emp['Experience']}): ")

                if name:
                    emp["Name"] = name
                if email:
                    emp["Email"] = email
                if department:
                    emp["Department"] = department
                if salary:
                    emp["Salary"] = float(salary)
                if experience:
                    emp["Experience"] = float(experience)

                print("Employee details updated successfully!")
                return

        print("Employee not found!")

    except ValueError:
        print("Invalid input!")


# Delete Employee
def delete_employee():
    try:
        emp_id = int(input("Enter Employee ID to delete: "))

        for emp in employees:
            if emp["Employee ID"] == emp_id:
                employees.remove(emp)
                print("Employee deleted successfully!")
                return

        print("Employee not found!")

    except ValueError:
        print("Invalid Employee ID!")


# Main Menu
def main():
    while True:
        print("\n===== Employee Management System =====")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee by ID")
        print("4. Update Employee Details")
        print("5. Delete Employee")
        print("6. Exit Application")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_employee()

        elif choice == "2":
            view_employees()

        elif choice == "3":
            search_employee()

        elif choice == "4":
            update_employee()

        elif choice == "5":
            delete_employee()

        elif choice == "6":
            print("Exiting Application... Goodbye!")
            break

        else:
            print("Invalid choice! Please select between 1 and 6.")


# Run Program
main()
