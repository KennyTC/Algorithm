# Brute force
# length of string is n --> n*(n+1)/2 possible substrings.
# A simple way is to generate all the substring and check each one whether it has exactly k unique characters or not.
# it would take O(n2) to generate all substrings and O(n) to do a check on each one. Thus overall it would go O(n3)
#-------------------------------------------------------------------------------------------------------------------
# Idea: Ban đầu dùng toàn bộ string. Kiểm tra có số lượng k distint phần tử hay ko. Nếu ko thỏa mãn thì loại bỏ từng
# phần tử của string một. Tới khi thỏa mãn <k là OK
def lengthOfLongestSubstringKDistinct(s, k):
    largestLength = 0
    n = len(s)
    found = False
    while (n > 0) and (n <= len(s)) and not found:
        for i in range(len(s) - n + 1):
            if len(set(s[i:i + n])) <= k:
                print("s[i:i + n]:{}".format(s[i:i + n]))
                largestLength = len(s[i:i + n])
                found = True
                break
        n = n - 1
    return largestLength


print(lengthOfLongestSubstringKDistinct("eceba", 2))
########################################################################################################################
# 2.
# Use dictionary d to keep track of (character, location) pair,
# where location is the rightmost location that the character appears at.
# Dic d dong vai tro la sliding window. keys của dict là chỉ có 2 characters, còn values của dict là index phải nhất của những kí tự đó.
# Nếu dict > k phần tử, thì ta phải loại 1 phần tử đi (phần tử trái nhất sẽ bị loại), và ta di chuyển đến phần tử trái nhất tiếp theo.
# low là index của phần tử trái nhất(mà chưa bị xóa), i là phần tử hiện tại --> từ phần tử low tới phần tử i đều xuất hiện trong dict.
# Thế nên số lượng sẽ là i-low +1
def lengthOfLongestSubstringKDistinct2(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    d = {}
    low, ret = 0, 0
    for i, c in enumerate(s):
        d[c] = i
        print(d)
        if len(d) > k:
            low = min(d.values())
            del d[s[low]]
            low += 1 # low +1 boi vi de sliding window di chuyen ve phia truoc
        ret = max(i - low + 1, ret)
    return ret

########################################################################################################################
# 3. Tuong tu nhu tren, nhung o day thay vi tim min, thi ta pop phan tu dau tien ra
def lengthOfLongestSubstringKDistinct3(s, k):
     d, start, res = dict(), 0, 0
     for i, c in enumerate(s):
          d[c] = i
          while len(d) > k:
              if d[s[start]] == start:
                  d.pop(s[start])
              start += 1
          res = max(res, i - start + 1)
     return res


print(lengthOfLongestSubstringKDistinct2("bawece", 2))
