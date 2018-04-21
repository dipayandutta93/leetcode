class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        
        i,j,k = 0,0,0
        nums = []

        while k < n+m:
            if nums1[i] <= nums2[j]:
                print(k)
                nums[k] = nums1[i]
                i+=1
                k+=1
            else:
                nums[k] = nums2[j]
                j+=1
                k+=1
        return nums

S = Solution()
nums1 = [1,5,8]
nums2 = [2,3,10]
out = S.merge(nums1,3,nums2,3)
print (out)