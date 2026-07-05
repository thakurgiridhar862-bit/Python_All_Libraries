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


df["Rank"] = df["Total"].rank(ascending=False, method="dense").astype(int)


topper = df.loc[df["Total"].idxmax()]

print("\nCLASS TOPPER")
print("-" * 50)
print(f"Name        : {topper['Name']}")
print(f"Total Marks : {topper['Total']}")
print(f"Percentage  : {topper['Percentage']:.2f}%")
print(f"Grade       : {topper['Grade']}")

# ==================================================

print("\nTOP 10 STUDENTS")
print("-" * 50)

top10 = df.nlargest(10, "Total")

print(top10[["Name", "Total", "Percentage", "Grade", "Rank"]])

print("\nSUBJECT TOPPERS")
print("-" * 50)

for subject in subjects:
    subject_topper = df.loc[df[subject].idxmax()]
    print(f"{subject:<12}: {subject_topper['Name']} ({subject_topper[subject]})")


print("\nLOW ATTENDANCE STUDENTS (<75%)")
print("-" * 50)

low_attendance = df[df["Attendance"] < 75]

print(low_attendance[["Name", "Attendance"]])


print("\nCLASS WISE AVERAGE PERCENTAGE")
print("-" * 50)

class_avg = df.groupby("Class")["Percentage"].mean().round(2)

print(class_avg)

print("\nFAILED STUDENTS")
print("-" * 50)

fail_students = df[(df[subjects] < 40).any(axis=1)]

print(fail_students[["Name"] + subjects])
