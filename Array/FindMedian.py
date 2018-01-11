#####################################################################################
# Merge sort 1
#####################################################################################
def FindMedian(num1, num2):
    num = num1 + num2
    snum = Sort(num)
    print(snum)
    return snum[len(snum) // 2]

# buoc tach lam doi
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
