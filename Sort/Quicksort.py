def Sort(a):
    QuickSort(a, 0, len(a) - 1)
    return a


def QuickSort(a, start, end):
    if start < end:
        splitpoint = Partition(a, start, end)
        QuickSort(a, start, splitpoint - 1)
        QuickSort(a, splitpoint + 1, end)
    return a


def Partition(a, start, end):
    pivot = a[start]
    left, right = start + 1, end
    done = False
    while not done:
        while (left <= right and a[left] <= pivot):
            left = left + 1
        while (left <= right and a[right] >= pivot):
            right = right - 1
        if (right < left):
            done = True
        else:
            a[left], a[right] = a[right], a[left]
    a[right], a[start] = a[start], a[right]
    return right


def Partition(a, start, end):
    pivot = a[end]
    left, right = start, end - 1
    done = False
    while not done:
        while (left <= right and a[left] <= pivot):
            left = left + 1
        while (left <= right and a[right] >= pivot):
            right = right - 1
        if (right < left):
            done = True
        else:
            a[left], a[right] = a[right], a[left]
    a[left], a[end] = a[end], a[left]
    return left

#################################################################################
# Chi su dung 1 function
#################################################################################
# def Quicksort2(x):
#     if len(x) == 1 or len(x) == 0:
#         return x
#     else:
#         pivot = x[0]
#         i = 0
#         for j in range(len(x) - 1):
#             if x[j + 1] < pivot:
#                 x[j + 1], x[i + 1] = x[i + 1], x[j + 1]
#                 i += 1
#         x[0], x[i] = x[i], x[0]
#         print(x)
#         first_part = Quicksort2(x[:i])
#         second_part = Quicksort2(x[i + 1:])
#         first_part.append(x[i])
#         return first_part + second_part

def Quicksort2(a):
    if len(a) == 1 or len(a) == 0:
        return a
    else:
        print("Array=", a, "Choose pivot=", a[0])
        pivot = a[0]
        i = 0
        for j in range(1, len(a)):
            if a[j] < pivot:
                i = i + 1
                print("Change", a[j], "vs", a[i])
                a[j], a[i] = a[i], a[j]
                print("After change -->", a)
        print("Now. Change ", a[i], "vs pivot", a[0])
        a[0], a[i] = a[i], a[0]
        print(" -->", a)
        print("--------------------------")
        first_part = Quicksort2(a[:i])
        second_part = Quicksort2(a[i + 1:])
        first_part.append(a[i])
        return first_part + second_part


# alist = [3, 7, 5, 9, 2, 1, 5,12,34,33,12,687,89]
# print(Quicksort2(alist))

# print(quicksort(alist))

