#runtime

def convert(input):

	arithmetic = ''

	words = input.split()
	print(words)
	
	for i in range(len(words)):
		if(words[i].lower() == 'add'): 
			words[i] = '+'
		elif(words[i].lower() == 'gets'):
			words[i] = '+'

	# converted = " ".join(x for x in words)
	for j in range(len(words)):
		if(words[j] == '+'):
			arithmetic += words[j]
		else:
			try: 
				num = int(words[j])
				arithmetic += str(num)

			except(ValueError):
				pass

	return arithmetic

problem = input("Give me a problem: ")
print(problem)
print()

arithmetic = convert(problem)
print()
print("In arithmetic:")
print(arithmetic)

