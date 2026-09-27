from datetime import date
from pathlib import Path
import json
from .models import Employee

def load_employees(path: Path) -> list[Employee]:
    data = json.loads(path.read_text())
    return[Employee(name=r["name"], hire_date=date.fromisoformat(r["hire_date"])) for r in data]

def save_employees(path: Path, employees: list[Employee]) -> None: 
    data = [{"name":e.name, "hire_date": e.hire_date.isoformat()} for e in employees]
    path.write_text(json.dumps(data, indent=2))