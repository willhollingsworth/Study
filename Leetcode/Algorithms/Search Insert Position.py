class Solution:
    def searchInsert(self, nums,target):
        if target in nums:
            return nums.index(target)
        nums.append(target)
        nums.sort()
        return nums.index(target)
        
        
        
        
test = Solution()

print(test.searchInsert([1,3,5,6],5),2)
print(test.searchInsert([1,3,5,6],2),1)
print(test.searchInsert([1,3,5,6],7),4)
