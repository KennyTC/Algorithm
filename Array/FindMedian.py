# Finding median of an unsorted array. Median of an array được coi thành bài toán: chọn phần tử thứ n//2 của một unsorted array.

import random

##################################################################################################################################################################
# 1. Sử dụng quick select. Pivot được lựa chọn ngẫu nhiên (thường là đầu và cuối của array. Nhưng cái này ko tốt vì O(n^2) nếu là dãy sắp xếp.
# Ta cố gắng chọn pivot tốt hơn bằng deterministic selection, hay còn gọi là median of median
def QuickSelect(list):
    median = QuickSelectHelper(list,0,len(list)-1,len(list)//2+1)
    return median

def QuickSelectHelper(list, left, right, k):
    split = Partition(list,left,right)
    length = split-left+1
    if k < length:
        return QuickSelectHelper(list,left,split-1,k)
    elif k > length:
        return QuickSelectHelper(list,split+1,right,k-length)
    else: # lengh ==k
        return list[split]

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

########################################################################################################################################################################
# Quick Select có thể viết thành 1 function sử dụng recursion
def QuickSelect2(arr, n):
    pivot = arr[0]
    below = [x for x in arr if x < pivot]
    above = [x for x in arr if x > pivot]

    num_less = len(below)
    num_lessoreq = len(arr) - len(above)

    if n < num_less:
        return QuickSelect2(below, n)
    elif n >= num_lessoreq:
        return QuickSelect2(above, n-num_lessoreq)
    else:
        return pivot

#############################################################################################################################################
# Phương pháp median of median.
def select(L, j):
    if len(L) < 10:
        L.sort()
        return L[j]
    S = []
    lIndex = 0
    while lIndex + 5 < len(L) - 1:
        S.append(L[lIndex:lIndex + 5])
        lIndex += 5
    S.append(L[lIndex:])
    Meds = []
    for subList in S:
        Meds.append(select(subList, int((len(subList) - 1) / 2)))
    med = select(Meds, int((len(Meds) - 1) / 2))
    L1 = []
    L2 = []
    L3 = []
    for i in L:
        if i < med:
            L1.append(i)
        elif i > med:
            L3.append(i)
        else:
            L2.append(i)
    if j < len(L1):
        return select(L1, j)
    elif j < len(L2) + len(L1):
        return L2[0]
    else:
        return select(L3, j - len(L1) - len(L2))



# Duplicates can occur.
num = 10000
array = [random.randint(1, 1000) for i in range(num)]
random.shuffle(array)
random.shuffle(array)

# Get the value of the kth item.
k = 7
kval = select_random_pivot(array, k)

# Test it.
sorted_array = sorted(array)
assert sorted_array[k] == kval
