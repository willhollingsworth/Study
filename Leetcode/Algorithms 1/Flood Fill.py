'''
https://leetcode.com/problems/flood-fill/


'''
from typing import ChainMap, List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.image = image
        self.nc = newColor
        self.iter = 1
        
        self.change_color(sr,sc)
        return self.image
    
    def change_color(self,r,c):
        try:
            self.image[r][c] = self.nc
            self.check_neighs(r,c)
        except: return
        
        
    def check_neighs(self,r,c):
        if self.iter == 0: return
        self.change_color(r+1,c)
        self.change_color(r-1,c)
        self.change_color(r,c+1)
        self.change_color(r,c-1)
        self.iter -= 1     
    
t = Solution()

print(t.floodFill([
    [1,1,1],
    [1,1,0],
    [1,0,1]],   1,1,2),
    
    [[2,2,2],
    [2,2,0],
    [2,0,1]])

