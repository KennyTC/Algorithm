def LisenseKeyFormat(s, K):
    s = str.upper(s).replace("-", "")
    print(s)
    remainder = len(s) % K
    s1 = ""
    if remainder != 0:
        s1 = s[:remainder]
        s1 = s1 + "-"
    i = remainder
    while (i + K <= len(s)):
        s1 = s1 + s[i:i + K] + "-"
        i = i + K
    print(s1)
    s1 = s1[:-1]
    print(s1)
    return s1


##############################################################
# improve

def LisenseKeyFormat2(S, K):
    S = str.upper(S).replace("-", "")
    remainder = len(S) % K
    s1 = S[:remainder]+"-" if remainder != 0 else ""
    i = remainder
    while (i < len(S)):
        s1 = s1 + S[i:i + K] + "-"  # i+ K has no problem of over index
        i = i + K
    print(s1)
    s1 = s1[:-1]
    print(s1)
    return s1


LisenseKeyFormat2("5F3Z-2e-9-w", 4)
LisenseKeyFormat2("2-5g-3-j", 2)
