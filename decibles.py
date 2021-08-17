from scipy.io.wavfile import read
# samprate, wavdata = read('/Users/kabirjolly/Documents/NasalCycleProject/data_and_outputs/exhalations_only_filtered_audio_highpass_Microphone_L_open.wav')
samprate, wavdata = read('/Users/kabirjolly/Documents/NasalCycleProject/data_and_outputs/exhalations_only_filtered_audio_highpass_Microphone_R_open.wav')

import numpy as np
import math
import statistics 
numchunks = wavdata.size/(samprate/0.25)
print(numchunks)
chunks = np.array_split(wavdata, numchunks)
dbs = [20*math.log10( math.sqrt(statistics.mean(chunk**2)) ) for chunk in chunks]
dbs = np.array(dbs)
print(dbs)
print(len(dbs))
print(dbs.mean())