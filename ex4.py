cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90

#Calculating the cars not driven against drivers
cars_not_driven = cars - drivers

#Calculating cars driven against drivers
cars_driven = drivers

#Calculating carpool capacity
carpool_capacity = cars_driven * space_in_a_car

#Calculating passengers per car
average_passengers_per_car = passengers / cars_driven


print ("There are ", cars, "cars available.")
print ("There are only ", drivers, "drivers available.")
print ("There will be ", cars_not_driven, "empty cars today.")
print ("We can Transport ", carpool_capacity, "people today.")
print ("We have ", passengers, "people to carpool today.")
print ("We need to put about", average_passengers_per_car, "people in each car.")

