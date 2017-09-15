import os
import random
import terminalsize

class Player:
	'''
		A class for a player.
	'''
	def __init__(self, info={}):
	'''
		Instantiates a player.
		info : a dictionnary with all the desired info on the player
	'''
		for key, value in additionalStats.items():
			self.info[key] = value

	def getInfo(self, infoName):
	'''
		Returns the requested info about the player.
		infoname : the name of the key in the info dictionnary
	'''
		return self.info[infoName]


def askInteger(question):
	'''
		Asks the user to enter an integer value.
		question : the question to ask the user
		Returns the user's input.
	'''
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
	'''
		Asks the user to enter an integer value contained within a determined range.
		question : the question to ask the user
		minimum  : the smallest value the user is allowed to enter
		maximum  : the biggest value the user is allowed to enter
		Returns the user's input.
	'''
	valid = False
	userInput = askInteger(question)
	while (valid == False):
		if (userInput >= minimum and userInput <= maximum):
			valid = True
		else:
			userInput = askInteger("Invalid input. Value must be between " + str(minimum) + " and " + str(maximum))
	return userInput

def paragraph(text):
	'''
		Prints text and wait for the user to press enter.
		text : the text to print
	'''
	input(text)

def header(text, align="center"):
	'''
		Prints a header containing a title.
		text  : the title to display
		align : the alignment of the title ('left', 'center' or 'right') (defaults to 'center')
	'''
	terminalWidth = terminalsize.get_terminal_size()[0]
	startPosition = 0

	for i in range(0, terminalWidth):
		print("=", end="")
	if (align == "left"):
		print(text)
	elif (align == "center"):
		startPosition = (terminalWidth - len(text)) // 2
		for i in range(0, startPosition):
			print(" ", end="")
		print(text)
	elif (align == "right"):
		startPosition = (terminalWidth - len(text))
		for i in range(0, startPosition):
			print(" ", end="")
		startPosition = (terminalWidth - len(text))
		print(text, end="")

	for i in range(0, terminalWidth):
		print("=", end="")

def infoHeader():
	terminalWidth = terminalsize.get_terminal_size()[0]
	for i in range(0, terminalWidth):
		print("=", end="")

	

	for i in range(0, terminalWidth):
		print("=", end="")


def rollDie(faces=6):
	'''
		Simulates a die roll.
		faces : number of faces on the rolled die (defaults to 6)
		Returns a random integer between 1 and 'faces'.
	'''
	return random.randint(0, faces)

def clearScreen():
	'''
		Clears the screen.
	'''
	os.system('cls' if os.name == 'nt' else 'clear')

		