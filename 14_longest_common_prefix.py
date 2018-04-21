class Solution(object):
	def longestCommonPrefix(self,strs):
		"""
		:typestrs:List[str]
		:rtype:str
		"""

		if len(strs) == 0:
			return ""
		longest_str = max(strs, key=len)
		substring = []

		while len(strs) != 0:

			elem = strs.pop()

			for i in range(0, len(elem)):
				if longest_str[i] != elem[i]:
					substring.append(longest_str[:i])
					break
			
			
			substring.append(elem)
					

		return min(substring, key=len)

S=Solution()
list_of_string = []
out=S.longestCommonPrefix(list_of_string)
print(out)
