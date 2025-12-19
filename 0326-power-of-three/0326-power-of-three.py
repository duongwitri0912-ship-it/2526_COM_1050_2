class Solution(object):
    def isPowerOfThree(self, n):
        if n > 0 and ((3**19) % n == 0):
            return True
        else:
            return False
        
        