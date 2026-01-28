# User Data ETL Pipeline

A Python-based data pipeline that extracts user data from an external API, transforms and validates it, and loads it into both CSV and SQLite database formats. The pipeline also generates insights from the processed data.

## Project Overview

This project implements a complete Extract-Transform-Load (ETL) workflow that:

- **Extracts** user data from the JSONPlaceholder API
- **Transforms** raw JSON data into a structured DataFrame format
- **Validates** the transformed data for quality and consistency
- **Loads** the cleaned data into CSV and SQLite database
- **Analyzes** the data to generate insights and statistics

## Project Structure

```
PythonAssignment2/
├── main.py                 # Entry point for the ETL pipeline
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── data/
│   ├── raw/              # Raw data from API extraction
│   │   └── users_raw.json
│   └── processed/        # Cleaned and transformed data
│       └── users_clean.csv
├── db/                   # Database storage
│   └── users.db          # SQLite database
├── logs/                 # Pipeline execution logs
│   └── pipeline.log
└── src/                  # Source code modules
    ├── extract.py        # Extract data from API
    ├── transform.py      # Transform and structure data
    ├── validate.py       # Validate data quality
    ├── load_csv.py       # Save to CSV file
    ├── load_sqlite.py    # Load to SQLite database
    └── insights.py       # Generate data insights and statistics
```

## Requirements

- Python 3.7 or higher
- pip (Python package manager)

## Installation

1. Clone or download this repository:
```bash
cd PythonAssignment2
```

2. Install required Python packages:
```bash
pip install -r requirements.txt
```

The following packages will be installed:
- `requests` - For making HTTP requests to the API
- `pandas` - For data manipulation and analysis

## Running the Project

1. Ensure you are in the project directory:
```bash
cd /path/to/PythonAssignment2
```

2. Run the main pipeline script:
```bash
python main.py
```

## Pipeline Stages

### 1. Extract (`src/extract.py`)
Retrieves user data from the JSONPlaceholder API and saves raw JSON to `data/raw/users_raw.json`.

### 2. Transform (`src/transform.py`)
Converts raw JSON data into a structured pandas DataFrame with relevant fields:
- user_id, name, username, email, city, zipcode, company_name

### 3. Validate (`src/validate.py`)
Performs data quality checks and validation on the transformed data.

### 4. Load CSV (`src/load_csv.py`)
Exports the validated data to a CSV file at `data/processed/users_clean.csv`.

### 5. Load SQLite (`src/load_sqlite.py`)
Loads the validated data into a SQLite database at `db/users.db`.

### 6. Insights (`src/insights.py`)
Generates statistical insights and analysis from the loaded data, including:
- Total count of valid users
- Users distribution by city
- Data quality metrics
- Additional statistical summaries

## Output Files

After running the pipeline, the following files will be generated:

- `data/raw/users_raw.json` - Raw data from API
- `data/processed/users_clean.csv` - Cleaned and processed data
- `db/users.db` - SQLite database with user records

## License

This project is an assignment-based project. Use and modify as needed for educational purposes.
