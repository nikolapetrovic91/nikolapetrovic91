def linear_search(list1, value):
    for i in range(len(list1)):
        if list1[i] == value:
            return i
    return -1


def binary_search(list1, left_index, right_index, value):
    mid_index = (left_index + right_index) // 2
    mid_number = list1[mid_index]
    if (left_index >= right_index):
        return -1
    if mid_number == value:
        return mid_index
    elif mid_number < value:
        return binary_search(list1, mid_index+1, right_index, value)
    elif mid_number > value: 
        return binary_search(list1, left_index, mid_index-1, value)


list1 = [1,2,5,7,9,10,12,14,17,22,33,55,78,89]
print(linear_search(list1, 17))
print(binary_search(list1, 0, len(list1)-1, 17))
