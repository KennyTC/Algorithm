# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

def ValidParenthesis(s):
    if len(s) % 2 == 1:
        return False
    s=s.replace("(",")").replace("{","}").replace("[","]")
    mid=int(len(s)/2)
    firsthalf = s[:mid][::-1]
    secondhaft = s[mid:]
    if firsthalf == secondhaft:
        return True
    else:
        return False


print(ValidParenthesis("()"))