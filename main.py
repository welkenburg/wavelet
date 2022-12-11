from scipy.io import wavfile
from matplotlib import pyplot as plt
import numpy as np


samplerate, data = wavfile.read('./samples/sample-3s.wav')
data = data.T[0]
time = np.arange(0.0, len(data)/samplerate, 1/samplerate)

plt.plot(time, data)
plt.show()