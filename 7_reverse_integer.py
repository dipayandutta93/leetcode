class Solution(object):
	def reverse(self, x):
		"""
		:type x: int
		:rtype: int
		"""

		flag = 0
		if x <0:
			x = abs(x)
			flag = 1

		i=len(str(x)) - 1
		num = 0
		while x!=0:
			y=x%10
			num = num + (10**i) * y
			i=i-1
			x=x/10
			
		if flag ==1:
			num = -num

		if num > 2147483647 or num < -2147483647:
			return 0 
		
		return num

S = Solution()
out = S.reverse(1534236469)
print (out)