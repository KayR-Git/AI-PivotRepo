from datetime import date
from dataclasses import dataclass
@dataclass
class Employee:
    name: str
    hire_date: date

    def tenure_years(self):
        return (date.today() - self.hire_date).days//365