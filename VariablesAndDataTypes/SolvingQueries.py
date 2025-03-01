# Given a dictionary, and a list of queries(keys),
# you have to find and print the value of each query from the dictionary if present else it prints "None".

class Solution:
    def SolvingQueries(self, dic, query):
        result = []
        for queries in query:
            if queries in dic:
                result.append(dic[queries])
            else:
                result.append(None)
        return result

di={1:"abc", 2:"cde", 6:12}
li = [1, 5, 2]
sol = Solution()
res=sol.SolvingQueries(di,li)
for item in res:
    print(item)
