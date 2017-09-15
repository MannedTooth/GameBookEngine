def askInteger(question):
	valid = False
	userInput = input(question + "\n")
	while (valid == False):
		try:
			userInput = int(userInput)
			valid = True
		except ValueError:
			userInput = input("Invalid input. Value must be an integer.\n")
	return userInput

def askIntegerWithinRange(question, minimum, maximum):
	valid = False
	userInput = askInteger(question)
	while (valid == False):
		if (userInput >= minimum and userInput <= maximum):
			valid = True
		else:
			userInput = askInteger("Invalid input. Value must be between " + str(minimum) + " and " + str(maximum))
		