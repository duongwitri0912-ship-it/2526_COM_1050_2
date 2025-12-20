class Solution(object):
    def plusOne(self, digits):
        c = []
        a = ""
        for i in digits:
            a += str(i)
        b = str(int(a) + 1)
        for j in b:
            c.append(int(j))
        return c

        