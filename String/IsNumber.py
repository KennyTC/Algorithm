import re
def isNumber(s):
    #result = re.compile("([\d]?[^(a-zA-Z^(e,E))][\d]?)").match(s) is OK
    result = re.compile("([\d]?[e,E]?[\d]?)").match(s)
    if result == None:
        return False
    else:
        return True

print(isNumber("2e10"))