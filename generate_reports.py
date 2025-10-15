import os

# Function to read file content
def read_file(filepath):
    if not os.path.exists(filepath):
        return f"Error: Report file not found at {filepath}"
    with open(filepath, "r") as f:
        return f.read()

# Read reports
coverage_report = read_file("coverage_report.txt")
pylint_report = read_file("pylint_report.txt")

# Create the content for REPORTS.md
reports_content = f"""# Automated Reports
## Coverage Report
```text
{coverage_report}
```
## Pylint Report
```text
{pylint_report}
```
"""
# Write to REPORTS.md
with open("REPORTS.md", "w") as f:
    f.write(reports_content)
