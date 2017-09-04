#main word problem solver

addwords = ['gets','get','more','add','adds','got','added','received','gives']
subwords = ['gave','lost','away','takes','take', 'took','taking','losing','loses']

add_count = 0
sub_count = 0
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

def findOperators():
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


		#find intervals of numbers and keywords between



def addition(problem):
	count = 0
	for word in problem:
		for key in addwords:
			if(word.lower() == key):
				count += 1
	return count


def subtraction(problem):
	count = 0
	for word in problem:
		for key in subwords:
			if(word.lower() == key):
				count += 1
	return count


#find operation between set of numbers?

def convert(input):

	arithmetic = ''

	words = input.split()
	problem = words
	print(words)

	add_count = addition(words)
	print(add_count)
	sub_count = subtraction(words)
	print(sub_count)

	if(add_count > sub_count):
		operation = '+'
	else:
		operation = '-'

	for word in words:
		try: 
			num = int(word)
			numbers.append(str(num))
		except(ValueError):
			pass

	print(numbers)
	for a in range(len(numbers)):
		if(a == len(numbers)-1):
			arithmetic += numbers[a]
		else:
			arithmetic += numbers[a]
			arithmetic += operation

	return arithmetic

problem_input = input("Give me a problem: ")
print()

problem = problem_input.split()

findNumbers()
print()
findOperators()

# arithmetic = convert(problem)
# print()
# print("In arithmetic:")
# print(arithmetic)



