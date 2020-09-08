import numpy as np

# sigmoid function used as activation function
def sigmoid(x):
    return 1/(1+np.exp(-x))

# derivative of the sigmoid function, needed for gradient
def sigmoid_der(x):
    return sigmoid(x)*(1-sigmoid(x))

# prediction function, for specified parameters
def predict(x, weights, bias):
    return sigmoid(np.dot(x, weights) + bias)

train_set = np.array([[0,1,0],[0,0,1],[1,0,0],[1,1,0],[1,1,1]])
labels = np.array([[1,0,0,1,1]])
labels = labels.reshape(5,1)

# We fix the seed for the pseudo random generator so as that we can replicate the result each time
np.random.seed(42)
weights = np.random.rand(3,1)
bias = np.random.rand(1)
rate = 0.05

# training the algorithm, ie implemented gradient descent, giving parameters
for epoch in range(20000):
    inputs = train_set
    # we calculate prediction based on current weights and bias, in this case 3-dim vector 
    z = predict(train_set, weights, bias)
    # we calculate error term, ie difference between predicted and real values
    error = z - labels

    # gradient part
    error_term = error
    sigm_term = sigmoid_der(z)

    sigm_error = sigm_term * error_term
    inputs = train_set.T
    weights -= rate * np.dot(inputs, sigm_error)
    
    # formula for bias will be different than for weights, follows from the derivation
    for num in sigm_error:
        bias -= rate * num
        
#print(weights)
#print(bias)
print(predict([1,0,0],weights,bias))