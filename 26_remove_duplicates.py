class Solution(object):
	def removeDuplicates(self, nums):

		if len(nums) == 0 or len(nums) == 1:
			return len(nums)

		j=0

		for i in range(0,len(nums)-1):
			if nums[i] != nums[i+1]:
				nums[j] = nums[i]
				j+=1

		nums[j] = nums[len(nums)-1]
		j+=1
		del nums[j:]
		return j


S = Solution()
n = [1,1,2]
out = S.removeDuplicates(n)
print(out)