#addition subtraction 
import nltk
from nltk.corpus import wordnet as wn

#keywords (nltk soon)
addwords = ['gets','get','more','add','adds','got','added','received','gives','receives']
subwords = ['gave','lost','away','takes','take', 'took','taking','losing','loses']

multwords = ["each"]
operation = ''
operators = []
numbers = []
problem = []



#SANDBOX

starter = ['add', 'get', 'receive']
for word in starter:
	for syn in wn.synsets(word, pos=wn.VERB):
		print()
		print(syn.definition())
		print("synonyms")
		print(syn.hypernyms())

#########






def findNumbers():
	for word in problem:
		try: 
			num = int(word)
			numbers.append(str(num))
		except(ValueError):
			pass
	print("numbers in problem (in order):")
	print(numbers)

#finds operators in problem statement (+ or -)
def findAddSumOperators():
	init_index = 0
	end_index = 0

	for i in range(len(problem)-1):
		for num in numbers:
			if(problem[i] == num):
				init_index = i
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
				if(first == last):
					break
				addnum = 0
				subnum = 0
				while(first < last):
					for key in addwords:
						if(problem[first].lower() == key):
							addnum+=1
					for key in subwords:
						if(problem[first].lower() == key):
							subnum+=1
					first+=1
				if(addnum > subnum):
					operators.append('+')
				else:
					operators.append('-')
			pass

	print()
	print("problem operators (in order):")
	print(operators)

#test
problem_input = input("Give me a problem: ")
print()

problem = problem_input.split()

findNumbers()
print()
findAddSumOperators()




