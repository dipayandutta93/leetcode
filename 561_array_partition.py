class Solution(object):
	def arrayPairSum(self, nums):
		nums = sorted(nums)
		l = []
		for i in range(0,len(nums)):
			if i%2 == 0:
				l.append(nums[i])
		

		return sum(l) 

S=Solution()
nums = [1,3,2,4]
out=S.arrayPairSum(nums)
print(out)