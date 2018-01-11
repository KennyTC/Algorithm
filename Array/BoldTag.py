def boldTag(s, list):
    # add to list
    l = []  # add a temp list
    for item in list:
        found = s.find(item)
        if found != -1:  # found this in s
            if (found, found + len(item) - 1) not in l:
                l.append((found, found + len(item) - 1))
    # sort the first item of
    l = sorted(l, key=lambda index: index[0])  # each item is a tuple(i,j), nên index[0] là phần tử đầu tiên của tuple
    ret = ""
    i = 0
    end = 0
    while (i < len(l) - 1):  # loop the nay ta moi co the tac dong vao i
        start = l[i][0]
        end = l[i][1]
        while (i < len(l) - 1 and l[i + 1][
            0] <= end + 1):  # so sanh so cuoi cùng của range này với số đầu tiên của range tiếp theo
            # nếu bé hơn thì merge. Sau đó ta phải tăng i lên, để tránh vòng while bên ngoài lặp lại phần tử này
            end = max(end, l[i + 1][1])
            i = i + 1
        ret = ret + "<b>{}</b>".format(s[start:end + 1])
    ret = ret + s[end + 1:len(s) + 1]
    print(ret)
    return ret


# print(boldTag("aaabbcc", ["aaa", "aab", "bc"]))


################################################################
# 2.
def boldTag2(s, list):
    s1 = []
    for i in range(len(s)):
        s1.append("F")
    for i in list: # O(len(list))
        found = s.find(i) # O(len(s))
        if found != -1:  # i is found in s
            s1[found:found + len(i)] = "T"*len(i)# the way to assign value to a range in list
    ret = []
    i = 0
    while (i < len(s1)):
        if s1[i] == "T":
            ret.append("<b>")
            while (i < len(s1) and s1[i] == "T"):
                ret.append(s[i])
                i = i + 1
            ret.append("</b>")
        else:  # F
            ret.append(s[i])
            i = i+ 1
    #print(ret)
    return "".join(ret)

print(boldTag2("aaabbcc", ["aaa", "aab", "bc"]))
print(boldTag2("abcxyz123", ["abc","123"]))
# O(len(list)*len(s)) time,
# O(s) space
###############################################