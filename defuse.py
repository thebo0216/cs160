userInput = input("Serial, vowel, batteries, port, car, FRK? ")
simonList = []

def password():
	str1 = input("Enter letters: ")
	str2 = input("Enter letters: ")
	str3 = input("Enter letters: ")

	if 'a' in str1 and 'b' in str2 and 'o' in str3:
		print('about')
	elif 'a' in str1 and 'f' in str2 and 't' in str3:
		print('after')
	elif 'a' in str1 and 'g' in str2 and 'a' in str3:
		print('again')
	elif 'b' in str1 and 'e' in str2 and 'l' in str3:
		print('below')
	elif 'c' in str1 and 'o' in str2 and 'u' in str3:
		print('could')
	elif 'e' in str1 and 'v' in str2 and 'e' in str3:
		print('every')
	elif 'f' in str1 and 'i' in str2 and 'r' in str3:
		print('first')
	elif 'f' in str1 and 'o' in str2 and 'u' in str3:
		print('found')
	elif 'g' in str1 and 'r' in str2 and 'r' in str3:
		print('great')
	elif 'h' in str1 and 'o' in str2 and 'u' in str3:
		print('house')
	elif 'l' in str1 and 'a' in str2 and 'r' in str3:
		print('large')
	elif 'l' in str1 and 'e' in str2 and 'a' in str3:
		print('learn')
	elif 'n' in str1 and 'e' in str2 and 'v' in str3:
		print('never')
	elif 'o' in str1 and 't' in str2 and 'h' in str3:
		print('other')
	elif 'p' in str1 and 'l' in str2 and 'a' in str3:
		print('place or plant')
	elif 'p' in str1 and 'o' in str2 and 'i' in str3:
		print('point')
	elif 'r' in str1 and 'i' in str2 and 'g' in str3:
		print('right')
	elif 's' in str1 and 'm' in str2 and 'a' in str3:
		print('small')
	elif 's' in str1 and 'o' in str2 and 'u' in str3:
		print('sound')
	elif 's' in str1 and 'p' in str2 and 'e' in str3:
		print('spell')
	elif 's' in str1 and 't' in str2 and 'i' in str3:
		print('still')
	elif 's' in str1 and 't' in str2 and 'u' in str3:
		print('study')
	elif 't' in str1 and 'h' in str2 and 'e' in str3:
		print('their or there or these')
	elif 't' in str1 and 'h' in str2 and 'i' in str3:
		print('thing or think')
	elif 't' in str1 and 'h' in str2 and 'r' in str3:
		print('three')
	elif 'w' in str1 and 'a' in str2 and 't' in str3:
		print('water')
	elif 'w' in str1 and 'h' in str2 and 'e' in str3:
		print('where')
	elif 'w' in str1 and 'h' in str2 and 'i' in str3:
		print('which')
	elif 'w' in str1 and 'o' in str2 and 'r' in str3:
		print('world')
	elif 'w' in str1 and 'o' in str2 and 'u' in str3:
		print('would')
	elif 'w' in str1 and 'r' in str2 and 'i' in str3:
		print('write')
	else:
		print('letters put in wrong, not a valid password, try again')
		password()

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
		elif colors.count("y") >= 2:
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

def main():
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


























