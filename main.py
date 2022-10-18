from re import A
from scipy.io import wavfile # scipy library to read wav files
import numpy as np

AudioName = "uprising.wav" # Audio File
fs, Audiodata = wavfile.read(AudioName)

# Plot the audio signal in time
import matplotlib.pyplot as plt
plt.plot(Audiodata[11000:11200])
plt.title('Audio signal in time',size=16)
plt.show()

print(np.shape(Audiodata))
print(Audiodata[11000:11200])