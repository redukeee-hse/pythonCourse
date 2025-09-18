def PtrSort(arr):
    n = len(arr)
    ptr1 = 0
    ptr2 = len(arr) - 1
    b = [0] * n

    while ptr1 <= ptr2:
        if abs(arr[ptr1]) > abs(arr[ptr2]):
            b[ptr2 - ptr1] = abs(arr[ptr1])
            ptr1 += 1
        else:
            b[ptr2 - ptr1] = abs(arr[ptr2])
            ptr2 -= 1
    return b


print(PtrSort([-3, -2, 0, 1, 3, 5]))
print(PtrSort([6]))
print(PtrSort([-5, -4, -3, -2, 1]))
print(PtrSort([-5, 0, 3, 3, 5, 10]))
print(PtrSort([]))
