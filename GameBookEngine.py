import os
import random
import terminalsize

class Player:
	#	A class for a player.
	
	def __init__(self, skill, stamina, luck):
	#	Instantiates a player.

		self.skill = skill
		self.stamina = stamina
		self.luck = luck

	def getInfo(self, infoName):
	#	Returns the requested info about the player.
	#	infoname : the name of the key in the info dictionnary

		return self.info[infoName]

class Creature:
	# A class for an enemy creature.

	def __init__(self):
		pass


def askInteger(question):
	#	Asks the user to enter an integer value.
	#	question : the question to ask the user
	#	Returns the user's input.
	
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
	#	Asks the user to enter an integer value contained within a determined range.
	#	question : the question to ask the user
	#	minimum  : the smallest value the user is allowed to enter
	#	maximum  : the biggest value the user is allowed to enter
	#	Returns the user's input.
	
	valid = False
	userInput = askInteger(question)
	while (valid == False):
		if (userInput >= minimum and userInput <= maximum):
			valid = True
		else:
			userInput = askInteger("Invalid input. Value must be between " + str(minimum) + " and " + str(maximum))
	return userInput

def paragraph(text):
	#	Prints text and wait for the user to press enter.
	#	text : the text to print
	terminalWidth = terminalsize.get_terminal_size()[0]
	position = 0
	words = []
	words = text.split(" ")

	for word in words:
		if (position + len(word) > terminalWidth):
			print("\n" + word, end=" ")
			position = len(word) + 1
		elif (word == "\n" or position + len(word) == terminalWidth):
			print(word, end="")
			position = 0
		else:
			print(word, end=" ")
			position = position + len(word) + 1
		
	input("\n")

def header(text, align="center"):
	#	Prints a header containing a title.
	#	text  : the title to display
	#	align : the alignment of the title ('left', 'center' or 'right') (defaults to 'center')
	
	terminalWidth = terminalsize.get_terminal_size()[0]
	startPosition = 0

	clearScreen()

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


def rollDice(numberOfDice=1, faces=6):
	#	Simulates a die roll.
	#	numberOfDice : number of dice to roll (defaults to 1)
	#	faces        : number of faces on the rolled die (defaults to 6)
	#	Returns a list of random integers between 1 and 'faces'.

	dices = []
	for i in range(0, numberOfDice):
		dices.append(random.randint(1, faces))

	return dices

def sumOfRollDice(numberOfDice=1, faces=6):
	#	Sums the result of a die roll.
	#	numberOfDice : number of dice to roll (defaults to 1)
	#	faces        : number of faces on the rolled die (defaults to 6)
	#	Returns the sum of the die roll.

	return sum(rollDice(numberOfDice, faces))

def clearScreen():
	#	Clears the screen.
	
	os.system('cls' if os.name == 'nt' else 'clear')