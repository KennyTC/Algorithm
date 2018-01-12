def LongestStringWithoutRepeat(s):
    dict = {}
    start, end = 0, 0
    counter = 0
    ret = 0
    while (end < len(s)):
        if s[end] in dict.keys():
            counter = counter + 1
            dict[s[end]] +=1
        else:
            dict[s[end]] = 1
        end += 1

        while (counter > 0): # khi trong dict, ton tai 1 phan tu xuat hien 2 lan vd dict{a:2, b:1}, thi se nhay vao loop nay
            # exit khoi while, khi ta loai bo dc phan tu trung nhau. Nghia la trong dict chi co phan tu distinct
            if dict[s[start]] > 1:
                counter = counter - 1
            dict[s[start]] -= 1
            start = start + 1
        ret = max(ret, end - start)
    return ret

print(LongestStringWithoutRepeat("bcabcbb"))
#print(LongestStringWithoutRepeat("pwwkew"))
#print(LongestStringWithoutRepeat("bbbbb"))