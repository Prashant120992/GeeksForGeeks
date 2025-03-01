# Given two sets A and B. find the Union of both the sets.
# Union of two given sets A and B is a set which consists of all the elements of A and all the elements of B
# such that no element is repeated.

# Input:
# A = {2, 5, 6}
# B = {1, 4, 3, 2}
# Output:
# 1 2 3 4 5 6

class solution:
    def Union(self, A, B):
        c = A.union(B)
        return c
a = {2, 5, 6}
b = {1, 4, 3, 2}
result = solution()
union_set=result.Union(a, b)
print(sorted(list(union_set)))
print(*sorted(list(union_set)))
print((set(union_set)))


