class Solution(object):
	def searchInsert(self, nums, target):
		for i in range(0,len(nums)-1):
			if target > nums[i] and target <= nums[i+1]:
				return i+1

		if target <= nums[0]:
			return 0
		elif target > nums[len(nums)-1]:
			return len(nums)

S=Solution()
l = [1]
target = 1
out=S.searchInsert(l,target)
print(out)
