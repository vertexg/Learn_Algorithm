def maxValue(array2d):
    curr = array2d[0][0]
    for array1d in array2d:
        for ele in array1d:
            if curr <= ele: curr = ele
    return curr

# 6
print(maxValue([[1,1,2,3,2], [5,5,1,5,2], [3,5,2,3,1], [1,2,3,6,3]]))

# 81
print(maxValue([[0,9,1,4,5], [1,3,3,4,7], [11,12,34,81,12], [12,24,63,76,13]]))
