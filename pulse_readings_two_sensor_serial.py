import serial
import time
import numpy
from matplotlib import pyplot as plt
from tqdm import  tqdm

# set up Serial connection and data input
s = serial.Serial("/dev/cu.usbserial-01C84FCC",250000)
start = time.perf_counter()
sensor_a_readings = []
sensor_b_readings = []
x = []
data_dumping_arr = []

# collect N datapoints
N = 500
for i in tqdm(range(N)):
    try:
        # grab both sensor datapoints
        data_point = s.readline().strip().decode("utf-8")
        sensor_a_reading = int(data_point.split(',')[1])
        sensor_b_reading = int(data_point.split(',')[0])
        sensor_a_readings.append(sensor_a_reading)
        sensor_b_readings.append(sensor_b_reading)

        # keep track of the corresponding times
        x.append(time.perf_counter())

        # collect data to save to file
        data_dumping_arr.append((x, (sensor_a_reading, sensor_b_reading)))
    except:
        print(i)

assert len(sensor_a_readings) == len(x) and len(sensor_b_readings) == len(x)
# graph output
plt.plot(x, sensor_a_readings, label = "Sensor A Data")
plt.plot(x, sensor_b_readings, label = "Sensor B Data")
plt.xlabel('Time')
plt.ylabel('PPG Sensor Pulse Readings')
plt.legend()
plt.show()

# uncomment below to save results to a file

"""
data_dumping_file = open("raw_readings.txt", "w")
data_dumping_file.write(str(data_dumping_arr))

data_dumping_file.close()
"""