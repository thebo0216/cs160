userInput = input("Serial, vowel, batteries, port, car, FRK? ")
simonList = []

def password():
	string1 = input("Enter letters: ")
	string2 = input("Enter letters: ")
	string3 = input("Enter letters: ")

	if 'a' in string1:
		if 'b' in string2:
			if 'o' in string3:
				print("about")
		elif 'f' in string2:
			if 't' in string3:
				print("after")
		elif 'g' in string2:
			if 'a' in string3:
				print("again")
	if 'b' in string1:
		if 'e' in string2:
			if 'l' in string3:
				print("below")
	if 'c' in string1:
		if 'o' in string2:
			if 'u' in string3:
				print("could")
	if 'e' in string1:
		if 'v' in string2:
			if 'e' in string3:
				print("every")
	if 'f' in string1:
		if 'i' in string2:
			if 'r' in string3:
				print("first")
		elif 'o' in string2:
			if 'u' in string3:
				print("found")
	if 'g' in string1:
		if 'r' in string2:
			if 'e' in string3:
				print("great")
	if 'h' in string1:
		if 'o' in string2:
			if 'u' in string3:
				print("house")
	if 'l' in string1:
		if 'a' in string2:
			if 'r' in string3:
				print("large")
		elif 'e' in string2:
			if 'a' in string3:
				print("learn")
	if 'n' in string1:
		if 'e' in string2:
			if 'v' in string3:
				print("never")
	if 'o' in string1:
		if 't' in string2:
			if 'h' in string3:
				print("other")
	if 'p' in string1:
		if 'l' in string2:
			if 'a' in string3:
				print("place or plant")
		elif 'o' in string2:
			if 'i' in string3:
				print("point")
	if 'r' in string1:
		if 'i' in string2:
			if 'g' in string3:
				print("right")
	if 's' in string1:
		if 'm' in string2:
			if 'a' in string3:
				print("small")
		elif 'o' in string2:
			if 'u' in string3:
				print("sound")
		elif 'p' in string2:
			if 'e' in string3:
				print("spell")
		elif 't' in string2:
			if 'i' in string3:
				print("still")
			elif 'u' in string3:
				print("study")
	if 't' in string1:
		if 'h' in string2:
			if 'e' in string3:
				print("their, there, or these")
			elif 'i' in string3:
				print("thing or think")
			elif 'r' in string3:
				print("three")
	if 'w' in string1:
		if 'a' in string2:
			if 't' in string3:
				print("water")
		elif 'h' in string2:
			if 'e' in string3:
				print("where")
			elif 'i' in string3:
				print("which")
		elif 'o' in string2:
			if 'r' in string3:
				print("world")
			elif 'u' in string3:
				print("would")
		elif 'r' in string2:
			if 'i' in string3:
				print("write")

def simpleWires():
	colors = input("What are the colors of the wires in order? ")
	if len(colors) == 3:
		if "r" not in colors:
			print("Cut the second wire")
		elif colors[2] == "w":
			print("Cut the last wire")
		elif colors.count("b") == 2:
			print("Cut the last blue wire")
		else:
			print("Cut the last wire")
	if len(colors) == 4:
		if colors.count("r") >= 2:
			if userInput[0] % 2 == 1:
				print("Cut the last red wire")
		elif colors[3] == "y":
			if 'r' not in colors:
				print("Cut the first wire")
		elif colors.count("b") == 1:
			print("Cut the first wire")
		elif colors.count("y") >= 2:+
			print("Cut the last wire")
		else:
			print("Cut the second wire")
	if len(colors) == 5:
		if colors[4] == "q":
			if userInput[0] % 2 == 1:
				print("Cut the fourth wire")
		elif colors.count("r") == 1:
			if colors.count("y") >= 2:
				print("Cut the first wire")
		elif "q" not in colors:
			print("Cut the second wire")
		else:
			print("Cut the first wire")
	if len(colors) == 6:
		if "y" not in colors:
			if unserInput[0] % 2 == 1:
				print("Cut the third wire")
		elif colors.count("y") == 1:
			if colors.count("w") >= 2:
				print("Cut the fourth wire")
		elif "r" not in colors:
			print("Cut the last wire")
		else:
			print("Cut the fourth wire")
def simon():
	if userInput[1] == "y":
		flash = input("What is flashing? ")
		if flash == "r":
			simonList.append("blue")
		elif flash == "b":
			simonList.append("red")
		elif flash == "g":
			simonList.append("yellow")
		elif flash == "y":
			simonList.append("green")
		print(simonList)
		user = input("Would you like to run this again? ")
		if user == "y":
			simon()
		else:
			simonList = []
	elif userInput[1] == "n":
		flash = input("What is flashing? ")
		if flash == "r":
			simonList.append("blue")
		elif flash == "b":
			simonList.append("yellow")
		elif flash == "g":
			simonList.append("green")
		elif flash == "y":
			simonList.append("red")
		print(simonList)
		user = input("Would you like to run this again? ")
		if user == "y":
			simon()
		else:
			simonList = []
			
def buttonPart2():
	inputColor = input("Hold and input the color: ")
	if inputColor == "b":
		print("4")
	elif inputColor == "w":
		print("1")
	elif inputColor == "y":
		print("5")
	else:
		print("1")

def button():
	colorInput = input("Color of button")
	wordInput = input("Word: ")
	if colorInput == "b":
		if wordInput == "abort":
			buttonPart2()
	elif userInput[2] >= 2:
		if wordInput == "detonate":
			print("Press and immediatley release")
	elif colorInput == "w":
		if userInput[4] == "y":
			buttonPart2()
	elif userInput[2] >= 3:
		if userInput[5] == "y":
			print("Press and immediatley release")
	elif colorInput == "y":
		buttonPart2()
	elif colorInput == "r":
		if wordInput == "hold":
			print("Press and immediatley release")
	else:
		buttonPart2()

main():
	user = input("What function would you like to run? ")
	if user == "pas":
		password()
	elif user == "simple":
		simpleWires()
	elif user == "simon":
		simon()
	elif user == "button":
		button()

main()


























