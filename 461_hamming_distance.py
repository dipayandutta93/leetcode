class Solution(object):
	def hammingDistance(self, x, y):

		count=0
		while x!=0 or y!=0:
			xdigit= x%2
			ydigit = y%2

			if xdigit != ydigit:
				count+=1

			x = x/2
			y=y/2
		return count
S=Solution()
x=1
y=4
out=S.hammingDistance(x,y)
print(out)