employees = {
    "Ravi": 40000,
    "Priya": 50000,
    "Amit": 60000,
    "Neha": 55000
}

highest_paid = max(employees, key=employees.get)

print("Employee with Highest Salary:", highest_paid)
print("Salary:", employees[highest_paid])