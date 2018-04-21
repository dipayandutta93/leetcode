class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        s = list(s)
        count =0

        if len(s) == 0 :
            return 0

        index = len(s)-1
        for i in range(len(s)-1,-1,-1):
            if s[i] != " ":
                index = i
                break
        for i in range(index,-1,-1):
            if s[i] != " ":
                count+=1
            else:
                return count
        return count    


        
S = Solution()
nums = "a  "
out = S.lengthOfLastWord(nums)
print out