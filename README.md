# Constructing, Testing, and Evaluating Methods for Analyzing the Nasal Cycle

## bandpass.py
Applies a bandpass filter (both lowpass and highpass filters) to an input audio file. Current thresholds set to attempt replication of the paper "Detection of the nasal cycle in daily activity by remote evaluation of nasal sound" by Tahamiler et al.

## decibles.py
Calculates the decible values of an audio file, but using chunks of audio segments within the file. The number of chunks used can be modified by changing the SCALE_FACTOR value within the file. More chunks result in a finer grained audio analysis but fewer chunks may suffice if the desired goal is to simply calculate (and later average) each exhalation as an individual chunk.

## exhale_extraction.py
Splices the audio file using 3 second intervals. This is done since the original audio is 30 seconds, containing 5 inhalations and 5 exhalations that are of 3 seconds in duration each. Since the inhalations are not important in the study of nasal cycle and determining nostril dominance, they are cut from the audio and then the exhalations are stiched together.

## fft_with_power.py
Translates the audio file (amplitude over time) into a FFT graph (power over frequency) such that frequencies can be analyzed for the microphone readings.

## highpass_on_audio.py
Applies a 10kHz highpass filter to the microphone readings. A qualitative analysis determined that this helped clear artifacts from the input signal and led to easier calculations of values used to determine nostril dominance.

## konno_mead.py
Implements the Konno-Mead strategy used to visually and quantitatively analyze chest and abdominal movements. This essentially means that the amplitudes of the signals from left and right pulse readings are graphed against each other. An ordinary least squares model was used to determine the linearity in this relationship.

## mic_loudness_logging.py
Calculates the integral loudness of an input audio file. Uses the pyloudnorm library which follows the ITU-R BS.1770-4 recommendation for audio loudness.

## prelim_mic_testing.py
Plots the microphone readings. Also has experimental code for looking at finding an enveloping function to plot around these readings.

## pulse_readings_two_sensor_serial.py
Takes PPG sensor readings by establishing a serial connection. Saves them to a file for future access and plots the results.

## wav_data_smoothing.py
Two attempts at smoothing the data by (1) using a moving average across sets of timesteps in the audio file and (2) using a convolutional based approach to downsample the input.

## data_and_ouputs
Graphs, data dumps, and audio files used before and after processing.

## old_files
Misc scripts no longer in use.
