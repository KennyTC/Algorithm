class Solution(object):
    def repeatedStringMatch(self, A, B):
        count = 1
        orgA = A
        while (len(A) <= 100) and (not (B in A)):  # O(len(A))
            count = count + 1
            A = A + orgA  # len(A)
            print(A, count)
        if count == 100 // len(orgA) + 1:  # check if not found
            return -1
        else:
            return count

    def repeatedStringMatch2(self, A, B):
        if len(set(B)) > len(set(A)):
            return -1

        x = int(len(B) / len(A)) if len(B) % len(A) == 0 else int(len(B) / len(A)) + 1
        s = x * A

        for i in range(len(s) - len(B) + 1):
            tf = True
            for j in range(len(B)):
                if s[i + j] != B[j]:
                    tf = False
                    break
            if tf == True:
                return x

        x += 1
        s += A

        for i in range(len(s) - len(B) + 1):
            tf = True
            for j in range(len(B)):
                if s[i + j] != B[j]:
                    tf = False
                    break
            if tf == True:
                return x

        x += 1
        s += A

        for i in range(len(s) - len(B) + 1):
            tf = True
            for j in range(len(B)):
                if s[i + j] != B[j]:
                    tf = False
                    break
            if tf == True:
                return x

        return -1


#################################################################
    def repeatedStringMatch(self, A, B):
        if len(set(B)) > len(set(A)):
            return -1

        x = int(len(B) / len(A)) if len(B) % len(A) == 0 else int(len(B) / len(A)) + 1
        s = x * A

        for i in range(len(s) - len(B) + 1):
            tf = True
            for j in range(len(B)):
                if s[i + j] != B[j]:
                    tf = False
                    break
            if tf == True:
                return x

        x += 1
        s += A

        for i in range(len(s) - len(B) + 1):
            tf = True
            for j in range(len(B)):
                if s[i + j] != B[j]:
                    tf = False
                    break
            if tf == True:
                return x

        x += 1
        s += A

        for i in range(len(s) - len(B) + 1):
            tf = True
            for j in range(len(B)):
                if s[i + j] != B[j]:
                    tf = False
                    break
            if tf == True:
                return x

        return -1

# sample of comparing 2 strings: if the first char equals --> compare next. But if the first not equal, --> move to next character
##############################################################################################################################
    # idea: i chay qua tung phan tu cua A,
    #       j ......................... B
    #       so sanh A[i] vs B[j]. Neu giong nhau thi tiep tuc so sanh
    #                             Neu khac nhau, thi move sang phan tu tiep theo trong A
    #       Tiep tuc cho toi khi j chay het B.
    #       Neu i chay het A roi thi ta lai reset i lai tu dau, trong khi j van giu nguyen.
    def repeatedStringMatch3(self, A, B):
        if (set(B) - set(A)): # neu B chua nhung ki tu ma A ko co --> -1
            return -1

        if len(A) == 0 and len(B) == 0:
            return 0

        rep = 1
        i = 0
        j = 0
        while j < len(B):
            if i == len(A):
                a = rep * len(A) - (len(A) - 1) # ????WHY
                print(a)
                if a >= len(B):
                    return -1
                rep += 1
                i = 0
            if A[i] == B[j]:
                i += 1
                j += 1
            else:
                i += 1
                j = 0

        return rep


a = Solution()
print(a.repeatedStringMatch3("abcd", "cdabcdab"))


