#arithmetic classifier
import numpy as np
from sklearn import preprocessing

np.random.seed(1)

#activation fns
def sigmoid(X):
	return 1/(1+np.exp(-X))

def sigmoid_deriv(output):
	return output*(1-output)

