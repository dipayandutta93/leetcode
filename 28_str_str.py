class Solution(object):
	def strStr(self, haystack, needle):

		if len(needle)>len(haystack):
			return -1
		index = -1
		
		for i in range(0,len(haystack)):
			k = i
			for j in range(0,len(needle)):
				if k >= len(haystack):
					return index
				if haystack[k] != needle[j]:
					break
				k +=1
				if j == len(needle)-1:
					index = i
					return index
		if needle == "":
			return 0
		return index

S=Solution()
haystack = "mississipi"
needle = "issippi"
out=S.strStr(haystack,needle)
print(out)