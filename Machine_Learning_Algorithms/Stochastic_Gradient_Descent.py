# stochastic gradient descent method for simple linear regression

# calculates the prediciton based on given coefficients
def predict(coef, row):
    return coef[0] + row[0]*coef[1]

# stochastic gradient descent implemented, returns the coeefficients
def determine_coef_gd(dataset, l_rate, epoch, coef_0):
    for n in range(epoch+1):
        sq_error = 0
        for row in dataset:
            error = row[1] - predict(coef_0, row)
            coef_0[0] = coef_0[0] + l_rate * error
            coef_0[1] = coef_0[1] + l_rate * error * row[0]
        for row in dataset:
            sq_error += (row[1]-predict(coef_0, row))**2
    print(f"for n={n}, squarred error is equal {sq_error}")
    return [coef_0]

#initialize dataset, learning rate, starting point and the condition on gradient (gradient equal 0 in local extremum)
dataset = [[1,1],[2,3],[4,3],[3,2],[5,5]]
l_rate = 0.00001
epoch = 10000000
coef_0 = [0,0]

coef_gd = determine_coef_gd(dataset, l_rate, epoch, coef_0)
print(f"the resulting coefficients are: {coef_gd}")
for row in dataset:
    yhat = predict(coef_0, row)
    print(f"expected: {row[1]} and predicted: {yhat}")