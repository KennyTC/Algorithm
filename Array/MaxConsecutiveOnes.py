# Given a binary array, find the maximum number of consecutive 1s in this array.
#
# Example 1:
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#     The maximum number of consecutive 1s is 3.
########################################################################################################################
def MaxConsecutiveOnes(s):
    i, maxlength = 0, 0
    while (i < len(s)):
        count = 0  # to count number of ones
        while i < len(s) and s[i] == 1: # để tránh out of range of s
            count += 1
            i = i + 1
        maxlength = max(maxlength, count)
        i=i+1
    print(maxlength)
    return maxlength

# print(MaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
# print(MaxConsecutiveOnes([1,1,1,1,0,0,0,0,1,1]))

# điểm đặc biệt là:
# * Chỉ sử dụng i cho cả while vòng trong và vòng ngoài
# * Check điều kiện i < len(s) ở cả 2 vòng while

# Phương pháp này chỉ là O(n) bởi tuy là 2 vòng while lồng nhau nhưng thực chất với mỗi phần tử, ta chỉ duyệt qua một lần
########################################################################################################################
# 2. Ta duyệt toàn bộ list, cứ gặp 0 thì ta reset count. Còn cứ gặp 1 thì count tăng 1

def MaxConsecutiveOnes2(s):
    count, maxlength=0,0
    for i in s:
        if i==1:
            count+=1
            maxlength=max(maxlength,count)
        else:
            count=0
    return maxlength

print(MaxConsecutiveOnes2([1, 1, 0, 1, 1, 1]))
print(MaxConsecutiveOnes2([1,1,1,1,0,0,0,0,1,1]))