import matplotlib.pyplot as plt
import numpy as np
import wave, sys
from scipy.signal import hilbert
from scipy.interpolate import make_interp_spline
from scipy.interpolate import interp1d

def moving_average(x):
	# convolutional vs. averaging approaches
	return np.mean(np.array(x).reshape(-1, 175), axis=1)
    # return np.convolve(x, np.ones(w), 'valid') / w

# shows the sound waves
def visualize(path: str):
	
	# reading the audio file
	raw = wave.open(path)
	signal = raw.readframes(-1)
	signal = np.abs(np.frombuffer(signal, dtype ="int16"))[:-1]
	averaged = moving_average(signal)
	f_rate = raw.getframerate()
	print("Len signal: ", len(signal), " Len averaged: ", len(averaged))
	time = np.linspace(
		0, # start
		len(signal) / f_rate,
		num = len(signal)
	)
	time_adj = np.linspace(
		0, # start
		len(signal) / f_rate,
		num = len(averaged),
	)

	plt.figure(1)
	
	# title of the plot
	file_title = path.split('/')[-1]
	plt.title(f"Sound Wave for file {file_title}")
	
	# label of x-axis
	plt.xlabel("Time")
	
	# actual ploting
	PLOT_INTERVAL = 1
	plt.plot(time[::PLOT_INTERVAL], signal[::PLOT_INTERVAL], label = "Mic Readings")
	plt.plot(time_adj, averaged, label = "Avg")
	# plt.plot(X_, Y_, label = "Envelope")


	#plt.plot(X_, np.abs(f_cubic(X_)), label = "Envelope")
	

	plt.legend()
	plt.grid()
	plt.show()


if __name__ == "__main__":
	path = input("Enter filepath: ")
	visualize(path)