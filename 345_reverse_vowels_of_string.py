class Solution(object):
	def reverseVowels(self, s):
		"""
		:type s: str
		:rtype: str
		"""

		s = list(s)
		vowels = ['a', 'i', 'o', 'u', 'e', 'A', 'I', 'O', 'U', 'E']
		index1 = len(s)-1
		index2 = 0

		while index1 > index2:
			
			if s[index1] in vowels and s[index2] in vowels:
				s[index1], s[index2] = s[index2], s[index1]
				index1 = index1 -1
				index2 = index2 + 1

			if s[index1] not in vowels:
				index1 = index1 -1

			if s[index2] not in vowels:
				index2 = index2 + 1
			
		return "".join(s)

S = Solution()
out = S.reverseVowels("leetcode")
print (out)