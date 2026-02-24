# Day 20: Mini Project 1 - Exploratory Data Analysis (EDA)

## 📋 Project Overview

This project demonstrates **Exploratory Data Analysis (EDA)** on customer analytics data. The goal is to clean, analyze, and visualize customer data to extract meaningful insights about customer demographics, income patterns, and their relationships.

## 📊 Dataset

**File:** `customer_analytics.csv`

### Dataset Features:
- **Age:** Customer age
- **Gender:** Customer gender (Male/Female)
- **AnnualIncome:** Annual income of customers
- Other relevant customer demographics

## 🔍 Analysis Steps

### 1. **Data Loading & Initial Exploration**
   - Load data using pandas
   - Display first few rows
   - Check dataset shape and dimensions
   - Examine data types and structure

### 2. **Data Cleaning**
   - Check for missing values
   - Handle missing data:
     - **Numeric columns:** Fill with median value
     - **Categorical columns:** Fill with mode (most frequent value)
   - Identify and remove duplicate rows

### 3. **Exploratory Data Analysis - Univariate Analysis**
   - **Age Distribution:** Histogram with KDE (Kernel Density Estimate)
   - **Income Distribution:** Histogram with KDE
   - **Gender Distribution:** Count plot

### 4. **Multivariate Analysis - Relationships**
   - **Age vs Annual Income:** Scatter plot to identify correlation
   - **Income by Gender:** Box plot for income comparison across genders
   - **Correlation Matrix:** Heatmap showing correlations between numeric variables

### 5. **Data Export**
   - Save cleaned data to `cleaned_customer_analytics.csv`

## 📈 Visualizations Generated

| Visualization | Purpose |
|---|---|
| Age Distribution | Understand age demographics |
| Income Distribution | Understand income patterns |
| Gender Distribution | See gender representation in data |
| Age vs Income Scatter Plot | Identify relationship between age and income |
| Income by Gender Box Plot | Compare income across genders |
| Correlation Heatmap | Find relationships between numeric variables |

## 🛠️ Technologies & Libraries

- **Python 3.x**
- **pandas:** Data manipulation and analysis
- **numpy:** Numerical operations
- **matplotlib:** Data visualization
- **seaborn:** Statistical data visualization

## 📝 Key Findings (After Execution)

The analysis provides insights into:
- Customer age and income distributions
- Gender composition of the customer base
- Relationship between age and annual income
- Income disparities across genders
- Correlation patterns between variables

## 📂 Output Files

- **cleaned_customer_analytics.csv** - Cleaned dataset ready for further analysis

## 🚀 How to Run

1. Ensure the dataset `customer_analytics.csv` is in the same directory
2. Install required libraries:
   ```bash
   pip install pandas numpy matplotlib seaborn
   ```
3. Run the notebook:
   ```bash
   jupyter notebook MiniProject1_EDA.ipynb
   ```
4. Execute cells in order from top to bottom

## 📌 Notes

- The visualization style is set to "whitegrid" for better readability
- All missing values are handled before analysis
- Duplicates are removed to ensure data quality
- The correlation heatmap uses the "coolwarm" color palette

## 🎯 Learning Objectives

✅ Data loading and initial exploration  
✅ Handling missing values  
✅ Identifying and removing duplicates  
✅ Creating meaningful visualizations  
✅ Analyzing univariate and multivariate relationships  
✅ Data cleaning and preprocessing workflow  

## 📄 File Structure

```
Day_20/
├── MiniProject1_EDA.ipynb          # Main notebook with analysis
├── customer_analytics.csv           # Input dataset
├── cleaned_customer_analytics.csv   # Output cleaned dataset
└── README.md                        # This file
```

---

**Project Date:** Day 20 - DS/AI Internship  
**Type:** Mini Project - Exploratory Data Analysis
