# DataFlow Inc. - Medallion Architecture Project

## Overview

This project demonstrates a simple Data Engineering pipeline using the Medallion Architecture (Bronze, Silver, and Gold layers). The raw Olist e-commerce dataset is processed using Python, Pandas, SQL, and PySpark.

## Technologies Used

- Python
- Pandas
- SQL
- PySpark
- Delta Lake
- Parquet

## Project Structure

```
Data-Flow-Inc/
│
├── data/
├── scripts/
├── spark/
├── sql/
├── run_pipeline.py
├── requirements.txt
└── README.md
```

## Medallion Architecture

### Bronze Layer
- Reads raw CSV files
- Converts CSV files to Parquet format

### Silver Layer
- Removes duplicate records
- Handles missing values
- Standardizes column names
- Performs schema validation
- Generates a data quality report

### Gold Layer
- Joins multiple datasets
- Creates business-ready datasets
- Generates sales summaries and reports

## How to Run

1. Install the required packages

```bash
pip install -r requirements.txt
```

2. Place all dataset CSV files inside:

```
data/raw/
```

3. Run the complete pipeline

```bash
python run_pipeline.py
```

## Dataset

The project uses the given **Kaggle E-commerce (Olist)** dataset.

One of the dataset files is **larger than GitHub's 50 MB upload limit**, so the `data` folder has been added to `.gitignore` and is **not included in this repository**.

Download the dataset separately and place the CSV files inside the `data/raw/` folder before running the project.

## Note

While working with the dataset, a few column names/files contained minor spelling inconsistencies. These were handled during preprocessing by standardizing column names before further processing.