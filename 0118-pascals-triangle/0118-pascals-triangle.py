class Solution(object):
    def generate(self, numRows):
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            s = [1,1]
            n = 2
            b = [1]
            e = [[1],[1,1]]
            while n < numRows:
                for i in range(0, len(s)-1):
                    b.append(s[i]+s[i+1])
                b.append(1)
                s = b
                b = [1]
                n += 1 
                e.append(s)
            return e
        
        