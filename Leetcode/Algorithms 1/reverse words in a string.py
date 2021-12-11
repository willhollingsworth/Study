from typing import List



class Solution:
    def reverseWords(self, s: str) -> str:
        nlist = []
        for word in s.split():
            nlist.append(word[::-1])
        return ' '.join(nlist)  
        
        
t = Solution()


t.reverseWords("Let's take LeetCode contest") 