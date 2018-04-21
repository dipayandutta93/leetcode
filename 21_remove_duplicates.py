class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for i in range(0,len(nums)):
        	for j in range(i,len(nums)):
        		if j < len(nums) and i < len(nums) and nums[i] == nums[j]:
        			del nums[j]

        return len(nums), nums

S = Solution()
print (S.removeDuplicates([1,1,2]))