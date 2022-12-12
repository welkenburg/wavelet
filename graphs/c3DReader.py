from matplotlib import pyplot as plt
import numpy as np

def show(data):
	plt.imshow(data, cmap='hot', aspect=100)
	plt.show()

if __name__ == "__main__":
	with open("data/2Darray.npy","rb") as f:
		data = np.load(f)

	plt.imshow(data, cmap='Blues', aspect=100)

	plt.show()