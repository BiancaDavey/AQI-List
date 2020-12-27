# AQI-List

AQI List is a program for reading multiple AQI readings from a file and returning a list of the average AQI readings by location, sorted by average AQI from highest to lowest.

## Features

* Collates data containing multiple AQI readings from multiple locations into a sorted list of average AQI readings by location
* Supports any positive number of AQI readings and locations
* Simple usage procedure

## Installation

Python 3 is required to run this program.

A text editor is required to provide the file containing the AQI data.

## Usage

1. Create a file with a .txt extension.
2. Add the AQI readings to the file in the format of one location name, comma, AQI reading per line.
3. Open the program script using the command `nano air_quality_list.py`.
4. Specify the name of the .txt file as the `FILENAME` variable in the program script.
5. Run the script for the program using the command `python3 air_quality_list.py`.

## Usage Example

```
nano example_AQI_readings.txt
```
![AQI readings in text file.](text.png)

```
nano air_quality_list.py
```
![Specifying filename.](filename.png)

```
python3 air_quality_list.py
```
![Final output of program.](output.png)


## Author

Bianca Davey

bdavey2@myune.edu.au
