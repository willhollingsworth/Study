
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = min(1,len(s))
        tested_chars = ''
        length = len(s)
        
        for c1 in range(length):
            tested_chars = s[c1]
            for c2 in range(c1+1,length):
                if s[c2] not in tested_chars:
                    tested_chars += s[c2]
                    longest = max(longest,len(tested_chars))
                else:
                    break
        return longest

        
        
t = Solution()

print(t.lengthOfLongestSubstring("abca"),3)
print(t.lengthOfLongestSubstring("abcabcbb"),3)
print(t.lengthOfLongestSubstring("bbbbb"),1)
print(t.lengthOfLongestSubstring(" "),1)
print(t.lengthOfLongestSubstring("dvdf"),3)