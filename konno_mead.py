import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm

# plot OLS line against y vs. y data to look at linearity
def OLS(sensor_a_data , sensor_b_data):
	X = sm.add_constant(sensor_a_data)
	model = sm.OLS(sensor_b_data, X)
	results = model.fit()
	intercept = results.params[0]
	slope = results.params[1]
	# print("SLOPE: ", slope)
	if (slope > 1):
		print("Left Dominance")
	else:
		print("Right Dominance")
	rsquared = results.rsquared
	y_predict = intercept + slope * sensor_a_data
	return y_predict

FILEPATH = "two_pulse_sensors_readings.csv"
sensor_df = pd.read_csv(FILEPATH)
print(sensor_df.head())
sensor_a_readings = sensor_df["Sensor A Readings"].values
sensor_b_readings = sensor_df["Sensor B Readings"].values
times = sensor_df["Time"].values
# use mpl to plot konno mead graphs
fig, (ax1, ax2) = plt.subplots(2)
fig.suptitle('Pulse Readings and Konno-Mead')
ax1.plot(times, sensor_a_readings, label = "Sensor A [Left]")
ax1.plot(times, sensor_b_readings, label = "Sensor B [Right]")
ax1.set(xlabel = 'Time', ylabel = 'PPG Sensor Pulse Readings')
# ax1.set_title('Pulse Readings Over Time')
y_pred = OLS(sensor_a_readings, sensor_b_readings)
ax1.legend()
ax2.plot(sensor_a_readings, sensor_b_readings)
ax2.plot(sensor_a_readings, y_pred, label = "OLS Regression")
ax2.legend()
ax2.set(xlabel = 'Left Sensor Readings', ylabel = 'Right Sensor Readings')
# ax2.set_title('Konno-Mead Diagram of Left vs. Right Pulse Readings')
plt.show()
# do amplitude differences result in a unique shape?
