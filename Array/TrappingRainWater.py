#######################################################################
# 1. can not understand the part: For index i, the water volume of i: vol_i = min(left_max_i, right_max_i) - bar_i!!!
def TrappingRainWater(array):
    trap = 0
    for i in range(len(array)):
        max_left = 0;
        max_right = 0
        for j in range(i + 1):
            max_left = max(max_left, array[j])
        for j in range(i, len(array)):
            max_right = max(max_right, array[j])
        print("i:{},array[i]:{},Max_left:{}, Max_right:{},min():{},*:{}".format(i, array[i], max_left, max_right,
                                                                                min(max_left, max_right),
                                                                                min(max_left, max_right) - array[i]))
        trap += min(max_left, max_right) - array[i]
    return trap


############################################################################
# 2.
# def TrappingRainWater2(array):
#     if array == None:
#         return 0
#     trap = 0
#     size = len(array)
#     max_left = array
#     max_right = array  # Here is 2 lists, not 2 values
#     max_left[0] = array[0]
#     for i in range(1, len(array)):
#         max_left[i] = max(array[i], max_left[i - 1])
#     print("max_left:{}".format(max_left))
#     max_right[size - 1] = array[size - 1]
#     for i in range(size - 2, -1, -1):  # loop down
#         max_right[i] = max(array[i], max_right[i + 1])
#     print("max_right:{}".format(max_right))
#     for i in range(1, size - 1, 1):  # loop up
#         print("i:{},Max_left:{}, Max_right:{},min:{}".format(i, max_left[i], max_right[i],
#                                                            min(max_left[i], max_right[i])))
#         trap += min(max_left[i], max_right[i]) - array[i]
#     return trap


print(TrappingRainWater2([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
