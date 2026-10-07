import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [20, 30, 25, 40]

plt.plot(months, sales, marker="o")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.savefig("sales_chart.png")
plt.savefig("sales_chart.pdf")

plt.show()