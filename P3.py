# Calculates time, gallons of gas used, and cost of gasoline for a trip

distance = 400.         # miles
mpg = 30.               # car mileage
speed = 60.             # average speed
costPerGallon = 4.10    # price of gas

time = distance/speed
gallons = distance/mpg
cost = gallons*costPerGallon

print(time,gallons,cost)

#print("%.2f %.2f %.2f" % (time,gallons,cost))
