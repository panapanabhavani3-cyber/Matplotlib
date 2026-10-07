import matplotlib.pyplot as plt

class_a = [45, 50, 55, 60, 65, 70, 75, 80]
class_b = [40, 48, 52, 58, 62, 68, 72, 78]

plt.hist(class_a, bins=5, alpha=0.5, label="Class A")
plt.hist(class_b, bins=5, alpha=0.5, label="Class B")

plt.title("Class A vs Class B Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.legend()

plt.show()