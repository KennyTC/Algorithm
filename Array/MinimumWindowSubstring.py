#######################################################################################################################
def MinimumWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    # Struggled with this problem for a long while.
    # Idea: Two pointers: moving end forward to find a valid window,
    #                     moving start forward to find a smaller window
    #                     counter and hash_map to determine if the window is valid or not
    # min_window_length contains minimum window length that satisfies conditions

    # Count the frequencies for chars in t
    hash_map = dict()
    for c in t:
        if c in hash_map:
            hash_map[c] += 1
        else:
            hash_map[c] = 1

    start, end = 0, 0

    # If the minimal length doesn't change, it means there's no valid window
    min_window_length = len(s) + 1

    # Start point of the minimal window
    min_window_start = 0

    # Works as a counter of how many chars still need to be included in a window
    num_of_chars_to_be_included = len(t)

    while end < len(s):
        # If the current char is desired
        if s[end] in hash_map:
            # Then we decreased the counter, if this char is a "must-have" now, in a sense of critical value
            if hash_map[s[end]] > 0:
                num_of_chars_to_be_included -= 1
            # And we decrease the hash_map value
            hash_map[s[end]] -= 1

        # valid window found. We increase "start" to find the minimum window
        while num_of_chars_to_be_included == 0:
            # See if this window is smaller
            if end - start + 1 < min_window_length:
                min_window_length = end - start + 1
                min_window_start = start

            # if s[start] is desired, we need to update the hash_map value and the counter
            if s[start] in hash_map:
                hash_map[s[start]] += 1
                # Still, update the counter only if the current char is "critical"
                if hash_map[s[start]] > 0:
                    num_of_chars_to_be_included += 1

            # Move start forward to find a smaller window
            start += 1

        # Move end forward to find another valid window
        end += 1

    if min_window_length == len(s) + 1:
        return ""
    else:
        return s[min_window_start:min_window_start + min_window_length]


############################################################################################
def MinimumWindow2(s, t):
    hash_map = dict()
    for c in t:
        if c in hash_map:
            hash_map[c] += 1
        else:
            hash_map[c] = 1
    start, end = 0, 0
    # min_window_start va min_window_length dung de luu tru ket qua cuoi cung. Neu ta chi dung start va end thi ko chinh xac, boi vi
    # start, end thay doi lien tuc.
    min_window_length = len(s)+1
    # min_window_length= len(s) thi se gap van de:
    #   + Gia su s=aa, t=aa --> ket qua tra ve la "", nhung dang le ra ket qua phai la aa
    #   + Vi vay, min_window_length= len(s) + 1 de tranh truong hop nay
    min_window_start = 0
    num_of_chars_to_be_included = len(t)

    while end < len(s):
        if s[end] in hash_map:
            if hash_map[s[end]] > 0:
                num_of_chars_to_be_included -= 1
                #num_of_chars_to_be_included se giam cho toi khi =0, khi no bang 0 nghia la cac character can thiet da tim thay.
                # Ta bat dau chay den while de toi uu string
            hash_map[s[end]] -= 1
        while num_of_chars_to_be_included == 0:
            if len(s[start:end + 1]) < min_window_length:
                min_window_length = len(s[start:end + 1])
                min_window_start = start
            if s[start] in hash_map:
                hash_map[s[start]] += 1
                if hash_map[s[start]] > 0:
                    num_of_chars_to_be_included += 1
            start += 1
        end += 1
    if min_window_length == len(s)+1:# neu min_window_length khong thay doi gi so voi ban dau, thi chung to la s ko chua t
        return ""
    else:
        return s[min_window_start:min_window_start + min_window_length]


print(MinimumWindow2("ADOBECODEBANC", "ABC"))
print(MinimumWindow2("AA", "AA"))
# test github
