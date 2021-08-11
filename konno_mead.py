import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# load numpy data
FILEPATH = "two_pulse_sensors_readings.csv"
sensor_df = pd.read_csv(FILEPATH)
print(sensor_df.head())
sensor_a_readings = sensor_df["Sensor A Readings"].values
sensor_b_readings = sensor_df["Sensor B Readings"].values
times = sensor_df["Time"].values
# use mpl to plot konno mead graphs
plt.plot(times, sensor_a_readings, label = "Sensor A [Left]")
plt.plot(times, sensor_b_readings, label = "Sensor B [Right]")
plt.xlabel('Time')
plt.ylabel('PPG Sensor Pulse Readings')
plt.legend()
plt.show()
# do amplitude differences result in a unique shape?