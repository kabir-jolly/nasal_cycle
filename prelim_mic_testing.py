# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
from scipy.signal import hilbert
from scipy.interpolate import make_interp_spline
from scipy.interpolate import interp1d

# shows the sound waves
def visualize(path: str):
	
	# reading the audio file
	raw = wave.open(path)
	
	# reads all the frames
	# -1 indicates all or max frames
	signal = raw.readframes(-1)
	signal = np.frombuffer(signal, dtype ="int16")
	# =====
	# analytic_signal = hilbert(signal)
	# amplitude_envelope = np.abs(analytic_signal)
	# =====

	# gets the frame rate
	f_rate = raw.getframerate()

	# to Plot the x-axis in seconds
	# you need get the frame rate
	# and divide by size of your signal
	# to create a Time Vector
	# spaced linearly with the size
	# of the audio file
	time = np.linspace(
		0, # start
		len(signal) / f_rate,
		num = len(signal)
	)

	X_Y_Spline = make_interp_spline(x = time, y = signal, k = 3)
	X_ = np.linspace(time.min(), time.max(), 500)
	#Y_ = X_Y_Spline(X_)
	f_cubic = interp1d(time, signal, kind='cubic')
	# using matlplotlib to plot
	# creates a new figure
	plt.figure(1)
	
	# title of the plot
	file_title = path.split('/')[-1]
	plt.title(f"Sound Wave for file {file_title}")
	
	# label of x-axis
	plt.xlabel("Time")
	
	# actual ploting
	PLOT_INTERVAL = 1
	plt.plot(time[::PLOT_INTERVAL], signal[::PLOT_INTERVAL], label = "Mic Readings")
	# plt.plot(time, amplitude_envelope, label = "Envelope")
	# plt.plot(X_, Y_, label = "Envelope")


	#plt.plot(X_, np.abs(f_cubic(X_)), label = "Envelope")
	

	plt.legend()
	print(signal[:30])
	with open('time.npy', 'wb') as f:
		np.save(f, time)
	with open('signal.npy', 'wb') as f:
		np.save(f, signal)
	# shows the plot
	# in new window
	plt.grid()
	plt.show()

	# you can also save
	# the plot using
	# plt.savefig('filename')


if __name__ == "__main__":
	
	# gets the command line Value
	# path = sys.argv[1]
	path = input("Enter filepath: ")

	visualize(path)
