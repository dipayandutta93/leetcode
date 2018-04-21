class Solution(object):
	def findDisappearedNumbers(self, nums):

		l = []
		l = list(set(range(1,len(nums)+1)) - set(nums))
		return l

S = Solution()
n = [4,3,2,7,8,2,3,1]
out = S.findDisappearedNumbers(n)
print(out)