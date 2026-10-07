import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]

y1 = [10, 20, 30, 40, 50]
y2 = [15, 25, 20, 35, 45]

plt.plot(x, y1, label="Product A")
plt.plot(x, y2, label="Product B")

plt.title("Product Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.legend()

plt.show()