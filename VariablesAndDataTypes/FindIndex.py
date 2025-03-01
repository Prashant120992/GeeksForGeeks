# Given a tuple arr with distinct elements and an integer x, find the index position of x.
# Assume it to have x in the tuple always.
#
# Examples:
#
# Input: arr = (1, 2, 3, 4, 5), x = 3
# Output: 2
# Input: arr = (3, 2, 1, 5, 4), x = 5
# Output: 3
class Solution:
    def FindIndex(self, arr, x):
        try:
            return arr.index(x)
        except ValueError:
            return -1
arr1 = (1, 2, 3, 4, 5)
x1 = 7
res=Solution()
print(res.FindIndex(arr1, x1))