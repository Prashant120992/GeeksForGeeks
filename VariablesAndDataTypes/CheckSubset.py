# Given two sets a and b. check whether a is subset of b?

# An a is subset of b, if all elements of a set a are present in another set b.

# Examples:
#
# Input: a = [1, 4, 3], b = [1, 4, 3, 2]
# Output: True
class Solution:
     def checkSubset(self, A,B):
         for i in A:
             if i not in B:
                 return False
         return True
a = [0,9,5]
b = [1, 4, 3, 2]
C = Solution()
result = C.checkSubset(a,b)
print(result)


