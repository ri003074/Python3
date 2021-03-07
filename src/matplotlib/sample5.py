import matplotlib.pyplot as plt

x = ["p1", "p2", "p3"]
y = [4, 5, 6]
z = [7, 8, 9]

# fig, ax = plt.subplots()
# ax.plot(x, y)
# ax.plot(x, z)

# plt.show()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(x, y, label="y")
ax.plot(x, z, label="z")
ax.legend(loc="lower right")
plt.show()
