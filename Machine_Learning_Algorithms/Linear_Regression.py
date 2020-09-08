# gradient descent method for simple linear regression

# calculates prediciton for given coefficients
def predict(coef, row):
    return coef[0] + row[0]*coef[1]

# gradient descent implemented in the function, returns the coefficients
def determine_coef_gd(dataset, l_rate, cond, coef_0):
    error = 10
    # n introduced to avoid infinite loop
    n=0
    while abs(2 * error) > cond:
        error = 0
        for row in dataset:
            error += (row[1] - predict(coef_0, row))
        coef_0[0] = coef_0[0] + l_rate * error
        coef_0[1] = coef_0[1] + l_rate * error * row[0]
        n += 1
        if n == 100000:
            print("gradient not yet close enough to 0")
            return [error,coef_0]
    return [error, coef_0]

#initialize dataset, learning rate, starting point and the condition on gradient (gradient equal 0 in local extremum)
dataset = [[1,1],[2,3],[4,3],[3,2],[5,5]]
l_rate = 0.001
cond = 0.00000001
coef_0 = [0,0]

coef_gd = determine_coef_gd(dataset, l_rate, cond, coef_0)
print(coef_gd)
for row in dataset:
    yhat = predict(coef_0, row)
    print(f"expected: {row[1]} and predicted: {yhat}")