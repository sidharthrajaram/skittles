#main word problem solver

addwords = ['gets','get','more','add','adds','got','added','received','gives','receives']
subwords = ['gave','lost','away','takes','take', 'took','taking','losing','loses']

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

def findAddSumOperators():
	init_index = 0
	end_index = 0

	for i in range(len(problem)-1):

		for num in numbers:

			if(problem[i] == num):
				#print("***********************")
				init_index = i
				# print("inIT")
				# print(init_index)

				start = init_index+1

				while(start < len(problem)):

					for num in numbers:

						if(problem[start] == num):
							end_index = start
							break

					if(end_index == start):
						break

					start+=1

				first = init_index
				last = end_index
				# print("indices")
				# print(first)
				# print(last)
				# print()

				if(first == last):
					break

				#the count up
				addnum = 0
				subnum = 0

				while(first < last):
					for key in addwords:
						if(problem[first].lower() == key):
							#print("ADD WORD FOUND")
							addnum+=1

					for key in subwords:
						if(problem[first].lower() == key):
							#print("SUB WORD FOUND")
							subnum+=1

					first+=1

				# print("add")
				# print(addnum)
				# print("sub")
				# print(subnum)

				if(addnum > subnum):
					operators.append('+')
				else:
					operators.append('-')
			pass

	print()
	print("problem operators (in order):")
	print(operators)

problem_input = input("Give me a problem: ")
print()

problem = problem_input.split()

findNumbers()
print()
findAddSumOperators()




