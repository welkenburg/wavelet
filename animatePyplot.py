#/bin/python

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig = plt.figure(figsize=(6,4))
axes = fig.add_subplot(1,1,1)
# plt.title("Dynamic Axes")

t = [np.arange(0,3,0.01),np.arange(3,6,0.01),np.arange(6,10,0.01)]
frequency = [1,2,1/2] #Hz
f = []
for i in range(3):
	f.append(np.sin(2 * np.pi * frequency[i] * t[i]))
f = np.concatenate(f)
t = np.concatenate(t)

t2 = [np.arange(0,4,0.01), np.arange(4,8,0.01), np.arange(8,10,0.01)]
frequency = [0,10,0] #Hz
f2 = []
for i in range(3):
	f2.append(np.sin(2 * np.pi * frequency[i] * t2[i]))
f2 = np.concatenate(f2)

f = f + f2

integ = []
integ2 = []
integ3 = []
integ4 = []
x = []
scale = 100
freqw = 1

# timeshift = np.arange(0,10,0.01)

# timePeriod = f * np.multiply(np.sin(2 * np.pi * freqw*(t-timeshift/scale)),np.exp(-(t-timeshift/scale)**2))
# print(np.shape(timePeriod))
# timeSpace = np.abs(np.trapz(timePeriod,axis=1))

# exit()

# plt.plot(timeSpace, timeshift, color="red")
# plt.show()

def animate(i):
	wavelet = np.multiply(np.sin(2 * np.pi * freqw*(t-i/scale)),np.exp(-(t-i/scale)**2))
	y = f * wavelet

	wavelet2 = np.multiply(np.sin(2 * np.pi * 1/2*(t-i/scale)),np.exp(-(t-i/scale)**2))
	y2 = f * wavelet2

	wavelet3 = np.multiply(np.sin(2 * np.pi * 2*(t-i/scale)),np.exp(-(t-i/scale)**2))
	y3 = f * wavelet3

	wavelet4 = np.multiply(np.sin(2 * np.pi * 10*(t-i/scale)),np.exp(-(t-i/scale)**2))
	y4 = f * wavelet4

	integ.append(np.abs(np.trapz(y)))
	integ2.append(np.abs(np.trapz(y2)))
	integ3.append(np.abs(np.trapz(y3)))
	integ4.append(np.abs(np.trapz(y4)))
	x.append(i/scale)
	# plt.xlim(i-30,i+3)
	# axes.set_ylim(-2, 2)
	fig.clear(True)
	graph1 = plt.subplot(212)
	graph1.plot(t,f,color="green")
	#plt.plot(t,wavelet,color="cyan")
	#plt.plot(t,y, color="red") #, scaley=True, scalex=True
	graph2 = plt.subplot(211)
	graph2.plot(x, integ, color="blue")
	graph2.plot(x, integ2, color="orange")
	graph2.plot(x, integ3, color="red")
	graph2.plot(x, integ4, color="green")

anim = FuncAnimation(fig, animate, interval=100)
plt.show()



