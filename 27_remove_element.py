class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        l = len(nums)
        i=0
        while i < l:
        	if nums[i] == val:
        		del nums[i]
        		l=len(nums)
        		i = i-1
        	i = i+1
        		
        return len(nums)

S = Solution()
print(S.removeElement([3,3],3))