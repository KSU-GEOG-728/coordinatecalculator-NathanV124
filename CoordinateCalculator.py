##-------------------------------------------------------------------------------------
## Name:  CoordinateCalculator.py
## Description:  Converts geographic coordinates in DDMMSS format to DD
## Created:  August 28th 2024
## Author:  Nathan Verrill (ntverrill@ksu.edu)
##-------------------------------------------------------------------------------------

coordinate = input("Enter the coordinates in DDMMSS format:")

def convert_decimal(coord):
    degrees = int(coord[:2])
    minutes = int(coord[2:4])
    seconds = int(coord[4:])

    decimal_degrees = degrees + (minutes / 60) + (seconds / 3600)
    return decimal_degrees

decimal_degrees = convert_decimal(coordinate)
print(f"Your final result is: {round(decimal_degrees, 2)} degrees")
    