import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [10, 20, 30, 40]

plt.subplot(2, 2, 1)
plt.plot(months, sales)
plt.title("Line")

plt.subplot(2, 2, 2)
plt.bar(months, sales)
plt.title("Bar")

plt.subplot(2, 2, 3)
plt.hist(sales)
plt.title("Histogram")

plt.subplot(2, 2, 4)
plt.scatter(range(4), sales)
plt.title("Scatter")

plt.tight_layout()

plt.show()