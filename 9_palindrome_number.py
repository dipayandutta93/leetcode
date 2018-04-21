class Solution(object):
	def isPalindrome(self,x):
		"""
		:typex:int
		:rtype:bool
		"""

		flag=0
		if x<0:
			x=abs(x)
			flag=1

		i=len(str(x))-1

		if x > 2147483647 or x < -2147483647:
			return False 

		while x!=0:

			one = x/(10**i)
			two = x%10

			print (one)
			print (two)
			if one != two:
				return False
		
			x=x%(10**i)
			x=x/10
			i = i-2
	
		return True

S=Solution()
out=S.isPalindrome(-2147447412)
print(out)