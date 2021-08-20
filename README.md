# Constructing, Testing, and Evaluating Methods for Analyzing the Nasal Cycle

## bandpass.py
Applies a bandpass filter (both lowpass and highpass filters) to an input audio file. Current thresholds set to attempt replication of the paper "Detection of the nasal cycle in daily activity by remote evaluation of nasal sound" by Tahamiler et al.

## decibles.py
Calculates the decible values of an audio file, but using chunks of audio segments within the file. The number of chunks used can be modified by changing the SCALE_FACTOR value within the file. More chunks result in a finer grained audio analysis but fewer chunks may suffice if the desired goal is to simply calculate (and later average) each exhalation as an individual chunk.

## exhale_extraction.py
Splices the audio file using 3 second intervals. This is done since the original audio is 30 seconds, containing 5 inhalations and 5 exhalations that are of 3 seconds in duration each. Since the inhalations are not important in the study of nasal cycle and determining nostril dominance, they are cut from the audio and then the exhalations are stiched together.

