from matplotlib import pyplot as plt
import numpy as np

def show(time, signal):
	plt.plot(time, signal)
	plt.show()

if __name__ == "__main__":
	with open("data/signal.npy","rb") as f:
		signal = np.load(f)
		time = np.load(f)

	plt.figure()
	plt.plot(time, signal)

	plt.show()