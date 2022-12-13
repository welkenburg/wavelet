from matplotlib import pyplot as plt
import numpy as np

transform = np.zeros((1000, 1000))
for i in range(1000):
	for j in range(1000):
		transform[i][j] = np.exp(((i-500)/10000)**2 + ((j-500)/10000)**2)

plt.imshow(transform, cmap='Blues', aspect=1)
plt.show()