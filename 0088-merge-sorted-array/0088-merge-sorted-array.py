class Solution(object):
    def merge(self, nums1, m, nums2, n):
        del nums1[m:len(nums1)]
        nums1.extend(nums2)
        def me(nums1):
            if len(nums1) <= 1:
                return nums1
            mid = len(nums1)//2
            left = nums1[:mid]
            right = nums1[mid:]
            sorted_left = me(left)
            sorted_right = me(right)
            return m(sorted_left, sorted_right)
        def m(left, right):
            res = []
            i=j=0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            res.extend(left[i:])
            res.extend(right[j:])
            return res
        nums1[:] = me(nums1)
        return nums1
        
           
        