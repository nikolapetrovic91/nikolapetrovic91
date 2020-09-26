def quick_sort(list1):
    if len(list1) < 2:
        return list1
    else:
        pivot = list1.pop()
        items_bigger = []
        items_smaller = []
        for item in list1:
            if item <= pivot:
                items_smaller.append(item)
            else:
                items_bigger.append(item)
        return quick_sort(items_smaller) + [pivot] + quick_sort(items_bigger)


list1 = [3, 4, 2, 6, 8, 7, 5, 1, 10, 9]
print(list1)
list1 = quick_sort(list1)
print(list1)