import matplotlib.pyplot as plt
import numpy as np

sizes = [20, 200, 2000, 20000]

plt.figure(figsize=(10, 8))

for i in range(len(sizes)):
    data = np.random.uniform(0, 200, sizes[i])
    plt.subplot(2, 2, i+1)
    plt.hist(data, bins=15, color='red', edgecolor='black')
    plt.title("n = " + str(sizes[i]))

plt.tight_layout()
plt.show()