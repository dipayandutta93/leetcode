
class Solution(object):
	def romanToInt(self,s):
		"""
		:types:str
		:rtype:int
		"""

		integer = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

		number = 0
		for i in range(0, len(s)):

			if i+1 < len(s):
				if integer[s[i]] >= integer[s[i+1]]:
					number = number + integer[s[i]]
				else:
					number = number - integer[s[i]]

			else:
				number = number + integer[s[i]]
		return number

S=Solution()
out=S.romanToInt('IX')
print(out)

