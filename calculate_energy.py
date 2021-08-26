import numpy as np
import os
from scipy.io import wavfile
from pydub import AudioSegment
import matplotlib.pyplot as plt

MIC_FILEPATH = "data_and_outputs/exhalations_only_filtered_audio_highpass_Microphone_L_open.wav"
AMBIENCE_FILEPATH = ""
FRAME_RATE = 44100

def calculate_energy(audio_data):
	N = len(audio_data)
	audio_data = abs(audio_data)
	audio_data = np.square(audio_data)
	energy = np.sum(audio_data) / N
	return energy

def remove_ambience(mic_filepath, ambience_filepath):
	fifteen_sec = 15000
	mic_samplerate, mic_data = wavfile.read(mic_filepath)
	ambience_samplerate, ambience_data = wavfile.read(ambience_filepath)
	interval_len = len(mic_data)
	# match ambience timeframe to be exactly as long as the mic recording
	ambience_data = ambience_data[:interval_len]
	assert len(ambience_data) == len(mic_data)
	data_w_ambience_removed = np.subtract(mic_data, ambience_data)
	return data_w_ambience_removed

def visualize(data):
	num_seconds_in_interval = 15
	time = np.linspace(
		0, # start
		num_seconds_in_interval,
		# len(signal) / f_rate,
		num = len(data)
	)
	plt.title("Plotting microphone exhalations with ambient noise removed")
	plt.plot(time, data)
	plt.show()


if __name__ == "__main__":
	samplerate, data = wavfile.read(MIC_FILEPATH)
	energy_before = calculate_energy(data)
	print(f"Energy before ambience removal: {energy_before}")
	assert samplerate == FRAME_RATE
	if AMBIENCE_FILEPATH != "":
		data = remove_ambience(MIC_FILEPATH, AMBIENCE_FILEPATH)
		energy_after = calculate_energy(data)
		print(f"Energy after ambience removal: {energy_after}")
	visualize(data)