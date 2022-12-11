from random import sample
from re import A
from scipy.io import wavfile # scipy library to read wav files
import numpy as np
from scipy.fft import rfft, rfftfreq
import matplotlib.pyplot as plt

AudioName = "uprising.wav" # Audio File
SAMPLE_RATE, Audiodata = wavfile.read(AudioName)

left_sound, right_sound = np.split(Audiodata, 2, axis=1)

min_bound = 10000
step = 1000
sample_data = left_sound[min_bound:min_bound+step]
sample_data = np.array(list(sample_data))

yf = rfft(sample_data)
xf = rfftfreq(len(sample_data)*2-1, 1 /SAMPLE_RATE)

plt.figure(112)
plt.plot(sample_data)
plt.title('Audio signal in time',size=16)

plt.figure(122)
plt.plot(xf, np.abs(yf))
plt.show()