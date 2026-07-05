import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("Employee_Salary_Analyzer/employees.csv")
print("\n" + "=" * 50)
print("       Employees Salary Analyzer ")
print("=" * 50)

df["Total Compensation"] = df["Salary"] + df["Bonus"]
Highest_Paid = df.loc[df["Salary"].idxmax()]

Lowest_Paid = df.loc[df["Salary"].idxmin()]

print("\nHighest Paid Employee")
print("-" * 50)
print(f"Name       : {Highest_Paid['Name']}")
print(f"EmployeeID : {Highest_Paid['EmployeeID']}")
print(f"Salary     : {Highest_Paid['Salary']}")
print(f"Department : {Highest_Paid['Department']}")
print(f"Experience : {Highest_Paid['Experience']}")
print(f"Bonus      : {Highest_Paid['Bonus']}")
print(f"Total Compensation : {Highest_Paid['Total Compensation']}")
print("-" * 50)
print("\nLowest Paid Employee")
print("-" * 50)
print(f"Name:        {Lowest_Paid['Name']}")
print(f"EmployeeID : {Lowest_Paid['EmployeeID']}")
print(f"Salary :     {Lowest_Paid['Salary']}")
print(f"Department : {Lowest_Paid['Department']}")
print(f"Experience : {Lowest_Paid['Experience']}")
print(f"Bonus      : {Lowest_Paid['Bonus']}")
print(f"Total Compensation : {Lowest_Paid['Total Compensation']}")


print("\nTop 10 highest Salaries")
print("-" * 50)
top10 = df.nlargest(10, "Salary")
print(top10[["Name", "EmployeeID", "Salary", "Department", "Experience"]])

dept_avg = df.groupby("Department")["Salary"].mean().round(2)
dep_max = df.groupby("Department")["Salary"].max()
dep_min = df.groupby("Department")["Salary"].min()
dep_Employees = df["Department"].value_counts()
dep_total = df.groupby("Department")["Salary"].sum()
# ================================
# Depatment Wise Output
# ================================
print("\nDEPARTMENT WISE ANALYSIS")
print("-" * 50)
dept_analysis = pd.DataFrame(
    {
        "Average Salary": dept_avg,
        "Maximum Salary": dep_max,
        "Minimum Salary": dep_min,
        "Employee Count": dep_Employees,
        "Total Expenses": dep_total,
    }
)

print(dept_analysis.to_string())
