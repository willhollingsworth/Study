from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]
        print(s)
        
t = Solution()

t.reverseString(["h","e","l","l","o"])     
        
        
        