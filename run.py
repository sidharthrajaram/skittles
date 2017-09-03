#runtime
addwords = ['gets','get','more','add','adds','got','added','received']
subwords = ['gave','lost','away','takes']
add_count = 0
sub_count = 0
operation = ''
operators = []
numbers = []

def findOperators(problem):
	pass

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

problem = input("Give me a problem: ")
print(problem)
print()

arithmetic = convert(problem)
print()
print("In arithmetic:")
print(arithmetic)

