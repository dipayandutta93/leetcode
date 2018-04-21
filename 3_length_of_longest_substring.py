class Solution(object):
	def lengthOfLongestSubstring(self, s):

		s = list(s)
		substr=[]
		max_len = 0

		for i in range(0,len(s)):
			#print max_len
			if s[i] not in substr:
				substr.append(s[i])
			else:
				for j in range(0,len(substr)):
					if substr[j] == s[i]:
						substr = substr[(j+1):]
						substr.append(s[i])
						#print "substr %s"%(substr)
						
						break
			if len(substr)>max_len:
				max_len = len(substr)
			#print substr
		return max_len

S=Solution()
out=S.lengthOfLongestSubstring("pwwkew")
print(out)