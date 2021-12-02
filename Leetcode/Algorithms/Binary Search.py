'''
https://leetcode.com/problems/binary-search/
'''

class Solution:
    def search(self, nums, target: int) -> int: 
        for x in range(len(nums)):
            if nums[x] == target:
                return x
            elif nums[x] >= target:
                return -1
        return -1
    
solution = Solution()        
        
print(solution.search([-1,0,3,5,9,12],9),4)
print(solution.search([-1,0,3,5,9,12],2),-1)