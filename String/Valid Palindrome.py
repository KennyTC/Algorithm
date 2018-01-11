import re
def ValidPalindrome(s):
    s = re.sub("[^a-zA-Z0-9]","",str.lower(s))
    s1=s[::-1] # list(reversed(s))
    if s==s1:
        return True
    else:
        return False
    #
    # for i in range(len(s)):
    #     if s[i]!=s1[i]:
    #         return False
    # return True

print(ValidPalindrome("A man, a plan, a canal: Panama"))