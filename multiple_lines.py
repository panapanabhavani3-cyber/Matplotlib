import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]

sales_2025 = [10000, 15000, 12000, 18000]
sales_2026 = [12000, 17000, 16000, 22000]

plt.plot(months, sales_2025, label="2025")
plt.plot(months, sales_2026, label="2026")

plt.title("Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.legend()

plt.show()