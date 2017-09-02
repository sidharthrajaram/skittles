#runtime

problem = input("Give me a problem: ")
print(problem)
print()

arithmetic = ''
for w in problem.split():
	if(w.lower() == 'add'):
		print("+")
	else:
		print(w)
