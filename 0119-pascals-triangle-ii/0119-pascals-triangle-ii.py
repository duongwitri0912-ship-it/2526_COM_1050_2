class Solution(object):
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            s = [1,1]
            n = 1
            b = [1]
            while n < rowIndex:
                for i in range(0, len(s)-1):
                    b.append(s[i]+s[i+1])
                b.append(1)
                s = b
                b = [1]
                n += 1 
            return s
        
        
        
        