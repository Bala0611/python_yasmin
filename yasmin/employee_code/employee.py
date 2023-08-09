class Employee:
    def __init__(self, salary, commission):
        self.salary = salary
        self.commission = commission

    def total_salary(self):
        total_sal = self.salary + self.commission
        return total_sal

    def calculate_tax(self):
        total_sal = self.total_salary()
        if total_sal < 50000:
            tax_percentage = 0
        elif total_sal < 70000:
            tax_percentage = 4
        elif total_sal < 100000:
            tax_percentage = 6.5
        else:
            tax_percentage = 8.5

        tax_amount = (tax_percentage / 100) * total_sal
        return tax_amount
