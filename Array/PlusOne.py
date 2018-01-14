# Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
#
# You may assume the integer do not contain any leading zero, except the number 0 itself.
#
# The digits are stored such that the most significant digit is at the head of the list.
##################################################################################################################
def PlusOne(digits):
    digits = list(map(lambda x: str(x), digits))
    plused = int("".join(digits)) + 1
    newdigits = list(str(plused))
    newdigits = list(map(lambda x: int(x), newdigits))
    sorted(newdigits)
    return newdigits

##################################################################################################################
# 2. The above needs to convert from int to string a lot. We will avoid this.
# Idea is to loop from the back. Just like we plus in normal way.
def PlusOne2(digits):
    for i in range(len(digits) - 1, -1, -1):  # from end to beginning
        if digits[i] != 9:
            digits[i] += 1  #
            break
        digits[i] = 0
    # Khac voi doan code duoi day. O doan code tren, neu plus 1 thanh cong, ta exit khoi vong for luon. Con doan code duoi,
    # ta van tiep tuc so sanh tiep, nen bi sai
    #     if digits[i] == 9:
    #         digits[i] = 0
    #     else:
    #         digits[i] += 1
    # print(digits)
    if digits[0] == 0:  # if the first number is 0, co nghia la so dang sau no luc nay la so 9, vi vay , we have to insert 1 at the position 0
        digits.insert(0, 1)
    return digits


print(PlusOne2([2,1,9]))
##################################################################################################################
# 3. Similarly, we do minus one
def MinusOne(digits):
    for i in range(len(digits) - 1, -1, -1):  # from end to beginning
        if digits[i] != 0:
            digits[i] -= 1  #
            break
        digits[i] = 9
    return digits


digit = [2, 1, 0]
print(MinusOne(digit))
