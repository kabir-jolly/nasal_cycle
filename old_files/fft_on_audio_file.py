import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy.fftpack import fft
import numpy as np
filepath = input("Enter a .wav filepath to get it's FFT: ")
rate, data = wav.read(filepath)
fft_out = fft(data)

plt.plot(data, fft_out)
plt.xlim([0, 6000])
plt.show()