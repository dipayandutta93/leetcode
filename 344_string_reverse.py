class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """

        return s[::-1]

S = Solution()
out = S.reverseString("leetcode")
print (out)
