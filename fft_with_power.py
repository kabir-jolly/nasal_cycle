import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
import numpy as np
import math
import statsmodels.api as sm
import scipy as sp

def fft(data):
	sampling_frequency = 256
	L = len(data)
	K = 8 #4 highest peaks
	frqMaxPower = 0
	size_with_padding_padding = 2**math.ceil(np.log2(np.abs(L))) #padding to the next power of 2.
	fft_data = sp.fftpack.fft((data - data.mean()), n = size_with_padding_padding)/L
	fft_data_shift = np.fft.fftshift(fft_data)
	power = np.square(np.abs(fft_data_shift))

	freq = np.fft.fftfreq(size_with_padding_padding, d=1/sampling_frequency) # sampling period is around 3.9 msec
	freq0= np.fft.fftshift(freq) #0-centered f
	v_list = power.argsort()[-K:][::-1]
	for item in v_list: 
		# print("****Frq[item]", freq0[item])   
		if freq0[item] > 0.07 and freq0[item] < 0.50:
			frqMaxPower = freq0[item]
			break
	return frqMaxPower, power, freq0

if __name__ == "__main__":
	filepath = input("Enter a .wav filepath to get it's FFT: ")
	rate, data = wav.read(filepath)
	dominant_frq, power, freqs = fft(data)
	plt.plot(freqs, power)
	#plt.xlim([0, 5])
	plt.show()