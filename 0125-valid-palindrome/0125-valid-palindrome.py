class Solution(object):
    def isPalindrome(self, s):
        b = ""
        for i in s:
            if i.isdigit() or "a" <= i.lower() <= "z":
                b += i.lower()
        if b == b[::-1]:
            return True
        else:
            return False

        
        