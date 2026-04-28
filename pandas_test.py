import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "salary": [70000, 80000, 90000],
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

print("\nSelected columns:")
print(df[["name", "age"]])

print("\nFiltered rows (age > 28):")
print(df[df["age"] > 28])

print("\nAverage salary by age:")
print(df.groupby("age")["salary"].mean())