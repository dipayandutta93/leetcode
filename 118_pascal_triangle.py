class Solution(object):
	def generate(self, numRows):

		a = [1]*(n)

		for i in range(0,n):
			a[i] = [1]*(i+1)

		for i in range(0,n):
			a[i][0] =1

			for j in range(1,i):
				a[i][j] = a[i-1][j]+a[i-1][j-1]

		return a


S = Solution()
n = 5
out = S.generate(n)
print(out)