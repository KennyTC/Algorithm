# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
# Note:
# Have you consider that the string might be empty? This is a good question to ask during an interview.
# For the purpose of this problem, we define empty string as valid palindrome.
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