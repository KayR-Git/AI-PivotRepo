from datetime import date
from dataclasses import dataclass
# @dataclass

class Employee:
    # def __init__(self, name, hire_date):
    #     self.name = name
    #     self.hire_date = hire_date
    name: str
    hire_date: date

    def tenure_years(self):
        return (date.today() - self.hire_date).days//365

emp = Employee("Kay", date(2020,1,1))
print(emp.tenure_years())
print(emp)