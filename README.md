# hrsummary

# Readme is to check what my project does.
```
Command-line tool that summarizes an employee.csv: headcount by department plus average tenure.
```

## Setup
```
git clone https://github.com/KayR-Git/AI-PivotRepo
cd Ai-PivotRepo
python -m venv .venv
.venv\Scripts\activate
```

## Usage
```
python hrsummary.py data/employees.csv
```

## CSV format
```
name,department,hire_date
Kay,Engineering,1990-01-01
```

## Example output
```
Department HeadCount
Engineering: 3
Sales: 2
Pharmacy: 1
Average Tenure: 15.3 years
```
