import pandas as pd
import matplotlib.pyplot as plt

# Create DataFrame
data = {
    "Department": ["IT", "HR", "IT", "Sales", "HR", "Sales"],
    "Salary": [50000, 40000, 60000, 45000, 42000, 55000]
}

df = pd.DataFrame(data)

# Group by Department and calculate average salary
summary = df.groupby("Department")["Salary"].mean()

print(summary)

# Visualization
summary.plot(kind="bar")

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.tight_layout()
plt.show()