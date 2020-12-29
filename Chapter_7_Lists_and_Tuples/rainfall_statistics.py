import pandas as pd
import read_file as read
import matplotlib.pyplot as plt


df_rainfall = read.open_xlsxfile(
    "C:\\Users\\f-eng\\OneDrive\\Documents\\Python\\Projects\\Python_Tutorials\\Chapter_7_Lists_and_Tuples\\rainfall.xlsx")

total = df_rainfall["Rainfall"].sum()
average = total / df_rainfall.shape[0]
min_rainfall = df_rainfall["Rainfall"].idxmin()
max_rainfall = df_rainfall["Rainfall"].idxmax()

print("The total rainfall was: {0:d} mm".format(total))
print("The average monthly rainfall was: {0:.2f} mm".format(average))
print("The month with the least rainfall was: {0} with {1:d} mm".format(
    df_rainfall.iloc[min_rainfall]["Month"], df_rainfall.iloc[min_rainfall]["Rainfall"]))
print("The month with the most rainfall was: {0} with {1: d} mm".format(
    df_rainfall.iloc[max_rainfall]["Month"], df_rainfall.iloc[max_rainfall]["Rainfall"]))
average_plot = [average] * 12
plt.plot(df_rainfall["Month"], df_rainfall["Rainfall"])
plt.plot(df_rainfall["Month"], average_plot)
plt.show()
