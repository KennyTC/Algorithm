#####################################################################################
# Merge sort 1
#####################################################################################
def Sort(num):
    if (len(num) <= 1):
        return num
    else:
        middle = len(num) // 2
        left = num[:middle]
        right = num[middle:]
        sleft = Sort(left)
        sright = Sort(right)
        return Merge(sleft, sright)

# buoc hop lai
def Merge(sleft, sright):
    s = []
    while (len(sleft) != 0 and len(sright) != 0):
        if (sleft[0] <= sright[0]):
            s.append(sleft[0])
            sleft.remove(sleft[0])
        else:
            s.append(sright[0])
            sright.remove(sright[0])
    if len(sleft)>0:
        s.extend(sleft)
    else:
        s.extend(sright)
    return s

#print(FindMedian([1,2,3,43,3,2,32,23],[1,2,22,2325,76,787]))

#####################################################################################
# Merge sort 2
#####################################################################################

def mergeSort(l):
    print("Splitting ", l)
    if len(l)>1:
        mid = len(l) // 2
        lefthalf = l[:mid]
        righthalf = l[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        # dung k boi vi chung ta se ghi de len phan tu cua l(list) luon. Neu khong dung k thi list se bi lap lai.
        # boi vi chung ta ko tao list moi de chua phan tu da sap xep, ma chung ta su dung luon list cu.
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                l[k]=lefthalf[i]
                i=i+1
            else:
                l[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            l[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            l[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ", l)


#####################################################################################
# Merge sort 3: Dung nhu the nay se bi lap
#####################################################################################
def mergeSort3(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist.append(lefthalf[i])
                i=i+1
            else:
                alist.append(righthalf[j])
                j=j+1
        while i < len(lefthalf):
            alist.append(lefthalf[i])
            i=i+1

        while j < len(righthalf):
            alist.append(righthalf[j])
            j=j+1
    return alist

#print(mergeSort3([1,2,3,43,3])) -->
