import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("students_performance.csv")
df["total"]= df["maths"] + df["science"] + df["english"]
df["average"] = df["total"] / 3
topper = df.loc[df["average"].idxmax()]
print("topper:")
print(topper)
lowest = df.loc[df["average"].idxmin()]
print("lowest:")
print(lowest)
class_average = df["average"].mean()
print("class average:" , class_average)
df["rank"] = df["average"].rank(ascending=False, method="min")
plt.figure(figsize=(7,4))
plt.bar(df["name"],df["average"])
plt.title("students average marks")
plt.xlabel("student name")
plt.ylabel("average marks")
plt.ylim(0,100)
plt.grid()
plt.show()
df.to_csv("student_report.csv", index=False)
print("report saved successfully")
def grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"
df["grade"] = df["average"].apply(grade)
print(df)
df["result"] = np.where(df["average"] >= 35, "pass", "fail")
print(df)
grade_counts = df["grade"].value_counts()
plt.figure(figsize= (6,6))
plt.pie(grade_counts,
labels= grade_counts.index,
        autopct = "%1.1f%%",
        startangle=90)
plt.title("grade distribution")
plt.show()
print("\n===========STUDENT PERFORMANCE REPORT==========")
print("total students:" , len(df))
print("class average:" , round(df["average"].mean(),2))
print("highest average:" , round(df["average"].max(),2))
print("lowest average:" , round(df["average"].min(),2))
print("\ntopper:") , print(df.loc[df["average"].idxmax(),["name", "average","grade"]])
print("\nlowest scorer:") , print(df.loc[df["average"].idxmin(),["name", "avearage","grade"]])
print("\npass percentage:", round((df["result"] == "pass").mean() * 100,2) "%")