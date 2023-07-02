from sys import argv

script, first, second, third = argv

print ("This is your script name:", script)
print ("This is your first argument", first)
print ("This is your second argument", second)
print ("This is your 3rd argument", third)

age = input ("your age is:")
height = input ("Your height is:")

print (f"So you are {age} years old and {height} cm high.")
