# Health-Dataset-EDA-Summary-Statistics-and-Visualizations-Python-


> Exploratory data analysis of a health/lifestyle dataset.  
> Computes descriptive statistics (mean, median, mode, variance, etc.) and produces boxplots for key variables such as Age, Height, Weight, FAF, TUE, FCVC, and NCP.


## Overview
This project performs a concise exploratory data analysis (EDA) on a health/lifestyle dataset.  
It generates:
- **Summary statistics** (mean, median, mode, range, variance, std. dev., coefficient of variation, IQR, MAD)
- **Boxplots** to visualize distributions and outliers

## Dataset
- **File:** `dataset.xlsx`  
- **Columns (examples):** `Age`, `Height`, `Weight`, `FAF`, `TUE`, `FCVC`, `NCP`  
- The data is anonymized and for educational purposes.

## Methods
- Read dataset from Excel
- Clean/prepare numeric columns (drop missing values where required)
- Compute descriptive statistics per variable
- Save results to a plain text file
- Create boxplots and save as PNG

## Results
- **Summary stats:** `summary_stats.txt`  
- **Boxplots:** `boxplot.png`

Example values from `summary_stats.txt`:
- `Age`: mean ≈ 23.0, median = 22, std ≈ 4.38
- `Height`: mean ≈ 1.70 m, std ≈ 0.093
- `Weight`: mean ≈ 86.5 kg, std ≈ 26.1
- `FAF`: mean ≈ 1.01
- `TUE`: mean ≈ 0.66
- `FCVC`: mean ≈ 2.42
- `NCP`: mean ≈ 2.96

## Repository Structure
```
.
├─ dataset.xlsx
├─ boxplot.png
├─ summary_stats.txt
├─ analysis.py
└─ README.md
```

## Requirements
- Python 3.9+
- Packages: `pandas`, `numpy`, `matplotlib`

Install dependencies:
```bash
pip install pandas numpy matplotlib
```

## Usage
```bash
python analysis.py
```
- Outputs:
  - `summary_stats.txt`
  - `boxplot.png`

## License
This project is licensed under the MIT License.
