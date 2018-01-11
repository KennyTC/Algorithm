################################
# 1. Sort and then swap
def QuickSort(a):
    if len(a) == 0 or len(a) == 1:
        return a
    else:
        pivot = a[0]
        i = 0
        for j in range(1, len(a)):
            if a[j] < pivot:
                i = i + 1
                a[i], a[j] = a[j], a[i]
        # exchange with pivot
        a[0], a[i] = a[i], a[0]
        first_part = QuickSort(a[:i])
        second_part = QuickSort(a[i + 1:])
        first_part.append(a[i])
        return first_part + second_part

# neu len(a) la so le --> bat dau tu so cuoi cung cua array
# neu len(a) la so chan --> bat dau tu so cuoi cung -1
def WiggleSort1(a):
    print(a)
    i = 1
    j = len(a) - 2
    if (len(a) % 2 == 0):
        j = len(a) - 2
    else:
        j = len(a) - 1
    while (i < j):
        if (i % 2 == 1): #neu la o vi tri le
            print("exchange:", a[i], "vs", a[j])
            a[i], a[j] = a[j], a[i]
            print("-->", a)
        i = i + 1
        j = j - 1
    return a
#-----------------------------------------------------------------------------------------------------------------
##################################################################################################################
# 2.
# Doi voi nhung van de co tinh doi xung, ta the co nghi theo huong nay:
#    co 1 bien de xu ly voi nhung so odd, even
#
def WiggleSort2(a):
    less=True
    print(a)
    for i in range(len(a)-1):
        # for odd position:
        if less==True:
            if a[i]>a[i+1]: # if a[i] > so tiep theo --> doi
                print("change",a[i],"vs",a[i+1])
                a[i],a[i+1]=a[i+1],a[i]
                print("-->",a)
        else:# for even position
            if a[i]<a[i+1]: # if a[i] < so tiep theo --> doi
                print("change", a[i], "vs", a[i + 1])
                a[i], a[i+1] = a[i + 1], a[i]
                print("-->",a)
        less=not less
    return a
####################################################################3
# 3. Improve 2.
#########################
def WiggleSort3(a):
    for i in range(len(a)-1):
        if ((i%2==0) and (a[i]>a[i+1])) or ((i%2==1) and (a[i]<a[i+1])):
                print("change",a[i],"vs",a[i+1])
                a[i],a[i+1]=a[i+1],a[i]
                print("-->",a)
    return a


alist = [3, 7, 5, 9, 2, 1, 5, 89]
#a = QuickSort(alist)
#print(a)
print(WiggleSort1(alist))
