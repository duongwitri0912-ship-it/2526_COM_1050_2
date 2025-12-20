class Solution(object):
    def lengthOfLastWord(self, s):
        j = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                if j != 0:
                    break
                else:
                    continue
            else:
                j += 1
        return j
        

     
        