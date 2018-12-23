# Calculates time, gallons of gas used, and cost of gasoline for a trip
distance = input("Input distance of trip in miles: ") #The value you input from the command line is a string.
distance = float(distance) #We need to convert it from a string to a number.
mpg = 30.
speed = 60.
costPerGallon = 4.10
time = distance / speed
gallons = distance / mpg
cost = gallons * costPerGallon