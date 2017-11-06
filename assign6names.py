def user():
	names = list(input("Enter names here: "))
	asc = 97
	freq = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	
	for i in range(len(names)):
		for j in range(0,25):
			if ord(names[i]) == asc:
				freq[asc-97] += 1
				j = 26
			asc += 1
		asc = 97
		j = 0
	return freq

def freqList(freq):
	asc = 97
	for i in range(len(freq)):
		asc += 1
		if freq[i] > 0:
			print(chr(asc)+ "-"+ str(freq[i]), end = '')

def main():
	freq = user()	
	freqList(freq)
	print()

main()
