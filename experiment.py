from matplotlib import pyplot as plt
import numpy as np
import math

duration = 1 # s
frequency = 100 # Hz
sample_rate = 1000 # sample per second
time = np.arange(0.0, duration, duration/sample_rate)

def wavelet(time, scale=1, offset=0):
	Xcomp = (time - offset) / scale
	exp = math.exp(-Xcomp * Xcomp)
	return math.sin(Xcomp)*exp

def sinewave(time, frequency=440):
	w0 = math.pi * 2 / frequency
	return np.sin(time)

def integral(function):
	return np.sum(function)/len(function)

signal = sinewave(time, frequency=100)

# transform = []
# for dt in simple_time:
# 	transform.append(integral(signal * wavelet(10, dt, simple_time)))

plt.figure()
# plt.subplot(211)
# plt.plot(simple_time, transform)

plt.subplot(111)
plt.plot(time, signal)

plt.show()