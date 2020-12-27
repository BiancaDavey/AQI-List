
#!usr/bin/env python3

# This program takes AQI readings for multiple locations and returns a list of the average AQI for each location, sorted in descending order by AQI reading.

# The read_data function takes a file containing AQI data and returns the file content as a dictionary, with location names as keys and AQI readings as values.

def read_data(filename):

    # textFileName initialises an empty dictionary to be used for the final output of a dictionary containing each location name and a list of its AQI readings.
    # file_content represents the file containing the AQI data.
    # The content of the file must adhere to the required format of location, comma, AQI reading for the function to execute successfully.

    exampleAQIFile = {}
    with open(filename) as file_content:

      # Line number is initialised at the first line of data in the file.
      # Duplicate location names are synthesised into single keys, with a list of their AQI readings as their values.

      line_number = 0  
      for line in file_content:
        key, value = line.strip().split(",") 
        if key in exampleAQIFile:
          exampleAQIFile[key].append(float(value)) 
        else:
          exampleAQIFile[key] = [float(value)]
      line_number += 1  
    return(exampleAQIFile)

# The get_average_dictionary function takes the dictionary returned by read_data, calcuates the average AQI per location, and returns a dictionary listing the average AQI per location in descending order.
# AQI readings in each list of values are added and divided by the number of readings to calculate the average.
# # This is applied to each key value pair in the dictionary taken as the argument for the function.

def get_average_dictionary(readings):

    averages = dict([(key, sum(values)/len(values)) for key, values in readings.items()])
    return(averages)

FILENAME = "exampleAQIFile.txt"

# The program will only execute when the script containing the program is directly invoked.

if __name__ == "__main__":

    try:
        readings = read_data(FILENAME)
        averages = get_average_dictionary(readings)
        for location in sorted(averages, key = averages.get, reverse = True):
            print(location, averages[location])

    # Error handling to ensure that the file to be taken as the argument for the read_data function adheres to file formatting requirements.

    except (IOError, ValueError):
        print("Error reading {}".format(FILENAME))
        print("Please ensure the file exists and matches the required format")
        print("(each line should begin with a location name, followed by a comma, followed by an AQI reading)")

