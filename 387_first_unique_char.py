class Solution(object):
    
    def firstUniqChar(self, s):

        hash = {}

        for i in range(0,len(s)):
            if s[i] not in hash.keys():
                hash[s[i]] = 1
            else:
                hash[s[i]]+=1
        print hash

        for i in range(0,len(s)):
            if hash[s[i]] == 1:
                return i
        return -1

S = Solution()
s = "anagram"
out = S.firstUniqChar(s)
print(out)