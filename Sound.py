import librosa
#loading audio file

from python_speech_features import mfcc
import scipy.io.wavfile as wav
import numpy as np
import librosa.display

from tempfile import TemporaryFile
import os
import pickle
import random 
import operator

import math

f='samples/Apiano.mp3'
x, sr = librosa.load(f) #x=pts pour pyplot, sr=fréquence (22KHz mono by default)
print(sr)
x = np.sin(200 * 2 * math.pi * np.arange(0,100, sr * 100 ))
print(type(x))
#visualizing audio
def see():
	import matplotlib.pyplot as plt
	import librosa.display
	plt.figure(figsize=(14,5)) #size plt
	librosa.display.waveshow(x, sr=sr) #display(pts,avc freq)
	plt.show()

#playing sound
def hear():
	import IPython.display as ipd # import ipython lib
	ipd.Audio(f, rate=sr, autoplay=False) #display audio file play (no autoplay)

#Spectogram(norm)
def specto():
	import matplotlib.pyplot as plt
	X =librosa.stft(x) #short term fourier transformation(pour specto)		
	Xdb = librosa.amplitude_to_db(abs(X)) #transforme l'amplitude en dB
	plt.figure(figsize=(14,5))
	librosa.display.specshow(Xdb,sr=sr,x_axis='time',y_axis='hz') #display specto, def axis
	plt.colorbar()  #barre de couleure droite
	plt.show()
#Spectogram (log)
def specto_log():
	import matplotlib.pyplot as plt
	X =librosa.stft(x) #short term fourier transformation(pour specto)		
	Xdb = librosa.amplitude_to_db(abs(X)) #transforme l'amplitude en dB
	plt.figure(figsize=(14,5))
	librosa.display.specshow(Xdb,sr=sr,x_axis='time',y_axis='log') #display specto, def axis
	plt.colorbar()  #barre de couleure droite
		
#Créa son


#Spectral Centroid
def spectral_cent(): #Basically shows the center of mass of a spectrum (frenauency of energy of a spectrum)
	import sklearn
	import matplotlib.pyplot as plt
	spectral_centroids = librosa.feature.spectral_centroid(x, sr=sr)[0]
	spectral_centroids.shape
	(775,)
	# Computing the time variable for visualization
	plt.figure(figsize=(12, 4))
	frames = range(len(spectral_centroids))
	t = librosa.frames_to_time(frames)
	# Normalising the spectral centroid for visualisation
	def normalize(x, axis=0):
		return sklearn.preprocessing.minmax_scale(x, axis=axis)
	#Plotting the Spectral Centroid along the waveform
	librosa.display.waveshow(x, sr=sr, alpha=0.4)
	plt.plot(t, normalize(spectral_centroids), color='b')
		
#Spectral Rolloff
def spectral_roll():
	import sklearn
	import matplotlib.pyplot as plt
	spectral_rolloff = librosa.feature.spectral_rolloff(x+0.01, sr=sr)[0]
	plt.figure(figsize=(12, 4))
	# Computing the time variable for visualization
	frames = range(len(spectral_rolloff))
	t = librosa.frames_to_time(frames)
	def normalize(x, axis=0):
		return sklearn.preprocessing.minmax_scale(x, axis=axis)
	#Plotting the Spectral Centroid along the waveform
	librosa.display.waveshow(x, sr=sr, alpha=0.4)
	plt.plot(t, normalize(spectral_rolloff), color='r')
		
#Spectral bandwith
def sbw(p):
	import matplotlib.pyplot as plt
	import sklearn
	if p < 2:
		return('p as to be sup 2')
	else:
		sb = librosa.feature.spectral_bandwidth(x+0.01, sr=sr, p=p)[0]
		def normalize(x, axis=0):
			return sklearn.preprocessing.minmax_scale(x, axis=axis)
		frames = range(len(sb))
		t = librosa.frames_to_time(frames)
		plt.figure(figsize=(15, 9))
		librosa.display.waveshow(x, sr=sr, alpha=0.4)
		plt.plot(t, normalize(sb), color='r')
		plt.legend(('p =',p))

#zero-crossing rate (is it smooth?)
def smooth():
	import matplotlib.pyplot as plt
	#Plot the signal:
	librosa.display.waveshow(x, sr=sr)
	# Zooming in
	n0 = 9000
	n1 = 9100
	plt.figure(figsize=(14, 5))
	plt.plot(x[n0:n1])
	plt.grid()	
	zero_crossings = librosa.zero_crossings(x[n0:n1], pad=False)
	return(sum(zero_crossings))
		
#Spectre de l'envellope humaine
def mfcc():
	import matplotlib.pyplot as plt
	mfccs = librosa.feature.mfcc(x, sr=sr)
	print(mfccs.shape)
	(20, 97)
	#Displaying  the MFCCs:
	plt.figure(figsize=(15, 7))
	librosa.display.waveshow(mfccs, sr=sr, x_axis='time')

specto()