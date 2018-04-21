class Solution(object):
	def findComplement(self, num):
		
		y=1
		n = num
		while num>0:
			y = y << 1
			num = num/2
		return ((y-1)-n)
		

S=Solution()
nums = 2
out=S.findComplement(nums)
print(out)