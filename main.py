import matplotlib.pyplot as plt
ax, fig = plt.subplots()
x = [2, 4, 5, 3, 2, 0, 7]
y = [num for num in range(0, 13, 2)]
plt.plot(y, x)
plt.show()