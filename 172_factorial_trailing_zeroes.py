class Solution(object):
	def trailingZeroes(self, n):
		
		x=0
		i=1
		while (5**i)<=n:
			x+=n/(5**i)
			i+=1
		
		return x


S = Solution()
n = 7
out = S.trailingZeroes(n)
print(out)