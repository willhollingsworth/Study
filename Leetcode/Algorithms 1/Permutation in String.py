class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        f_char = []
        for i,c in enumerate(s2):
            if c == s1[0]:
                f_char.append(i)
        for direction in range(2):
            for f in f_char:
                if direction:
                    if s2[f+1] == s1[1]:
                        return True
                else:
                    if s2[f-1] == s1[1]:
                        return True
        
        
        
t = Solution()

print(t.checkInclusion("ab","eidbaooo"),True)
print(t.checkInclusion("zx","eidbaxo"),True)