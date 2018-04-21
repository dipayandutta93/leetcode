class Solution(object):
	def isPalindrome(self, s):
		i=0
		j=len(s)-1

		while i<=j:
			print s[i]
			print s[j]
			while not s[i].isalnum() and i<j:
				i+=1
			while not s[j].isalnum() and i<j:
				j-=1
			if s[i].lower() != s[j].lower():
				return False

			i+=1
			j-=1
		return True

S = Solution()
s = ".,"
out = S.isPalindrome(s)
print(out)