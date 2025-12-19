class Solution(object):
    def removeDuplicates(self, nums):
        k = 1
        a = []
        for i in range(0, len(nums)-1):
            if nums[i] != nums[i+1]:
                k += 1
                a.append(nums[i])
        a.append(nums[len(nums)-1])
        nums[:] = []
        for j in a:
            nums.append(j)
        return k
        