import argparse
from pathlib import Path

from summarize import summarize

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Print a headcount/tenure summary for an employee CSV."
    )
    parser.add_argument("csv_path", type=Path, help="Path to the employee CSV file")
    return parser.parse_args()

def format_report(summary: dict) -> str:
        lines = ["Department HeadCount"]
        for dept, count in summary["headcount_by_department"].items():
             lines.append(f" {dept}: {count}") 
        lines.append(f"Average Tenure: {summary['average_tenure_years']} years")
        return "\n".join(lines)

def main() -> None:
     args = parse_args()
     summary = summarize(args.csv_path)
     print(format_report(summary))

if __name__ == "__main__":
    main()

    
