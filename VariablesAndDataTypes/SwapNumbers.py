# Given 2 numbers a and b, Need to swap their values so a holds the value of b and b holds the value of a.
# Write a code to swap values of a and b at the specified place.
class solution:
    def swap(self, a,b):
        a, b = b,a
        print(a, b)

c = solution()
c.swap(5, 6)

