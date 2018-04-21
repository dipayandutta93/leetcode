class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = -99999
        max_so_far = -99999

        for i in range (0,len(nums)):
        	if max_sum + nums[i] >= nums[i]:
        		max_sum = max_sum + nums[i]
        	else:
        		max_sum = nums[i]

        	if max_sum > max_so_far:
        		max_so_far = max_sum
        		index = i
        largest_subarray = []

        sum = 0
        while sum < max_so_far:
        	largest_subarray = [nums[index]] + largest_subarray
        	sum = sum + nums[index]
        	index = index - 1

        #print(largest_subarray)

        return max_so_far

S = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
out = S.maxSubArray(nums)
print(out)