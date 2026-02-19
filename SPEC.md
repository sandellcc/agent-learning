Project: CSV Summary Tool (CLI)

Goal:
Build a Python command-line tool that reads a CSV file and prints:

- Total number of rows
- Sum of a numeric column named "value"
- Average of that column
- Top 3 largest values

Usage:
python src/main.py data.csv

Requirements:
- Must handle missing file errors gracefully
- Must handle empty CSV file
- Must raise clear error if column "value" does not exist
- Code must be modular (separate parsing and calculations)
- Must include unit tests for logic

Acceptance Criteria:
- Running with valid CSV prints correct results
- Tests pass with pytest
