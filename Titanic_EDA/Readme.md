# 🚢 Titanic Dataset - Data Cleaning & Exploratory Data Analysis

This project performs Data Cleaning and Exploratory Data Analysis (EDA) on the famous Titanic dataset to understand the factors that influenced passenger survival.

The analysis includes data cleaning, univariate analysis, bivariate analysis, feature engineering, and correlation analysis using Python.

---

# 📌 Project Objectives

- Understand the Titanic dataset
- Perform Data Cleaning
- Handle Missing Values
- Analyze Individual Features
- Explore Relationships Between Features
- Create New Features
- Identify Survival Patterns
- Visualize Data using Charts

---

# 📂 Dataset

Dataset Used:

- train.csv

Dataset Features:

- PassengerId
- Survived
- Pclass
- Name
- Sex
- Age
- SibSp
- Parch
- Ticket
- Fare
- Cabin
- Embarked

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- VS Code
- Git & GitHub

---

# 📊 Project Workflow

## 1. Dataset Overview

- Total Rows
- Total Columns
- Missing Values
- Duplicate Values
- Memory Usage
- Column Names
- Data Types
- Statistical Summary

---

## 2. Data Cleaning

- Filled missing values in Age using Median
- Filled missing values in Embarked using Mode
- Removed Cabin column due to excessive missing values
- Removed unnecessary columns
- Removed duplicate records

---

## 3. Univariate Analysis

Categorical Analysis

- Survival Distribution
- Gender Distribution
- Passenger Class Distribution
- Embarkation Port Distribution
- Siblings/Spouse Distribution
- Parents/Children Distribution

Numerical Analysis

- Age Distribution
- Fare Distribution

---

## 4. Bivariate Analysis

- Gender vs Survival
- Passenger Class vs Survival
- Embarkation Port vs Survival
- Age vs Survival
- Fare vs Survival

---

## 5. Feature Engineering

Created a new feature:

- Family Size = SibSp + Parch + 1

Analysis Performed

- Family Size Distribution
- Family Size vs Survival

---

## 6. Correlation Analysis

- Correlation Matrix
- Heatmap Visualization

---

# 📈 Visualizations

The project includes:

- Countplots
- Histograms
- Boxplots
- Correlation Heatmap

Total Graphs Generated: **18**

---

# 📌 Key Insights

- Most passengers did not survive the disaster.
- Female passengers had a much higher survival rate than males.
- First-class passengers had better survival chances.
- Most passengers boarded from Southampton.
- Most passengers traveled alone or with small families.
- Younger passengers had slightly better survival chances.
- Higher fare passengers were more likely to survive.
- Small families showed better survival rates.
- Fare and Passenger Class showed noticeable relationships with survival.

---

# 📁 Project Structure

```
Task_2_Titanic_EDA/
│
├── data/
│   └── train.csv
│
├── graphs/
│
├── analysis.py
│
├── README.md
│
└── requirements.txt
```

---

# 🚀 Conclusion

This project demonstrates the complete Exploratory Data Analysis workflow, including data cleaning, visualization, feature engineering, and extracting meaningful insights from real-world data.

It serves as a strong beginner-friendly portfolio project for Data Analytics and Data Science.

---

# 👨‍💻 Author

**Giridhar Jadon**

GitHub:
https://github.com/thakurgiridhar862-bit