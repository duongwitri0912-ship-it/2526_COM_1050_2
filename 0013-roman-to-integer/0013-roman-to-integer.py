class Solution(object):
    def romanToInt(self, s):
        total = 0
        remain = 0
        found = True
        dict = {"IV": 4,"IX": 9,"XL": 40,"XC": 90,"CD": 400,"CM": 900}
        dict2 = {"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}
        while found:
            found = False
            for i in range (0, len(s)-1):
                a = s[i:i+2]
                if a in dict:
                    remain += dict[a]
                    s = s.replace(a, "")
                    found = True
        for i in s:
            if i in dict2:
                total += dict2[i]
        return remain + total

            

        