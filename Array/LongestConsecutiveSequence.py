
def LongestConsecutive1(a):
    a = sorted(a)
    print(a)
    l = 1
    i = 0
    while (i < len(a) - 1):
        base = a[i]
        print("base", base, ",a[", i, "]=", a[i])
        k = 0
        while (base == a[i] and i < len(a) - 1):
            k = k + 1
            i = i + 1
            base = base + 1
            print("a[", i, "]=", a[i])
        if k > l:
            l = k
        print("k=", k)
    return l


# --> O(n2)
###############################################################################################3
# 2. Brute force search, means find all possible algorithms and test
def LongestConsecutive2(a):
    max = 1
    for i in a:  # O(n)
        counter = 1
        value = i + 1
        while (value in a):  # search O(n)
            counter += 1
            value += 1  # O(n)
        print("counter", counter)
        if counter > max:
            max = counter
    return max


# --> O(n^3)
###################################################################################################
# 3. Sort first. The idea is like 1 but to compare btw numbers are better
def LongestConsecutive3(a):
    if not a:  # len(a) == 0:
        return 0
    a = sorted(a)  # O(nlogn)
    print(a)
    counter = 1
    longest = 1
    for i in range(0, len(a) - 1):  # O(n)
        if a[i] == a[i + 1] - 1:
            counter = counter + 1
        else:
            longest = max(counter, longest)  # assign counter to max,
            counter = 1  # reset counter to 1, start counting a new chain
        print("counter=", counter)
    return longest
# this method will O(nlogn) due to the Sort. The space complexity will be O(1): if the Sort the array in place.
# if the array is required not to change --> we need to copy to another array, then O(n)
#####################################################################################################
# 4. To optimize 2. We do not need to start from every element of array. We just need to start from elements beginning of the
# array. We do it by checking its preceding number in the array or not, and we use Set in python to look --> O(1).

def LongestConsecutive4(a):
    longest = 0
    print("a=", a)
    num_set = set(a)
    print("num_set=", num_set)
    for num in num_set:
        if num - 1 not in num_set:  # begin with the smallest number of each chain. Note that look up in set() will be O(1)
            current_num = num  # while loop just run whenever current_num is assigned. And current_num  is assigned at most n times because we just assign current_num a different num each loop.
            print("start:", current_num)
            current_streak = 1
            while current_num + 1 in num_set:  # overal run of while is linearly proportional to overal run of current_num
                current_num += 1
                print(current_num)
                current_streak += 1
            longest = max(longest, current_streak)
    return longest


# --> Good way

print(LongestConsecutive4([1, 3, 2, 2, 4, 5, 5, 11, 10, 12, 12, 18, 21, 22]))
