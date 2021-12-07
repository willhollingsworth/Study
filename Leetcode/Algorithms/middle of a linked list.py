from typing import Optional,List
'''
Python does not have native linked lists making this question harder to test and answer

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        print(head.next.next)
        
        # mid = int(len(head)/2)
        # return head[mid:]
        
        
        
t = Solution()

print(t.middleNode([1,2,3,4,5]))
print(t.middleNode([1,2,3,4,5,6]))