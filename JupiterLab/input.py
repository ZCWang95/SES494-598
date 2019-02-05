a=input("input something here:")
print(a)
# Calculates time, gallons of gas used, and cost of gasoline for a trip
distance = input("Input distance of trip in miles: ")
distance = float(distance)
mpg = 30.
speed = 60.
costPerGallon = 4.10
time = distance / speed
gallons = distance / mpg
cost = gallons * costPerGallon