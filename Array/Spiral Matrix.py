import numpy as np


def SpiralMatrix(L):
    array = []
    M = np.array(L)
    while (M.size > 0):
        # right
        if (M.size > 0):
            array.extend(list(M[0, :]))
            M = M[1:, :]  # remove the first row
        print("After right {}".format(M))
        # down
        if (M.size > 0):
            array.extend(list(M[:, -1]))
            M = M[:, :-1]  # remove the last col
        print("After down {}".format(M))
        # left
        if (M.size > 0):
            array.extend(reversed(list(M[-1, :])))
            M = M[:-1, :]
        print("After left {}".format(M))
        # up
        if (M.size > 0):
            array.extend(reversed(list(M[:, 0])))
            M = M[:, 1:]
        print("After up {}".format(M))
    print(array)
    return array
######################################################################################################
#2.
# We used Numpy to easily sliding. But in case, we can not use Numpy, how to solve it?. Idea is consider
# c1...c2 : beginning and ending col
# r1...r2: beginning and ending row
# We will have a function to go around the rectangule created by c1, c2, r1,r2.
# Increase c1, r1 by 1, decrease c2, r2 by 1. Then call the function again. 
def SpiralMatrix2(matrix):
    def spiral_coords(r1, c1, r2, c2):
        for c in range(c1, c2 + 1):
            yield r1, c  # traverse top
        for r in range(r1 + 1, r2 + 1):
            yield r, c2  # traverse right
        if r1<r2 and c1<c2:
            for c in range(c2 - 1, c1, -1):
                yield r2, c  # traverse bottom
            for r in range(r2, r1, -1):
                yield r, c1  # traverse left

    if not matrix: return []
    array = []
    r1, r2 = 0, len(matrix) - 1
    c1, c2 = 0, len(matrix[0]) - 1
    while r1 <= r2 and c1 <= c2:
        for r, c in spiral_coords(r1, c1, r2, c2):
            array.append(matrix[r][c])
            r1 += 1
            r2 -= 1
            c1 += 1
            c2 -= 1
    print(array)
    return array


C = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
SpiralMatrix2(C)
