class Employee:
    def __init__(self, first, last, pay):

        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + "@company.com"

    def fullname(self):
        return '{}{}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('rahul', 'danu', '50000')
emp_2 = Employee('areeba', 'ansari','60000')

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)














