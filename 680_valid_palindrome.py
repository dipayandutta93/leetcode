class Solution(object):

    def checkPalindrome(self,str):
        
        index1 = len(str) -1
        index2 = 0

        while index1 >= index2:

        	if str[index1] != str[index2]:
        		return False, index1, index2
        	index1 = index1 - 1
        	index2 = index2 + 1
    	
    	return True, index1, index2

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        type, i1, i2 = self.checkPalindrome(s)

        if type == False:

        	str1 = s[:i1] + s[(i1+1):]
        	str2 = s[:i2] + s[(i2+1):]

        	type1, j1, j2 = self.checkPalindrome(str1)
        	type2, k1, k2 = self.checkPalindrome(str2)

        	if type1 == False and type2 == False:
        		return False

        return True



S = Solution()
out = S.validPalindrome("bsddb")
print (out)