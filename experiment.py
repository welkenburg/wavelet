from matplotlib import pyplot as plt
import numpy as np
import math
from graphs import c2DReader

duration = 3 # s
frequency = 10 # Hz
sample_rate = 100 # sample per second
time = np.arange(0.0, duration, duration/sample_rate)
sparam = np.arange(0.01, 100, 0.01)

def wavelet(time, scale=1, offset=0):
	Xcomp = (time - offset) / scale
	exp = np.exp(-Xcomp * Xcomp)
	return np.sin(Xcomp)*exp

def sinewave(time, frequency=440, amplitude=1):
	w = frequency * math.pi * 2
	return amplitude * np.sin(time * w)

def integral(function):
	return np.sum(function)/len(function)

s11 = sinewave(time[:int(len(time)/3)], frequency=10, amplitude=10)
s12 = sinewave(time[:int(len(time)/3)], frequency=20, amplitude=5)
s13 = sinewave(time[:int(len(time)/3)], frequency=100, amplitude=1)

s21 = sinewave(time[int(len(time)/3):2*int(len(time)/3)], frequency=5, amplitude=8)
s22 = sinewave(time[int(len(time)/3):2*int(len(time)/3)], frequency=30, amplitude=5)
s23 = sinewave(time[int(len(time)/3):2*int(len(time)/3)], frequency=20, amplitude=1)

s31 = sinewave(time[2*int(len(time)/3):], frequency=2, amplitude=6)
s32 = sinewave(time[2*int(len(time)/3):], frequency=30, amplitude=4)
s33 = sinewave(time[2*int(len(time)/3):], frequency=50, amplitude=2)

seg1 = s11 + s12 + s13
seg2 = s21 + s22 + s23
seg3 = s31 + s32 + s33

signal = np.concatenate((seg1,seg2,seg3))
# c2DReader.show(time,signal)
# wave = wavelet(time, offset=5)

transform = np.zeros((len(time), len(sparam)))
print(len(time))
for x in np.arange(0,len(time)):
	if x % 10 == 0:
		print(x)
	for y in np.arange(0,len(sparam)):
		transform[x][y] = integral(signal * wavelet(time, scale=sparam[y] ,offset=time[x]))


with open("data/2Darray.npy","wb") as f:
	np.save(f, transform)

print("done!")