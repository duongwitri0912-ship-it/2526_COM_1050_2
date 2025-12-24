class Solution(object):
    def majorityElement(self, nums):
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        n_half = len(nums) // 2
        
        for key in d:
            if d[key] > n_half:
                return key
        


        