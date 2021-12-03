# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

import random

def isBadVersion(num,length):
    bad_version = 3
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
        test = length/2
        last_good = 0
        while True:
            if isBadVersion(test,length):
                print(test,'is bad')
                if last_good == test-1:
                    break
                test = int(test/2)
            else:
                print(test,'is good')
                last_good = test
                
                test = test + int(test/2)
        return test            
        # isBadVersion(3)
        # return
            
        ''''
        bad = 3, length = 8
        test 4 = bad
        test 2 = good
        test 3 = bad
        
        
        
        this doesnt work if you round up or down
        bad 7 , length = 12 (round up) 
        6 good
        9 is bad
        5 is good
        8 is bad
        4 is good
        6 is good
        
        
        
        
        
        
        '''    
solution = Solution()

print(solution.firstBadVersion(8))