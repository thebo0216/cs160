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
	colorInput = input("Color of button: ")
	wordInput = input("Word: ")
	if colorInput == "b":
		if wordInput == "abort":
			buttonPart2()		
	elif userInput[2] >= "2":
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

def memory():
	#Stage 1
	display1 = int(input("What nunber is displaying?: "))
	if display1 == 1:
		print("Second position")
		num1 = int(input("What is the number?: "))
		pos1 = "Second position"
	elif display1 == 2:
		print("Second position")
		num1 = int(input("What is the number?: "))
		pos1 = "Second position"
	elif display1 == 3:
		print("Third position")
		num1 = int(input("What is the number?: "))
		pos1 = "Third position"
	elif display1 == 4:
		print("Fourth position")
		num1 = int(input("What is the number?: "))
		pos1 = "Fourth position"
	#Stage 2
	display2 = int(input("What number is displaying?: "))
	if display2 == 1:
		print("Number 4")
		pos2 = int(input("What is the position?: "))
		num2 = "Number 4"
	elif display2 == 2:
		print(pos1)
		num2 = int(input("What number is it?: "))
		pos2 = pos1
	elif display2 == 3:
		print("First positin")
		num2 = int(input("What number is it?: "))
		pos2 = "First position"
	elif display2 == 4:
		print(pos1)
		num2 = int(input("What number is it?: "))
		pos2 = pos1
	#Stage 3
	display3 = int(input("What number is displaying?: "))
	if display3 == 1:
		print(num2)
		pos3 = int(input("What is the position?: "))
		num3 = num2
	elif display3 == 2:
		print(num1)
		pos3 = int(input("What is the position?: "))
		num3 = num1
	elif display3 == 3:
		print("Third position")
		num3 = int(input("What is the number?: "))
		pos3 = "Third position"
	elif display3 ==4:
		print("Number 4")
		pos3 = int(input("What is the position?: "))
		num3 = "Number 4"
	#Stage 4
	display4 = int(input("What numer is displaying?: "))
	if display4 == 1:
		print(pos1)
		num4 = int(input("What is the number?: "))
		pos4 = pos1
	elif display4 == 2:
		print("First position")
		num4 = int(input("What is the number?: "))
		pos4 = "First position"
	elif display4 == 3:
		print(pos2)
		num4 = int(input("What is the number?: "))
		pos4 = pos2
	elif display4 == 4:
		print(pos2)
		num4 = int(input("What si the number?: "))
		pos4 = pos2
	#Stage 5
	display5 = int(input("What is the number displaying?: "))
	if display5 == 1:
		print(num1)
	elif display5 == 2:
		print(num2)
	elif display5 == 3:
		print(num4)
	elif display5 == 4:
		print(num3)

def whosFirst():
	display = input("What is the display?: ")
	if display == "ur":
		print("1, 1")
		whosFirst2()
	elif display == "yes" or "nothing" or "led" or "they are":
		print("1, 2")
		whosFirst2()
	elif display == " " or "reed" or "leed" or "they're":
		print("1, 3")
		whosFirst2()
	elif display == "first" or "okay" or "c":
		print("2, 1")
		whosFirst2()
	elif display == "blank" or "read" or "red" or "you" or "your" or "you're" or "their":
		print("2, 2")
		whosFirst2()
	elif display == "display" or "says" or "no" or "lead" or "hold on" or "you are" or "there" or "see" or "cee":
		print("2, 3")
		whosFirst2()

def whosFirst2():
	word = input("What is the word?: ")
	if word == "ready":
		print("yes, okay, what, left, press, right, blank, ready, no, first, uhhh, nothing, wait")
	elif word == "first":
		print("left, okay, yes, middle, no, right, nothing, uhhh, wait, ready, blank, what, press, first")
	elif word == "no":
		print("blank, uhhh, wait, first, what, ready, right, yes, nothing, left, press, okay, no, middle,")
	elif word == "blank":
		print("wait, right, okay, middle, blank, press, ready, nothing, no, what, left, uhhh, yes, first")
	elif word == "nothing":
		print("uhhh, right, okay, middle, yes, blank, no, press, left, what, wait, first, nothing, ready")
	elif word == "yes":
		print("okay, right, uhhh, middle, first, what, press, ready, nothing, yes, left, blank, no, wait")
	elif word == "what":
		print("uhhh, what, left, nothing, ready, blank, middle, no, okay, first, wait, yes, press, right")
	elif word == "uhhh":
		print("ready, nothing, left, what, okay, yes, right, no, press, blank, uhhh, middle, wait, first")
	elif word == "left":
		print("right, left, first, no, middle, yes, blank, what, uhh, wait, press, ready, okay, nothing")
	elif word == "right":
		print("yes, nothing, ready, press, no, wait, what, right, middle, left, uhhh, blank, okay, first")
	elif word == "middle":
		print("blank, ready, okay, what, nothing, press, no, wait, left, middle, right, first, uhhh, yes")
	elif word == "okay":
		print("middle, no, first, yes, uhhh, nothing, wait, okay, left, ready, blank, press, what, right")
	elif word == "wait":
		print("uhhh, no, blank, okay, yes, left, first, press, what, wait, nothing, ready, right, middle")
	elif word == "press":
		print("right, middle, yes, ready, press, okay, nothing, uhhh, blank, left, first, what, no, wait")
	elif word == "you":
		print("sure, you are, your, your're, next, uh huh, ur, hold, what?, you, uh uh, like, done, u")
	elif word == "you are":
		print("your, next, like, uh huh, what?, done, uh uh, hold, you, u, you're, sure, ur, you are")
	elif word == "your":
		print("uh uh, you are, uh huh, your, next, ur, sure, u, you're, you, what?, hold, like, done")
	elif word == "your're":
		print("you, your're, ur, next, uh uh, you are, u, your, what?, uh huh, sure, done, like, hold")
	elif word == "ur":
		print("done, u, ur, uh huh, what?, sure, your, hold, you're, like, next, uh uh, you are, you")
	elif word == "u":
		print("uh huh, sure, next, what?, you're, ur, uh uh, done, u, you, like, hold, you are, your")
	elif word == "uh huh":
		print("uh huh, your, you are, you, done, hold, uh uh, next, sure, like, you're, ur, u, what?")
	elif word == "uh uh":
		print("ur, u, you are, you're, next, uh uh, done, you, uh huh, like, your, sure, hold, what?")
	elif word == "what?":
		print("you, hold, you're, you, u, done, uh uh, like, you are, uh huh, ur, next, what?, sure")
	elif word == "done":
		print("sure, uh huh, next, what?, your, ur, you're, hold, like, you, u, you are, uh uh, done")
	elif word == "next":
		print("what?, uh huh, uh uh, your, hold, sure, next, like, done, you are, ur, you're, u, you")
	elif word == "hold":
		print("you are, u, done, uh uh, you, ur, sure, what?, you're, next, hold, uh huh, your, like")
	elif word == "sure":
		print("you are, done, like, you're, you, hold, uh huh, ur, sure, u, what?, next, your, uh uh")
	elif word == "like":
		print("you're, next, u, ur, hold, done, uh uh, what?, uh huh, you , like, sure, you are, your")

def complicatedWires():
	wire = input("Enter wire color, star, led")
	if wire == rnn:
		if userInput[0] % 2 == 0:
			print("Cut")
		else:
			print("Don't cut")
	elif wire == ryn:
		print("Cut")
	elif wire == rny or wire == ryy:
		if userInput[2] >= 2:
			print("Cut")
		else:
			print("Don't cut")
	elif wire == bnn:
		if userInput[0] % 2 == 0:
			print("Cut")
		else:
			print("Don't cut")
	elif wire == byn:
		print("Don't cut")
	elif wire == bny or wire == byy:
		if userInput[3] == "y":
			print("Cut")
		else:
			print("Don't cut")
	elif wire == rbnn:
		if userInput[0] % 2 == 0:
			print("Cut")
		else:
			print("Don't cut")
	elif wire == rbyn:
		if userInput[3] == "y":
			print("Cut")
		else:
			print("Don't cut")

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
	elif user == "memory":
		memory()
	elif user == "first":
		whosFirst()

while True:
	main()
	

























