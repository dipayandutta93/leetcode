class Solution(object):
	def reverseWords(self, s):
		index = 0
		s=list(s)
		for i in range(0,len(s)):
			if s[i] == " " or i == len(s) -1:
				j=index
				k=i-1
				if i==len(s)-1:
					k=i
				while j <=k:
					temp = s[j]
					s[j] = s[k]
					s[k] = temp
					j+=1
					k-=1
					index = i+1
		return "".join(s)


S=Solution()
s = "Let's take LeetCode contest"

out=S.reverseWords(s)
print(out)