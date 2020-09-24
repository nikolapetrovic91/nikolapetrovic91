def selection_sort(list1):
    for i in range(0, len(list1)):
        minimum = list1[i]
        index = i
        changed = False
        for j in range(i+1, len(list1)):
            if list1[j] < minimum:
                minimum = list1[j]
                index = j
                changed = True
        if changed == True:
            temp = list1[i]
            list1[i] = list1[index]
            list1[index] = temp

list1 = [6, 5, 4, 3, 9, 8, 7, 2, 1]
print(list1)
selection_sort(list1)
print(list1)
        