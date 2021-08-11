# https://dsp.stackexchange.com/questions/56604/bandpass-filter-for-audio-wav-file
import numpy as np
import os
from scipy.io import wavfile
from scipy.signal import butter, lfilter
from prelim_mic_testing import visualize

WAV_FILE_NAME = input("Enter a .wav filepath to apply a bandpass filter on it: ")
highcut = 10000.0 # 10kHz highpass filter
FRAME_RATE = 44100

# def orders 5-5-6
def butter_bandpass(highcut, fs, order=3):
    nyq = 0.5 * fs
    high = highcut / nyq
    b, a = butter(order, high, btype='highpass')
    return b, a

def butter_bandpass_filter(data, highcut, fs, order=3):
    b, a = butter_bandpass(highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

def bandpass_filter(buffer):
    return butter_bandpass_filter(buffer, highcut, FRAME_RATE, order=3)

samplerate, data = wavfile.read(WAV_FILE_NAME)
assert samplerate == FRAME_RATE
filtered = np.apply_along_axis(bandpass_filter, 0, data).astype('int16')
filename = 'filtered_audio_highpass.wav'
wavfile.write(filename, samplerate, filtered)

visualize(filename)