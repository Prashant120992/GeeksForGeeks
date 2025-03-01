# Given a tuple arr , print "True" if all elements of tuple are different otherwise print "False".
# A tuple is a collection of items that are ordered and unchangeable.
# Examples:
#
# Input:
# arr = (1, 2, 3, 4, 5, 4)
# Output: False
# Input:
# arr = (1, 2, 3, 4, 5)
# Output: True

class Solution:
    def CheckTupleDistinct(self, arr):
        arr1=[]
        for i in arr:
            if i not in arr1:
                arr1.append(i)
            else:
                return False
        return True
arr2 = [1, 2, 3, 4, 5]
res = Solution()
print(res.CheckTupleDistinct(arr2))