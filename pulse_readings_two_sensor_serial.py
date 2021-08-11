import serial
import time
import numpy
from matplotlib import pyplot as plt
from tqdm import  tqdm
import pandas as pd

# set up Serial connection and data input
s = serial.Serial("/dev/cu.usbserial-01C84FCC",250000)
start = time.perf_counter()
sensor_a_readings = []
sensor_b_readings = []
times = []
data_dumping_arr = []

# collect N datapoints
N = 1000
for i in tqdm(range(N)):
    try:
        # grab both sensor datapoints
        data_point = s.readline().strip().decode("utf-8")
        sensor_a_reading = int(data_point.split(',')[0])
        sensor_b_reading = int(data_point.split(',')[1])
        sensor_a_readings.append(sensor_a_reading)
        sensor_b_readings.append(sensor_b_reading)

        # keep track of the corresponding times
        times.append(time.perf_counter())

        # collect data to save to file
        data_dumping_arr.append((x, (sensor_a_reading, sensor_b_reading)))
    except:
        print(f"There was an error reading in sensor data at point {i}")

assert len(sensor_a_readings) == len(times) and len(sensor_b_readings) == len(times)

# turn them into numpy arrays
sensor_a_readings = np.array(sensor_a_readings)
sensor_b_readings = np.array(sensor_b_readings)
times = np.array(times)

# save in a tabular format
sensor_df = pd.DataFrame()
sensor_df["Time"] = times
sensor_df["Sensor A Readings"] = sensor_a_readings
sensor_df["Sensor B Readings"] = sensor_b_readings
sensor_df.to_csv('two_pulse_sensors_readings.csv', index = False)

# graph output
plt.plot(times, sensor_a_readings, label = "Sensor A [Left]")
plt.plot(times, sensor_b_readings, label = "Sensor B [Right]")
plt.xlabel('Time')
plt.ylabel('PPG Sensor Pulse Readings')
plt.legend()
plt.show()

# comment/uncomment for saving results to a file


data_dumping_file = open("raw_readings.txt", "w")
data_dumping_file.write(str(data_dumping_arr))

data_dumping_file.close()
