class Solution(object):
	def rob(self, nums):

		p = []
		
		if len(nums) == 0:
			return 0

		if len(nums) == 1:
			return nums[0]
		if len(nums) == 2:
			return (max(nums[0], nums[1]))
				
		p.append(nums[0])
		p.append(max(nums[0], nums[1]))

		for i in range(2, len(nums)):
			p.append(max(nums[i]+p[i-2],p[i-1]))
		return p[len(nums)-1]


S = Solution()
s = [0]
out = S.rob(s)
print(out)