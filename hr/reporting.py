from .models import Employee

def tenure_years(emp: Employee) -> str:
    return f"{emp.name} - {emp.tenure_years()} years"