from sys import argv

age = int(input('Age: '))
weight = input('Weight: ')

print("You're %s years old with %s lbs weight" % (age, weight))

script, first, second, third = argv
print("The script is called:", script)
print("Your first command line variable is:", first)
print("Your second command line variable is:", second)
print("Your third command variable is:", third)