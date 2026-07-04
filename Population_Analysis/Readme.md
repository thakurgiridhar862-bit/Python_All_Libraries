# 🌍 Population Distribution Analysis (2024)

A complete Data Analysis project that explores global population trends using World Bank population data. The project focuses on data cleaning, exploratory data analysis (EDA), statistical insights, and visualizations to understand how population is distributed across countries and regions worldwide.

---

## 📌 Project Overview

This project analyzes population data of 217 countries for the year 2024.

The objective was to:

- Clean and preprocess raw World Bank population data
- Remove aggregated and non-country records
- Analyze population distribution across countries
- Identify the most and least populated countries
- Compare population across regions
- Generate meaningful visual insights using Python

---

## 🎯 Project Objectives

- Understand global population distribution
- Perform data cleaning and preprocessing
- Extract statistical insights
- Create professional visualizations
- Identify regional population patterns
- Practice real-world Exploratory Data Analysis (EDA)

---

## 📂 Dataset

### Dataset Source

World Bank Population Dataset

### Files Used

- Population Data
- Country Metadata
- Cleaned Dataset (`newdata.csv`)

### Final Dataset

- 217 Countries
- 73 Columns
- Population Data from 1960–2024

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- VS Code
- Git & GitHub

---

## 🧹 Data Cleaning Process

The raw dataset contained several aggregate records such as:

- World
- South Asia
- High Income
- OECD Members
- IDA & IBRD Groups

These records were removed to ensure analysis was performed only on actual countries.

### Cleaning Steps

- Removed unnecessary columns
- Removed aggregate regions and economic groups
- Verified missing values
- Verified duplicate records
- Created a clean country-level dataset
- Converted population values into millions for better visualization

---

## 📊 Statistical Analysis

### Highest Population Country

| Country | Population |
|----------|-----------|
| India | 1.45 Billion |

### Lowest Population Country

| Country | Population |
|----------|-----------|
| Tuvalu | 9,646 |

### Population Statistics

| Metric | Value |
|----------|----------|
| Average Population | 37.41 Million |
| Median Population | 6.59 Million |

---

## 📈 Visualizations

### 1️⃣ Population Distribution Histogram

Analyzed the distribution of population across countries.

#### Key Findings

- Most countries have relatively small populations
- A few countries contain extremely large populations
- Population distribution is highly right-skewed
- Large population outliers significantly impact the average

---

### 2️⃣ Top 10 Most Populated Countries

#### Countries Identified

1. India
2. China
3. United States
4. Indonesia
5. Pakistan
6. Nigeria
7. Brazil
8. Bangladesh
9. Russian Federation
10. Ethiopia

---

### 3️⃣ Region-Wise Population Distribution

Population was aggregated by geographical regions to understand regional demographic concentration.

#### Top Regions

- East Asia & Pacific
- South Asia
- Sub-Saharan Africa

---

## 🔍 Key Insights

### Insight 1

India is the most populated country in the world with approximately **1.45 billion** people.

### Insight 2

China remains the second most populated country with approximately **1.41 billion** people.

### Insight 3

The average population is significantly higher than the median population, indicating the presence of large population outliers.

### Insight 4

East Asia & Pacific is the most populated region globally with more than **2.3 billion** people.

### Insight 5

A large portion of the world's population is concentrated in Asia.

### Insight 6

Most countries have populations below 100 million, while only a few countries exceed 1 billion people.

---

## 📁 Project Structure

```text
Task_1_Population_Analysis
│
├── data
│   ├── data.csv
│   └── newdata.csv
│
├── graphs
│   ├── dist_pop.png
│   ├── top10_most_pop_country.png
│   └── region_wise_population.png
│
├── analysis.py
│
└── README.md
```

---

## 🚀 Conclusion

This project demonstrates the complete workflow of a real-world data analysis task, including data cleaning, exploratory analysis, statistical interpretation, and visualization. The analysis highlights global population inequalities and reveals how population is concentrated across specific countries and regions.

---

## ⭐ Skills Demonstrated

- Data Cleaning
- Data Wrangling
- Exploratory Data Analysis (EDA)
- Statistical Analysis
- Data Visualization
- Pandas
- Matplotlib
- Seaborn
- Problem Solving

---

### 📌 Project Status

✅ Completed

---

## 👨‍💻 Author

**Giridhar Thakur**

- AIML Student
- Python Developer
- Data Scientist Enthusiast
- Aspiring AI/ML Engineer
