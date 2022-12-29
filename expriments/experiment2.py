import numpy as np
import matplotlib.pyplot as plt
import librosa

def genSine(duration, frequency, offset= 0, samplerate = 100, totlength=-1):
	time = np.arange(offset,duration+offset,1/samplerate)
	signal = np.sin(2* np.pi * frequency * time)
	if(totlength <= duration):
		return signal
	before = np.zeros((offset)*samplerate)
	after = np.zeros((totlength-offset-duration)* samplerate)
	return np.concatenate((before,signal,after))

def genWavelets(frequencies, offset, samplerate=100, duration=10):
	time = np.arange(0,duration,1/samplerate) - offset
	timeFrequenciePlane = np.outer(frequencies, time) # dot product
	sinComponent = np.sin(2* np.pi * timeFrequenciePlane)
	expTimeComponent = np.exp(-time**2)
	expComponent = np.repeat([expTimeComponent], [np.size(frequencies)], axis=0) # matching dimentions
	return np.multiply(sinComponent,expComponent)


# Hz = [
# 	genSine(duration=10, frequency=10,	totlength=60, offset=10),
# 	genSine(duration=10, frequency=20,	totlength=60, offset=20),
# 	genSine(duration=10, frequency=30,	totlength=60, offset=30),
# 	genSine(duration=10, frequency=40,	totlength=60, offset=40),
# 	genSine(duration=10, frequency=60,	totlength=60, offset=50)
# ]
# signal = sum(Hz)

# SAMPLE_RATE = 100
# DURATION = 100
# scaleCoef = 100
# nprange = np.arange(0,DURATION,1/SAMPLE_RATE)
# signal = np.sin(nprange* 2 * np.pi * np.exp(nprange/scaleCoef))

# AudioName = "samples/uprising.wav" # Audio File
# SAMPLE_RATE, Audiodata = wavfile.read(AudioName)

# left_sound, right_sound = np.split(Audiodata, 2, axis=1)

# min_bound = 10000
# step = 1 * SAMPLE_RATE
# signal = np.array(left_sound[min_bound:min_bound+step]).reshape((step,))

audioName = "samples/Apiano.mp3"
signal, SAMPLE_RATE = librosa.load(audioName)
DURATION = 0.4#np.size(signal) / SAMPLE_RATE
print(SAMPLE_RATE, DURATION)
signal = signal[:int(DURATION*SAMPLE_RATE)]

sgplt = plt.subplot(211)
sgplt.plot(np.arange(0,DURATION,1/SAMPLE_RATE), signal,color="red")
# plt.show()
frequencies = np.arange(0,400,10,dtype=np.float)

transformBuffer = []

for offset in np.arange(0,DURATION,1/SAMPLE_RATE):
	if offset * SAMPLE_RATE % (DURATION * SAMPLE_RATE / DURATION) <= 0.1:
		print(offset * SAMPLE_RATE // (DURATION * SAMPLE_RATE / DURATION))
	wavelets = genWavelets(frequencies, offset=offset, duration=DURATION, samplerate=SAMPLE_RATE)
	transform = signal * wavelets
	transformBuffer.append(np.abs(np.trapz(transform)))

# print(np.shape(transformBuffer))
trsmPlt = plt.subplot(212)
xres, yres = np.shape(transformBuffer)
trsmPlt.imshow(transformBuffer, cmap='hot', aspect=yres/xres)
plt.show()
