import nltk
import numpy as np 
from sklearn import preprocessing
#operation learner (based on action-learn)

#something that can look at arithmetic problems and answer and determine
#answers independently

np.random.seed(1)

#activation fns
def sigmoid(X):
	return 1/(1+np.exp(-X))

def sigmoid_deriv(output):
	return output*(1-output)

#dataset (soon this should be a database)
inputs = []
outputs = []

def new_word(input):
	for word in inputs:
		if(word == input):
			return False
	return True

def add_data(input, output):
	# if(new_word(input)):
	inputs.append(input)
	outputs.append(output)
	print("command added!")
	# else:
	# 	print("command already exists!")

def collection():
	#test/collection
	new_input = "placeholder"
	while(new_input != ''):
		new_input = input("Tell me something: ")
		if(new_input != ''):
			action_space = input("What should say now? ")
			add_data(new_input, action_space)

def encode_inputs(inputs, decode=False, input_data=None):
	try:
		input_encode = preprocessing.LabelEncoder()
		input_encode.fit(inputs)
		if(decode):
			return input_encode.inverse_transform(input_data)
		return input_encode.transform(inputs)
	except(IndexError, ValueError):
		print("well. shoot. encoding didn't work.")

def encode_outputs(outputs, decode=False, output_data=None):
	try:
		output_encode = preprocessing.LabelEncoder()
		output_encode.fit(outputs)
		if(decode):
			return output_encode.inverse_transform(output_data)
		return output_encode.transform(outputs)
	except(IndexError, ValueError):
		print("well. shoot. encoding didn't work.")

collection()
# print("COMMMANDS:")
# print(inputs)
# print("CORRESPONDENCE:")
# print(outputs)
# print()

encoded_inputs = encode_inputs(inputs)
encoded_outputs = encode_outputs(outputs)
scale_divisor = len(encoded_outputs)

#TRAINING SET
input_data = np.array([encoded_inputs]).T
output_data = np.array([encoded_outputs]).T

# print(input_data)
# print()
# print(output_data)
#print("rescaled output data:")
output_data = output_data/scale_divisor
# print(output_data)
# print()

syn0 = 2*np.random.random((1,4))-1
syn1 = 2*np.random.random((4,4))-1
syn2 = 2*np.random.random((4,1))-1 #output layer

def train(epochs, syn0, syn1, syn2, input_data, output_data):

	for iter in range(epochs):
		l0 = input_data

		l1 = sigmoid(np.dot(l0, syn0))
		l2 = sigmoid(np.dot(l1, syn1))
		l3 = sigmoid(np.dot(l2, syn2)) #output prediction

		#output error and delta rule 
		l3_error = output_data - l3
		l3_delta = l3_error * sigmoid_deriv(l3)

		#error contributions from hidden layers and deltas "error signal"
		l2_error = np.dot(l3_delta, syn2.T)
		l2_delta = l2_error * sigmoid_deriv(l2)

		l1_error = np.dot(l2_delta, syn1.T)
		l1_delta = l1_error * sigmoid_deriv(l1)

		#adjustments 
		syn0_adjustment = np.dot(l0.T, l1_delta)
		syn1_adjustment = np.dot(l1.T, l2_delta)
		syn2_adjustment = np.dot(l2.T, l3_delta)

		#update weights
		syn0 += syn0_adjustment
		syn1 += syn1_adjustment
		syn2 += syn2_adjustment

		if (iter % 1000 == 0):
			print()
			# print ("layer one error after %s iterations: %s" % 
			# 	(iter, str(np.mean(np.abs(l1_error)))))
			# print ("layer two error after %s iterations: %s" % 
			# 	(iter, str(np.mean(np.abs(l2_error)))))
			print ("output layer error after %s iterations: %s" % 
				(iter, str(np.mean(np.abs(l3_error)))))

	return l3

def predict(syn0, syn1, syn2, input_data):
	l0 = input_data
	l1 = sigmoid(np.dot(l0, syn0))
	l2 = sigmoid(np.dot(l1, syn1))
	l3 = sigmoid(np.dot(l2, syn2))
	return l3

results = train(100000, syn0, syn1, syn2, input_data, output_data)
prtpred = results * scale_divisor
rounded_pred = np.around(prtpred, 1)

decoded_inputs = encode_inputs(inputs, True, input_data)

to_decode_out = rounded_pred.astype(int)
decoded_outputs = encode_outputs(outputs, True, to_decode_out)

print()
print("NUMERICAL RESULTS")
print(rounded_pred)

print()
print("DECODED INPUTS:")
print(decoded_inputs)


print()
print("DECODED OUTPUTS:")
print(decoded_outputs)



print()
print("PREDICTION PHASE:")

pred_input = "placeholder"
while(pred_input != ''):

	pred_input = input("Tell me something: ")
	if(pred_input != ''):
		input_encode = preprocessing.LabelEncoder()
		input_encode.fit(inputs)
		X = input_encode.transform([pred_input]) 

		#print(X)
		prediction = predict(syn0, syn1, syn2, [X])
		#print(prediction * scale_divisor)
		rounded_result = np.around(prediction * scale_divisor, 1)

		result = rounded_result.astype(int)
		#print(result)
		final_result = encode_outputs(outputs, True, result)
		print()
		print("based on your command, here's my action prediction:")
		print(final_result)
	print()