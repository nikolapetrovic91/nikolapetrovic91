def merge(l1, left_index, middle_index, right_index):
    list1 = l1[left_index : middle_index + 1]
    n1 = len(list1)
    list2 = l1[middle_index + 1 : right_index+1]
    n2 = len(list2)
    i = 0
    j = 0
    k = left_index
    while i < n1 and j < n2:
        if list1[i] < list2[j]:
            l1[k] = list1[i]
            i += 1
        else:
            l1[k] = list2[j]
            j += 1
        k += 1
    
    while i < n1:
        l1[k] = list1[i]
        i += 1
        k += 1
    while j < n2:
        l1[k] = list2[j]
        j += 1
        k += 1

def merge_sort(s1, left_index, right_index):
    if left_index < right_index:
        middle_index = (left_index + right_index) // 2
        merge_sort(s1, left_index, middle_index)
        merge_sort(s1, middle_index + 1, right_index)
        merge(s1, left_index, middle_index, right_index)


s1 = [1, 5, 3, 8, 2, 10, 9, 4, 7, 6]
print(s1)
merge_sort(s1, 0 , len(s1)-1)
print(s1)