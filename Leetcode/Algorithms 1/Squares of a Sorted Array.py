

class Solution:
    def sortedSquares(self,nums):
        out = []
        for x in nums:
            out.append(x ** 2)
        out.sort()    
        return out
    
    
test = Solution()

print(test.sortedSquares([-4,-1,0,3,10]),[0,1,9,16,100])
print(test.sortedSquares([-7,-3,2,3,11]),[4,9,9,49,121])

        