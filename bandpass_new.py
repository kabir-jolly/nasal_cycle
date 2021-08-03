# https://dsp.stackexchange.com/questions/56604/bandpass-filter-for-audio-wav-file
import numpy as np
import os
from scipy.io import wavfile
from scipy.signal import butter, lfilter

WAV_FILE_NAME = input("Enter a .wav filepath to apply a bandpass filter on it: ")
lowcut = 10.0
highcut = 150.0
FRAME_RATE = 44100

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

def bandpass_filter(buffer):
    return butter_bandpass_filter(buffer, lowcut, highcut, FRAME_RATE, order=6)

samplerate, data = wavfile.read(WAV_FILE_NAME)
assert samplerate == FRAME_RATE
filtered = np.apply_along_axis(bandpass_filter, 0, data).astype('int16')
wavfile.write('filtered_audio.wav', samplerate, filtered)