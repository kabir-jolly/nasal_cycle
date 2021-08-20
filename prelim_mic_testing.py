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
	
	signal = raw.readframes(-1)
	signal = np.frombuffer(signal, dtype ="int16")

	# =====
	# trying to get a smoothed signal
	# analytic_signal = hilbert(signal)
	# amplitude_envelope = np.abs(analytic_signal)
	# =====

	f_rate = raw.getframerate()
	time = np.linspace(
		0, # start
		len(signal) / f_rate,
		num = len(signal)
	)

	X_Y_Spline = make_interp_spline(x = time, y = signal, k = 3)
	X_ = np.linspace(time.min(), time.max(), 500)
	#Y_ = X_Y_Spline(X_)
	f_cubic = interp1d(time, signal, kind='cubic')
	plt.figure(1)
	
	# title of the plot
	file_title = path.split('/')[-1]
	plt.title(f"Sound Wave for file {file_title}")
	
	plt.xlabel("Time")
	
	PLOT_INTERVAL = 1
	plt.plot(time[::PLOT_INTERVAL], signal[::PLOT_INTERVAL], label = "Mic Readings")
	# uncomment below to try enveloping approach
	# plt.plot(time, amplitude_envelope, label = "Envelope")
	# plt.plot(X_, Y_, label = "Envelope")

	#plt.plot(X_, np.abs(f_cubic(X_)), label = "Envelope")

	plt.legend()
	# print(signal[:30])
	# uncomment below to save results to a .npy file
	# with open('time.npy', 'wb') as f:
	# 	np.save(f, time)
	# with open('signal.npy', 'wb') as f:
	# 	np.save(f, signal)
	plt.grid()
	plt.show()
	# plt.savefig('filename')


if __name__ == "__main__":
	
	# gets the command line Value
	# path = sys.argv[1]
	path = input("Enter filepath: ")

	visualize(path)
