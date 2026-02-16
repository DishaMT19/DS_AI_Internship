# DS AI Internship Project

This repository contains fundamental Python programming concepts covered during a Data Science & AI internship. The project is organized by daily lessons, progressing from basic syntax to data structures and operations.

## Project Structure

```
DS_AI_Internship/
├── README.md
├── day3fundamentals.py
└── src/
    ├── Day 1/
    │   └── Hello.py
    ├── Day 2/
    │   └── day2fundamentals.py
    ├── Day 3/
    │   └── day3fundamentals.py
    ├── Day 4/
    │   └── day4_pythonfundamentals.py
    ├── Day 5/
    │   └── day5_pythonfundamentals.py
    ├── Day 6/
    │   └── day6_pythonfundamentals.py
    ├── Day 7/
    │   └── day7_pythonfundamentals.py
    ├── Day 8/
    |   └── day8_pythonfundamentals.py
    ├──  Day 9/
    |    └── day9_pythonfundamentals.py
    ├── Day 10/
    |    └── day10_pythonfundamentals.py
    ├── Day 11/
    |   └── day11_pythonfundamentals.py
    ├── Day 12/
    |   └── day12_pythonfundamentals.py
    └── Day 12/
        └── day12_pythonfundamentals.py

  

```

## Course Content

## 📅 Day 1: Welcome & Setup
**Files:**  
- src/Day 1/hello.py  
- src/Day 1/version_check.py  

**Topics Covered:**
- System Orientation & Tool Awareness
- Python Installation & Verification
- VS Code & Anaconda Setup
- GitHub Account & Repository Creation

**Key Learnings:**
- Environment Setup: Installed Python and verified using version commands
- IDE Familiarity: Configured VS Code for Python development
- Version Checking: Used terminal/command prompt to verify Python installation
- First Program: Wrote and executed a basic "Hello World" script
- GitHub Basics: Created repository and pushed initial project files

---

## 📅 Day 2: Variables, Data Types & Control Flow
**File:**  
- src/Day 2/day2fundamentals.py  

**Topics Covered:**
- Data Types: int, float, string, boolean
- Type Checking: Using `type()` function
- User Input: Accepting input with `input()` and type conversion
- Conditional Statements: if-elif-else logic
- Arithmetic Operations: Addition, subtraction, multiplication, division
- Error Handling: Division by zero checks
- String Formatting: String concatenation

---

## 📅 Day 3: Lists & Tuples
**File:**  
- src/Day 3/day3fundamentals.py  

**Topics Covered:**
- Lists & Tuples: Creation and basic usage
- Indexing & Slicing: Accessing elements using positive and negative indexes
- List Methods: append(), insert(), remove(), pop()
- Mutability: Understanding how lists can be modified
- Tuple Immutability: Why tuples are safer for fixed data
- Real-world Use Cases: Lists vs Tuples comparison

---

## 📅 Day 4: Dictionaries & Sets
**File:**  
- src/Day 4/day4fundamentals.py  

**Topics Covered:**
- Dictionaries: Key-value pair data structure
- Dictionary Operations: Adding, updating, deleting elements
- Safe Access: Using `.get()` to avoid KeyErrors
- Iteration: Looping through keys and values
- Sets: Creating unique collections
- Set Operations: Union, intersection, difference
- Duplicate Removal: Using sets for data cleaning

---

## 📅 Day 5: Functions & Modules
**Files:**  
- src/Day 5/main.py  
- src/Day 5/math_operations.py

**Topics Covered:**
- Functions: Defining and calling functions
- Arguments & Return Values
- Variable Scope: Local vs Global
- Built-in Modules: Importing standard Python modules
- Custom Modules: Creating and importing user-defined modules
- Code Organization: Separating logic into reusable components
- Real-world Practice: Power calculation and average computation

---

## Day 6: Key Learnings

- **Working with Files:** Learned how to open, read, write, and append data to files, enabling programs to store information persistently.
- **Safe Resource Management:** Understood how using `with open()` automatically closes files after use, helping prevent memory leaks and file corruption.
- **CSV Data Handling:** Learned the basics of reading and processing CSV files to work with structured, tabular data.
- **Error Handling Techniques:** Gained experience using `try` and `except` blocks to handle errors gracefully without crashing the program.

  ---

## Day 7: File Handling

### 📘 Topics Covered

#### 1. Introduction to File Reading & Writing
- Learned the basics of reading from and writing to files in Python.
- Understood different file modes such as read (`r`), write (`w`), and append (`a`).

#### 2. Context Managers using `with open()`
- Studied how context managers ensure files are properly closed after use, even if an error occurs.
- Learned why the `with open()` syntax is the recommended approach for file handling in Python.
- Understood how improper file handling can lead to memory leaks and resource exhaustion in larger applications.

  ---

  ## 📅 Day 8: NumPy – Arrays, Broadcasting & Reshaping

**File:**  
- `src/Day 8/day8_numpy.py`

**Topics Covered:**
- NumPy Array Creation using `np.array()` and `np.arange()`
- Broadcasting concepts for operations on arrays with different shapes
- Vectorized computations for efficient numerical processing
- Array Reshaping using `reshape()`
- Transpose operations using `transpose()`
- Statistical functions such as `np.mean()`
- Axis-based computations (row-wise and column-wise operations)
- Data preparation techniques for Machine Learning models

---

## 📅 Day 9: Pandas Series – Indexing, Filtering & Data Cleaning

**File:**  
- `src/Day 9/day9_pandas_series.py`

**Topics Covered:**
- Introduction to Pandas Series as a one-dimensional labeled data structure
- Series creation using default and custom indexing
- Indexing and selection techniques (label-based and position-based access)
- Boolean masking for conditional data filtering
- Handling missing data using `dropna()` and `fillna()`
- Representation and detection of missing values (`NaN`)
- Vectorized string operations using the `.str` accessor
- Data preparation techniques for analysis and Machine Learning preprocessing

**Assignments Completed:**
- Task 1: The Product Catalog (Series Creation & Indexing)
- Task 2: The Grade Filter (Boolean Masking & Missing Data)
- Task 3: The Username Formatter (Vectorized String Operations)
----

## 📅 Day 10: Data Cleaning – Missing Values, Duplicates & Validation

**File:**  
- `src/Day 10/day10_data_cleaning.py`

**Topics Covered:**
- Understanding dirty data and common data quality issues
- Identification and handling of missing values in datasets
- Detection and removal of duplicate records
- Data type conversion for numerical and categorical fields
- String cleaning techniques for consistent data representation
- Final data validation to ensure data integrity and reliability
- Preparing clean datasets for analysis and Machine Learning workflows

**Assignments Completed:**
- Task 1: The Integrity Audit (Missing Values & Duplicates)
- Task 2: The Type Fixer (Data Type Conversion)
- Task 3: The Categorical Standardizer (String Cleaning)

---

# 📅 Day 11: Data Visualization – Matplotlib & Plot Customization

**File:**  
- `src/Day 11/day11_data_visualization.py`

**Topics Covered:**
- Introduction to Matplotlib and basic plotting workflow
- Creating Line Plots for trend analysis
- Building Scatter Plots to analyze relationships between variables
- Designing Bar Charts for categorical data comparison
- Customizing plots (titles, labels, legends, colors, gridlines)
- Working with multiple plots using subplots
- Improving readability and presentation quality of visualizations

**Assignments Completed:**
- Task 1: The Trend Tracker (Line Plots)

  ---

  # 📅 Day 12: Take-Home Tasks – Advanced Visualization Practice

**File:**  
- `src/Day 12/day12_take_home_tasks.py`

**Topics Covered:**
- Practical implementation of scatter plots for correlation analysis
- Identifying positive, negative, and no-correlation patterns
- Creating bar charts for comparative analysis
- Designing dashboards using multiple subplots
- Structuring visual outputs for better analytical storytelling
- Enhancing visualization clarity with proper labeling and layout adjustments

**Assignments Completed:**
- Task 1: Correlation Checker (Scatter Plots)
- Task 2: The Comparison Dashboard (Bar Charts & Subplots)

  ---

  # 📅 Day 13: Exploratory Data Analysis (EDA) – Patterns, Relationships & Insights

**File:**  
- `src/Day 13/day13_exploratory_data_analysis.py`

**Topics Covered:**
- Introduction to Exploratory Data Analysis (EDA) and its role in data workflows
- Univariate Analysis for understanding single-variable distributions
- Bivariate Analysis for examining relationships between two variables
- Correlation analysis to measure strength and direction of relationships
- Outlier detection techniques to identify unusual data points
- Interpreting patterns to generate meaningful analytical insights

**Assignments Completed:**
- Task 1: The Distribution Deep-Dive (Univariate Analysis)
- Task 2: The Relationship Map (Bivariate Analysis)
- Task 3: The Pattern Finder (Correlation & Outliers)

  ---

### 🔑 Key Concepts Covered

- Development environment setup and tool configuration  
- Python syntax and program structure  
- Variables, data types, and type conversion  
- User input handling and basic input/output operations  
- Arithmetic operations and operator precedence  
- Conditional statements and decision-making logic  
- Core data structures: lists, tuples, dictionaries, and sets  
- Indexing, slicing, and iteration techniques  
- Data cleaning and duplicate handling using sets  
- Function definition, arguments, and return values  
- Variable scope and lifetime (local vs global)  
- Modular programming and custom module creation  
- File handling using context managers  
- CSV file reading and structured data ingestion  
- Exception handling using try–except blocks  
- NumPy array creation and shape management  
- Vectorized operations for efficient computation  
- Broadcasting for element-wise array operations  
- Array reshaping, stacking, and transposing  
- Statistical operations for data normalization  
- Preparing data with correct dimensions for machine learning models
-  One-dimensional labeled data structures
- Default and custom indexing in Pandas Series
- Label-based (`loc`) and position-based (`iloc`) selection
- Boolean filtering and conditional selection
- Missing value representation (`NaN`)
- Data cleaning using `dropna()` and `fillna()`
- Vectorized operations and `.str` accessor methods
- Dirty data and data quality challenges
- Missing value identification and handling
- Duplicate detection and removal
- Data type conversion techniques
- String cleaning and categorical standardization
- Data validation and integrity checks
- End-to-end data cleaning pipeline
- Data visualization fundamentals and importance in analysis  
- Using Matplotlib for graphical representation of data  
- Line plots for tracking changes over time  
- Scatter plots for identifying relationships and correlations  
- Bar charts for categorical data comparison  
- Plot customization (titles, axis labels, legends, grids)  
- Creating and managing subplots for multiple visual comparisons
- Correlation analysis using scatter plots  
- Visual interpretation of relationships between variables  
- Comparative analysis using bar charts  
- Combining multiple charts using subplots  
- Layout adjustment and dashboard-style visualization design  
- Improving readability with titles, labels, and legends
- Purpose and importance of Exploratory Data Analysis (EDA)  
- Statistical summaries for understanding data distribution  
- Visualization techniques for univariate analysis  
- Identifying relationships using bivariate analysis  
- Correlation measurement and interpretation  
- Detecting and handling outliers in datasets  

  
 
---

### 📘 Internship Progress

| Concept | Day | File |
|-------|-----|------|
| Basic Output | 1 | `Hello.py` |
| Variables & Types | 2 | `day2fundamentals.py` |
| Control Flow | 2 | `day2fundamentals.py` |
| Lists & Tuples | 3 | `day3fundamentals.py` |
| List Operations | 3 | `day3fundamentals.py` |
| Dictionaries & Sets | 4 | `day4fundamentals.py` |
| Dictionary Operations | 4 | `day4fundamentals.py` |
| Function and Moduels  | 5  | `day5_pythonfundamentals.py`|
| Function and Moduels with Specfic Task  | 6  | `day6_pythonfundamentals.py`|
| File Handling  | 7 | `day7_pythonfundamentals.py`|
| Numpy   | 8  |  `day8_pythonfundamentals.py` |
| Pandas   | 9  |  `day9_pythonfundamentals.py` |
| Data Cleaning | 10 | `day10_pythonfundamentals.py` |
| Data Visulization |11| `day11_pythonfundamentals.py `|
|  Data Visulization with Specfic task | 12 |  ` day12_pythonfundmentals.py`|
|  Exploratory Data Analysis (EDA)  |13 |  1day13_pythonfundmentals.py `|
---

### 🎯 Learning Outcomes

- ✅ Understanding system setup, development tools, and project workflows  
- ✅ Installing and verifying Python and required development environments  
- ✅ Using GitHub for repository creation and version control  
- ✅ Understanding Python syntax and program structure  
- ✅ Working with different data types (`int`, `float`, `string`, `bool`)  
- ✅ Performing arithmetic operations and handling operator precedence  
- ✅ Accepting and processing user input  
- ✅ Using conditional statements for decision-making  
- ✅ Creating and manipulating lists and tuples  
- ✅ Applying list methods for data manipulation  
- ✅ Understanding indexing, slicing, and iteration techniques  
- ✅ Creating and using dictionaries and sets  
- ✅ Performing dictionary operations (add, update, delete, access)  
- ✅ Using sets for duplicate removal and set operations  
- ✅ Writing reusable functions with arguments and return values  
- ✅ Understanding variable scope (local vs global)  
- ✅ Creating and importing custom Python modules  
- ✅ Reading from and writing to files using context managers  
- ✅ Parsing CSV files for structured data processing  
- ✅ Handling runtime errors using try–except blocks  
- ✅ Creating and manipulating NumPy arrays  
- ✅ Applying vectorized operations for efficient computation  
- ✅ Using broadcasting for element-wise array operations  
- ✅ Reshaping, stacking, and transposing NumPy arrays  
- ✅ Applying statistical functions for data normalization  
- ✅ Preparing data with correct dimensions for machine learning models  
- ✅ Gained the ability to create and manipulate Pandas Series with meaningful index labels
- ✅ Understood indexing and selection mechanisms for efficient data access
- ✅ Applied boolean masking to filter datasets based on logical conditions
- ✅ Identified, removed, and imputed missing values in real-world data
- ✅ Performed vectorized string operations for efficient data cleaning
- ✅ Developed foundational skills required for data analysis and ML preprocessing
- ✅ Gained the ability to identify and handle dirty data in structured datasets.
- ✅ Understood methods for detecting and resolving missing values.
- ✅ Applied duplicate data detection and removal techniques.
- ✅ Converted data types to appropriate formats for analysis and computation.
- ✅ Cleaned and standardized categorical string data.
- ✅ Ensured final dataset integrity through validation checks.
- ✅ Prepared high-quality datasets suitable for data analysis and Machine Learning workflows.
- ✅ Understanding how to visualize data effectively using Matplotlib  
- ✅ Creating line plots to analyze trends over time  
- ✅ Using scatter plots to identify relationships between variables  
- ✅ Designing bar charts for categorical comparisons  
- ✅ Customizing plots to enhance clarity and presentation quality  
- ✅ Organizing multiple visualizations using subplots  
- ✅ Interpreting graphical outputs to support data-driven decisions
- ✅ Strengthened understanding of correlation through scatter plot analysis  
- ✅ Identified trends and relationships between datasets visually  
- ✅ Built structured comparison dashboards using bar charts  
- ✅ Organized multiple visualizations effectively using subplots  
- ✅ Enhanced presentation quality through proper labeling and formatting  
- ✅ Improved analytical thinking through visual data interpretation
- ✅ Understanding the importance of EDA before advanced analysis or modeling  
- ✅ Performing univariate analysis to examine data distribution and variability  
- ✅ Conducting bivariate analysis to explore relationships between variables  
- ✅ Measuring and interpreting correlation values  
- ✅ Identifying outliers and understanding their impact on analysis  
- ✅ Developing analytical thinking through pattern recognition  
  
---


### 📘 Overall Learning Summary (Day 1 – Day 9)

- Gained familiarity with the development environment through system orientation, tool awareness, and workflow setup.
- Installed and verified Python, configured VS Code and Anaconda, and established a structured development setup.
- Created and managed GitHub accounts and repositories, enabling version control and project submission workflows.
- Developed foundational understanding of Python syntax through basic programs and version verification tasks.
- Learned core Python fundamentals including variables, data types, type casting, and operator precedence.
- Practiced user input handling and basic input/output operations for interactive programs.
- Applied arithmetic operations and implemented basic validation and error-handling logic.
- Built logical decision-making skills using conditional statements and comparison operators.
- Explored lists and tuples, focusing on indexing, slicing, mutability, and real-world use cases.
- Utilized list methods for data manipulation and tuple immutability for configuration-style data.
- Worked with dictionaries to manage structured key–value data and perform iteration.
- Used sets to handle unique data collections, remove duplicates, and perform set operations such as intersection and membership testing.
- Strengthened problem-solving skills through practical assignments like inventory management and data cleaning.
- Learned function definition, argument passing, and return values to modularize code.
- Understood variable scope and lifetime, distinguishing between local and global variables.
- Implemented modular programming by importing standard libraries and creating custom Python modules.
- Improved code organization, reusability, and readability following programming best practices.
- Gained experience with file handling, including reading and writing files using context managers.
- Parsed CSV files for structured data ingestion tasks.
- Implemented robust error handling using `try` and `except` blocks to prevent runtime failures.
- Introduced NumPy for numerical computing and array-based data processing.
- Created NumPy arrays using `np.array()` and `np.arange()` and understood array shapes and dimensions.
- Applied vectorized operations to perform efficient numerical computations without explicit loops.
- Used broadcasting to perform element-wise operations between arrays of different shapes.
- Manipulated array dimensions using reshaping, stacking, and transposing techniques.
- Applied statistical functions such as mean calculation for data analysis and normalization.
- Prepared structured data suitable for machine learning and deep learning models.
- Understood the importance of correct data dimensions for image processing and neural network architectures such as CNNs.
- Developed a strong foundation in Python programming, including variables, data types, operators, and input/output operations.
- Understood control flow constructs such as conditional statements and looping mechanisms.
- Acquired practical experience with functions, modular programming, and code reusability.
- Learned file and directory handling concepts along with basic automation using scripts.
- Explored core data structures including lists, tuples, sets, and dictionaries with real-world examples.
- Gained hands-on experience with NumPy for numerical computing, array operations, broadcasting, reshaping, and statistical computations.
- Applied vectorized operations to improve computational efficiency and code performance.
- Built a foundational understanding of data preparation techniques relevant to data analysis and Machine Learning workflows.
- Developed a clear understanding of data quality issues commonly found in real-world datasets, including missing values, duplicates, and inconsistent data types.
- Learned systematic approaches to identify, analyze, and resolve missing data to improve dataset reliability.
- Applied techniques to detect and remove duplicate records, ensuring data integrity and accuracy.
- Performed data type conversions to transform raw data into analysis-ready formats.
- Implemented string cleaning and standardization techniques to ensure consistency in categorical data.
- Validated cleaned datasets to confirm correctness before analysis and machine learning usage.
- Developed a strong understanding of data visualization principles and their role in data analysis.
- Gained hands-on experience creating line plots, scatter plots, and bar charts using Matplotlib.
- Learned how to customize visual elements such as titles, labels, legends, and grids for better clarity.
- Practiced organizing multiple visualizations using subplots for structured data presentation.
- Improved ability to interpret graphical outputs to extract meaningful insights from datasets.
- Applied visualization concepts to real-world analytical tasks through structured assignments.
- Developed deeper insight into correlation analysis using scatter plots.
- Built comparison dashboards using bar charts and subplots for multi-metric analysis.
- Improved ability to design clean, readable, and professional visual outputs.
- Strengthened confidence in interpreting and presenting data-driven insights.
- Built a strong foundation in Exploratory Data Analysis as a critical step in data workflows.
- Analyzed individual variables to understand distribution, spread, and central tendency.
- Explored relationships between variables using bivariate analysis techniques.
- Applied correlation analysis to quantify relationships and detect meaningful patterns.
- Identified outliers and evaluated their influence on overall dataset behavior.
- Strengthened ability to extract actionable insights from raw data.

---

## Author

Disha M T

## Last Updated

February 16, 2026

