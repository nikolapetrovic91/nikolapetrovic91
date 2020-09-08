from math import sqrt


#Euclidean distance between two points
def euclidean_distance(x,y):
    sq_dist = 0
    for i in range(len(x)):
        sq_dist = sq_dist + (x[i]-y[i])**2
    return sqrt(sq_dist)

#Calculate the distance between one particular point and each of the points from the dataset, and returing the list sorted by distance
def euclidean_distance_n(x, dataset):
    distances = []
    for i in range(len(dataset)):
        d = euclidean_distance(x, dataset[i][:len(dataset[i])-1])
        distances.append([d, dataset[i][-1]])
        distances.sort()
    return distances

#for specified number of neighbours, it returns the k neighbours closest to the given point
def predict(x, dataset, k):
    distances = euclidean_distance_n(x, dataset)
    relevant = distances[:k]
    values = [row[1] for row in relevant]
    distances = [row[0] for row in relevant]
    count = {item: values.count(item) for item in values}
    highest = max(count.values())
    for a, b in count.items():
        if b == highest:
            return a

x = [7,8]

dataset = [[2.7810836,2.550537003,0],
    [1.465489372,2.362125076,0],
    [3.396561688,4.400293529,0],
    [1.38807019,1.850220317,0],
    [3.06407232,3.005305973,0],
    [7.627531214,2.759262235,1],
    [5.332441248,2.088626775,1],
    [6.922596716,1.77106367,1],
    [8.675418651,-0.242068655,1],
    [7.673756466,3.508563011,1]]

prediction = predict(x, dataset, 6)
print(prediction)
