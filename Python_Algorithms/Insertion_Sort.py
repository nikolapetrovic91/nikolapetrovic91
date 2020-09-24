def insertion_sort(list1):
    for i in range(1, len(list1)):
        j = i
        value = list1[i]
        while j > 0:
            if list1[j-1] > value:
                temp = list1[j-1]
                list1[j-1] = list1[j]
                list1[j] = temp
            j -= 1


list1 =[5, 3, 6, 4, 10, 7, 9, 8, 2, 1]
print(list1)
insertion_sort(list1)
print(list1)