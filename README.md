# Basic Data Analyzer

---

## Project Overview
This project implements a **Basic Data Analyzer** in Python that facilitates the exploration and analysis of datasets. The script performs essential exploratory data analysis (EDA), including:
- Summarizing data structure and statistics.
- Visualizing data distributions.
- Generating a correlation heatmap.
- Saving all outputs (plots and reports) for easy reference.

The project was initially designed to analyze a dataset generated randomly for another project. The dataset used is titled **`dataLogisticMap.csv`**, which contains numerical and structured data, making it ideal for testing EDA functionalities.

---

## Features

1. **Data Loading**:
   - Loads datasets from CSV files.
   - Displays basic information about the dataset, including dimensions and column names.

2. **Data Summary**:
   - Provides a detailed summary of the dataset, including:
     - Data types.
     - Non-null value counts.
     - Memory usage.
   - Generates descriptive statistics for numerical columns.

3. **Data Visualization**:
   - **Histogram**: Displays the distribution of a selected column.
   - **Correlation Heatmap**: Shows relationships between numerical columns using a heatmap.

4. **Report and Plot Saving**:
   - Saves a summary report (`data_report.txt`) containing:
     - Data structure overview.
     - Descriptive statistics.
   - Saves plots as PNG files for later use.

---

## Usage Instructions

### 1. Install Dependencies
Ensure you have the required Python libraries installed:
```bash
pip install pandas matplotlib seaborn
```

### 2. Run the Script
Execute the script and provide inputs when prompted:
```bash
python data_analyzer.py
```

### 3. Input Prompts
- **CSV File Path**: Provide the path to the dataset (e.g., `dataLogisticMap.csv`).
- **Output Directory**: Specify the directory to save the report and plots.
- **Column Name**: Choose a column for which to plot a distribution.

### 4. Outputs
- `data_report.txt`: A text file containing a summary of the data.
- `distribution_<column>.png`: A histogram plot for the selected column.
- `correlation_heatmap.png`: A heatmap showing correlations between numerical columns.

---

## File Structure
```
.
├── data_analyzer.py        # Main Python script
├── dataLogisticMap.csv     # Example dataset used for analysis
├── outputs/                # Directory for generated reports and plots
│   ├── data_report.txt
│   ├── distribution_<column>.png
│   └── correlation_heatmap.png
```

---

## Example Dataset: dataLogisticMap.csv
The dataset **`dataLogisticMap.csv`** used in testing contains the following characteristics:
- **Type**: Randomly generated dataset for logistic map simulations or other analytical purposes.
- **Structure**: Multiple columns with numerical values, ideal for correlation analysis and statistical exploration.
- **Example Columns**:
  - `Time`: Represents time steps in the simulation.
  - `Population`: Represents population values in logistic map scenarios.
  - Other numerical variables for further analysis.

---

## Output Example

### 1. Summary Report (data_report.txt):
```
Data Summary:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1000 entries, 0 to 999
Data columns (total 5 columns):
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   Column_1    1000 non-null   int64  
 1   Column_2    980 non-null    float64
 2   Column_3    1000 non-null   object 
 3   Column_4    950 non-null    float64
 4   Column_5    1000 non-null   int64  
dtypes: float64(2), int64(2), object(1)
memory usage: 39.2+ KB

Descriptive Statistics:
          Column_1      Column_2      Column_4      Column_5
count  1000.000000   980.000000   950.000000   1000.000000
mean     50.123456     0.987654     3.123456     25.456789
std      12.345678     0.543210     1.234567      5.678910
min      10.000000     0.123456     1.000000     15.000000
25%      40.000000     0.500000     2.000000     20.000000
50%      50.000000     1.000000     3.000000     25.000000
75%      60.000000     1.500000     4.000000     30.000000
max      90.000000     2.000000     5.000000     35.000000
```

### 2. Plots:
- **Histogram**: `distribution_Population.png`.
- **Heatmap**: `correlation_heatmap.png`.

---

## Potential Applications
- Exploratory data analysis for machine learning or simulation projects.
- Preprocessing datasets for advanced analysis.
- Generating insights and reports for scientific or academic purposes.

---
