import soundfile as sf
import pyloudnorm as pyln

while True:
	filepath = input("Enter a .wav filepath to get it's normalized loudness: ")
	if (len(filepath) != 0):
		data, rate = sf.read(filepath) # load audio

		# peak normalize audio to -1 dB
		peak_normalized_audio = pyln.normalize.peak(data, -1.0)

		# measure the loudness first 
		meter = pyln.Meter(rate) # create BS.1770 meter
		loudness = meter.integrated_loudness(data)
		print("Loudness: ", loudness)
		# loudness normalize audio to -12 dB LUFS
		loudness_normalized_audio = pyln.normalize.loudness(data, loudness, -12.0)
		print("Normalized Loudness: ", loudness_normalized_audio)
	else:
		break