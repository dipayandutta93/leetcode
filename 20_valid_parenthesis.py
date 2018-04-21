class Solution(object):
	def isValid(self, s):
		"""
		:type s: str
		:rtype: bool
		"""

		dict1 = {'(':1, '{':2, '[':3}
		dict2 = {')':1, '}':2, ']':3}
		l = []

		if len(s)%2 != 0:
			return False
		for i in range(0,len(s)):
			print(s[i])
			if s[i] in dict1:
				l.append(s[i])
			elif s[i] in dict2:
				if l == []:
					return False
				elif dict1[l.pop()] != dict2[s[i]]:
					return False
		
		if l != []:
			return False
		else: 
			return True

	
S = Solution()
print (S.isValid("()"))


