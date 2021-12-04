from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        if k > len(nums):
            k = k%len(nums)
            print(k)
        
        nums[:] = nums[-k:]+nums[:-k]    
        print(nums)
    # too slow
    # def rotate(self, nums: List[int], k: int) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     for x in range(k):
    #         nums[:] = [nums[-1]]+nums[:-1]
        
    #     print(nums)
test = Solution()


            
print(test.rotate([1,2,3,4,5,6,7],3),[5,6,7,1,2,3,4])
print(test.rotate([-1,-100,3,99],2),[3,99,-1,-100])
print(test.rotate([1,2],3),[2,1])