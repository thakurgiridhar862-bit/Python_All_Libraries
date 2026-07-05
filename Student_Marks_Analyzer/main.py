import pandas as pd
import matplotlib.pyplot as plt


print("\n" + "=" * 50)
print("          STUDENT MARKS ANALYZER")
print("=" * 50)


df = pd.read_csv("Students_Marks_Analyzer/students.csv")


subjects = ["Maths", "Physics", "Chemistry", "Computers", "Soft Skills"]

df["Total"] = df[subjects].sum(axis=1)

df["Percentage"] = (df["Total"] / 500) * 100


def grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "Fail"


df["Grade"] = df["Percentage"].apply(grade)
