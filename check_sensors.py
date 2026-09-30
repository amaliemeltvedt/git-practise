# Importing necessary packages
import yaml
import pandas as pd
import json

# Using "with open()" to read the file
with open("git-practise/config.yml", "r") as file:
    data = yaml.safe_load(file)

# Extracting the data
max_days = data["max_days_since_calibration"]
output_file = data["output_file"]

# Using the pandas package to read the xlsx and csv files
sensors = pd.read_excel("git-practise/sensors.xlsx")
calibrations = pd.read_csv("git-practise/calibrations.csv")

# Using the merge() function to match by sensor_id
combined = pd.merge(sensors, calibrations, on="sensor_id")

# Printing the results
print(combined)

# Identifying the overdue sensors
overdue = combined[combined["days_since_calibration"] > max_days]

# Turning the data into a list of dictionaries for the JSON array
data = overdue[
    ["sensor_id", "lab_room", "owner", "days_since_calibration"]
].to_dict(orient="records")

# Turning the list into a JSON format
with open(output_file, "w") as file:
    json.dump(data, file, indent=2)