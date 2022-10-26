from ctypes import sizeof
import numpy as np
from matplotlib import pyplot as plt
from scipy.io.wavfile import write
from scipy.fft import rfft, rfftfreq

SAMPLE_RATE = 44100 # Hertz
DURATION = 5 # Seconds

def generate_sine_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq
    # 2pi because np.sin takes radians
    y = np.sin((2 * np.pi) * frequencies)
    return x, y

# Generate a 2 hertz sine wave that lasts for 5 seconds
_,sin_wave 	= generate_sine_wave(400, SAMPLE_RATE, DURATION)
_,noise 	= generate_sine_wave(10000, SAMPLE_RATE, DURATION)

noise *= 0.2
audio = sin_wave + noise
normalized_audio = np.int16(audio / audio.max() * (2**15 - 1)) # 16bits = 2^15-1 values

write("exp1-noisy sound.wav", SAMPLE_RATE, normalized_audio)

# FFT

N = SAMPLE_RATE * DURATION
yf = rfft(normalized_audio)
xf = rfftfreq(N, 1/SAMPLE_RATE)

plt.plot(xf, np.abs(yf))
plt.show()