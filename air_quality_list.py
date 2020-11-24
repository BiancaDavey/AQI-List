
#!usr/bin/env python3

# This program takes AQI readings for multiple locations and returns a list of the average AQI for each location, sorted in descending order by AQI reading.
#
# This program contains two functions.

# The read_data function takes a file containing AQI data and returns the file content as a dictionary, with location names as keys and AQI readings as values.

def read_data(filename):

    # readings initialises an empty dictionary to be used for the final output of the function.
    # file_content represents the file containing the AQI data.
    # The content of the file must adhere to the required format of location, comma, AQI reading for the function to execute successfully.

    readings = {}
    with open(filename) as file_content:

      # Line number is initialised at the first line of data in the file.
      # For loop traverses the file line by line.
      #
      # Location names are set as keys, and AQI readings are set as their values.
      # Duplicate location names are synthesised into single keys, with a list of their AQI readings as their values.

      line_number = 0  # Line number is initialised to begin for loop at first line.
      for line in file_content:
        key, value = line.strip().split(",")  # Content of each line split into key and value representing location and AQI reading, based on adherence to the required file format.
        if key in readings:
          readings[key].append(float(value))  # AQI readings of duplicate location names appended to the existing key as a float value.
        else:
          readings[key] = [float(value)]
      line_number += 1  # For loop is applied to next line.

    # Function returns dictionary containing each location name with a list of their AQI reading(s).

    return(readings)

# The get_average_dictionary function takes the dictionary returned by the read_data function, calcuates the average AQI for each location name, and returns a dictionary with location names as keys and t$

def get_average_dictionary(readings):

    # Dictionary is initialised for final output.
    # AQI readings in each list of values are added and divided by the number of readings to calculate the average.
    # This is applied to each key value pair in the dictionary taken as the argument for the function.
    # Function returns dictionary containing each location name and its average AQI.

    averages = dict([(key, sum(values)/len(values)) for key, values in readings.items()])
    return(averages)

# Specifies the file containing the data for the AQI readings and locations.

FILENAME = "readings.txt"

# Program will only execute when the script containing the program is directly invoked.

if __name__ == "__main__":

    # Function calls

    try:
        readings = read_data(FILENAME)
        averages = get_average_dictionary(readings)

        # For loop traverses through the keys in the dictionary returned by the get_average_dictionary function, and sorts the average AQI readings by their value from highest to lowest.
        # Final output displays each location name with its average AQI reading, sorted in descending order by average AQI reading.

        for location in sorted(averages, key = averages.get, reverse = True):
            print(location, averages[location])

    # Error handling to ensure that the file to be taken as the argument for the read_data function adheres to the file formatting requirements of the function.

    except (IOError, ValueError):
        print("Error reading {}".format(FILENAME))
        print("Please ensure the file exists and matches the required format")
        print("(each line should begin with a location name, followed by a comma, followed by an AQI reading)")

