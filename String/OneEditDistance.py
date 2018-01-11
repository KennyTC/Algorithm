# Python program to check if given two strings are
# at distance one

# Returns true if edit distance between s1 and s2 is
# one, else false
def isEditDistanceOne(s1, s2):
    # Find lengths of given strings
    m = len(s1)
    n = len(s2)

    # If difference between lengths is more than 1, then strings can't be at one distance
    if abs(m - n) > 1:
        return False
    count = 0  # Count of isEditDistanceOne
    i = 0
    j = 0
    while i < m and j < n:
        # If current characters dont match
        if s1[i] != s2[j]:
            if count == 1:
                return False

            # If length of one string is more, then only possible edit is to remove a character
            if m > n:
                i += 1
            elif m < n:
                j += 1
            else:  # If lengths of both strings is same
                i += 1
                j += 1

            # Increment count of edits
            count += 1

        else:  # if current characters match
            i += 1
            j += 1

    # if last character is extra in any string
    if i < m or j < n:
        count += 1

    return count == 1

#print(isEditDistanceOne("geek","seek"))
#################################################3
# 2. Idea: Bởi chỉ khác nhau một character nên, nếu như ta thấy 1 chỗ khác nhau rồi, thì đoạn còn lại chắc chắn phải giống nhau.
# Ta loop cả 2 string đồng thời, nếu có một chỗ khác nhau thì ta so sánh đoạn string còn lại, tính từ chỗ khác nhau đó.
# Nhưng đoạn loop này ko xử lý đc 2 trings giống nhau y hệt đoạn đầu, vd goose - goosekkkkks, nên ta phải xử lý thêm ở đoạn return
def isEditDinstanceOne2(s1,s2):
    minlength = min(len(s1), len(s2))
    for i in range(minlength):
        if s1[i]!=s2[i]: # neu s1 va s2 giong nhau het o phan dau, vd goose va goosekkkkks thi doan code nay se ko dc chay
            if len(s1)==len(s2):
                return s1[i+1:]==s2[i+1:]
            elif len(s1)<len(s2):# s2> s1
                return s2[i+1:]==s1[i:]
            else: # s1 > s2
                  return s1[i+1:]==s2[i:]
    return abs(len(s1)-len(s2))==1

print(isEditDinstanceOne2("gfg","gfkm"))