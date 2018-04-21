class Solution(object):
    
    def isAnagram(self,string1,string2):
        
        hash = {}

        if len(string1) != len(string2):
            return False
        for i in range(0,len(string1)):
            if string1[i] in hash: 
                hash[string1[i]]+= 1
            else:
                hash[string1[i]]=1
            if string2[i] in hash:
                hash[string2[i]]-=1
            else:
                hash[string2[i]]=-1
        return all(value==0 for value in hash.values())

S = Solution()
s = "anagram"
t = "nagram"
out = S.isAnagram(s,t)
print(out)