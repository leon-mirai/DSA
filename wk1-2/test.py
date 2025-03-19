# 2 parameters - arras - no size limit
# return boolean


arr1 = ['a', 'b', 'c', 'x']
arr2 = ['z', 'y', 'i']
# return false
arr3 = ['a', 'b','x']
arr4 = ['d', 'f', 's', 'x','e']
# return true

# def isCommonItem(array1, array2):
#     for i in range(len(array1)):
#         for j in range(len(array2)):
#             if (array1[i] == array2[j]):
#                 return True
#     return False

def isCommon2(ar1, ar2):
    # loop through first array and create dictionary
    # where properties == items in the array
    # loop through second array and check if item in second array exists on created dictionary
    myDict = dict()
    for i in ar1:
        if not i in myDict:
            item = i
            myDict[item] = True

    for j in ar2:
        if j in myDict:
            return True
    return False

print(isCommon2(arr1, arr2))
print(isCommon2(arr3, arr4))