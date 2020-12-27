# AQI-List

AQI List is a program for reading AQI readings for multiple locations from a txt file and returning a list of the average AQI readings for each location in descending order.

## Features

* Collates data containing multiple AQI readings from multiple locations into a sorted list of average AQI readings by location
* Supports any positive number of AQI readings and locations
* Simple usage procedure

## Installation

Python 3 is required to run this program.

A text editor is required to provide the file containing the AQI data.

## Usage

1. Create a file with a .txt extension.
2. Add the AQI readings to the file in the format of one location name, comma, and AQI reading per line.
3. Open the program script using the command `nano air_quality_list.py`.
4. Specify the name of the .txt file to match `exampleAQIList.txt` file as in the program script, or customise it.
5. Run the script for the program using the command `python3 air_quality_list.py`.

## Usage Example

```
nano exampleAQIFile.txt
```
[![example-AQIFiletxt.png](https://i.postimg.cc/jj3LmzqG/example-AQIFiletxt.png)](https://postimg.cc/WDrNJqkn)


```
python3 air_quality_list.py
```
[![AQI-List-Usage-Example.png](https://i.postimg.cc/nzsCJCCM/AQI-List-Usage-Example.png)](https://postimg.cc/5YVx595M)


## Author

Bianca Davey

bdavey2@myune.edu.au
