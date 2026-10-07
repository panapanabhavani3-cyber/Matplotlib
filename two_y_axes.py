import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]

sales = [100, 150, 120, 180, 200]
customers = [20, 30, 25, 40, 50]

fig, ax1 = plt.subplots()

ax1.plot(months, sales)
ax1.set_xlabel("Month")
ax1.set_ylabel("Sales")

ax2 = ax1.twinx()
ax2.plot(months, customers)
ax2.set_ylabel("Customers")

plt.title("Sales and Customers")
plt.show()