class Solution(object):
    def missingNumber(self, nums):

    	sum=0
    	for i in range(0,len(nums)):
    		sum+=nums[i]
    	return (len(nums)*(len(nums)+1)/2)-sum

S = Solution()
s = [0]
out = S.missingNumber(s)
print(out)