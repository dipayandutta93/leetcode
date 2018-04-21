class Solution(object):
	def rotate(self, nums, k):


		n=len(nums)
		nums= nums+nums
		nums=nums[(n-k):(2*n-k)]
		print nums
		return nums

S = Solution()
nums = [1,2]
k=1
out = S.rotate(nums,k)
print(out)