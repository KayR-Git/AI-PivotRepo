from datetime import date
from pathlib import Path
import json

from hr.models import Employee
from hr.reporting import tenure_years

from hr.store import load_employees, save_employees

if __name__ == '__main__':
    path = Path("data/employees.json")

    try:
        employees = load_employees(path)
    except FileNotFoundError:
        print(f"{path} not found")
        employees =[]
    except json.JSONDecodeError:
        print(f"{path} is corrupt")
        employees =[]

    for emp in employees:
        print(tenure_years(emp))

    employees.append(Employee("Sam", date(2013, 1, 15)))
    save_employees(path, employees)
    print(f"Saved {len(employees)} employees to {path}")