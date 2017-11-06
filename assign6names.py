def user():
	names = [str(n) for n in input("Enter names here: ").split()]

	d = {}
	for i in names:
		if i in d:
			d[i] = d.get(i)+1
		else:
			d[i] = 1
	for k,v in d.items():
		print(str(k)+'-'+str(v))

def main():
	user()

main()
