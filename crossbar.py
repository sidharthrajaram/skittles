#multiplication division testbed

multwords = ["each"]
operation = ''
operators = []
numbers = []
problem = []

def findNumbers():
	for word in problem:
		try: 
			num = int(word)
			numbers.append(str(num))
		except(ValueError):
			pass
	print("numbers in problem (in order):")
	print(numbers)

problem_input = input("Give me a problem: ")
print()

problem = problem_input.split()

findNumbers()
print()
# findAddSumOperators()




