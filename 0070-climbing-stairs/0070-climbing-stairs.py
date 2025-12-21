class Solution(object):
    def climbStairs(self, n):
        a = 0
        b = 1
        st = 1
        for _ in range(n):
            st = a + b
            a, b = b, st
        return st

        
        