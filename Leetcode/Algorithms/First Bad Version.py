# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

import random

def isBadVersion(num,length):
    bad_version = 9
    if num >= bad_version:
        return True
    else: 
        return False

class Solution:
    def firstBadVersion(self, length):
        """
        :type n: int
        :rtype: int
        """
        high = length
        low = 0
        test = int(length/2)
        while True:
            if low == high - 1:
                    break
            if isBadVersion(test):
                print(test,'is bad')
                high = test
                test = high - int((high - low)/2)
            else:
                print(test,'is good')
                low = test
                test = int((high - low)/2) + low
        print('last bad version is',high)
        return high
    
solution = Solution()

solution.firstBadVersion(12)
    
                
        # isBadVersion(3)
        # return
            
''''
        second method storing a high and low value
        b7 L12
        t6 g
        t9 b
        
        
        
        
        
        first method, works
        bad = 3, length = 8
        test 4 = bad
        test 2 = good
        test 3 = bad
        
        
        first method
        this doesnt work if you round up or down
        bad 7 , length = 12 (round up) 
        6 good
        9 is bad
        5 is good
        8 is bad
        4 is good
        6 is good
        
        
        
        
        
        
'''    
