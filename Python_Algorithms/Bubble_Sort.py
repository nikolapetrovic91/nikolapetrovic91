def bubble_sort(s1):
    for i in range(len(s1)):
        swapped = False
        for j in range(len(s1)-1-i):
            if s1[j] > s1[j+1]:
                a = s1[j+1]
                s1[j+1] = s1[j]
                s1[j] = a
                swapped = True
        if swapped == False:
            break


s1 = [1, 5, 3, 8, 2, 10, 9, 4, 7, 6]
bubble_sort(s1)
print(s1)