from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zcount = nums.count(0)
        while 0 in nums: nums.remove(0)
        for x in range(zcount):
            nums.append(0)
        print(nums)
        
test = Solution()
print(test.moveZeroes([0,1,0,3,12]),[1,3,12,0,0])