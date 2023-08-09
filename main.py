from employee import Employee
# Example usage
salary = 50000
commission = 2000  # Replace this with the actual commission based on bugs fixed
employee1 = Employee(salary,commission)
total_sal = employee1.total_salary()
tax_amount = employee1.calculate_tax()

print(f"Total Salary: {total_sal}")
print(f"Tax Amount: {tax_amount}")