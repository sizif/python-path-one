import random

print("Hello, what's yr favourite number?")
number = input()

print("Your favourite number is " + number)

minNumber = 1
maxNumber = 100
magicNumber = random.randint(minNumber, maxNumber)

message = "The magic number is between {0} and {1}"
print(message.format(minNumber, maxNumber))

found = False

while not found:
	print("Guess what it is?")
	guess = int(input())
	if guess == magicNumber:
		found = True
	if guess < magicNumber:
		print("Too low")
	if guess > magicNumber:
		print("Too high")
print("You got it!")