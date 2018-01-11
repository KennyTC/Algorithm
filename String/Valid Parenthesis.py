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