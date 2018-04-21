class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """

        if len(word) > 1:
            if word.islower():
                return True
            elif word.isupper():
                return True
            elif word[0].isupper() and word[1:].islower():
                return True
            else:
                return False
        else:
            return True 



S = Solution()
out = S.detectCapitalUse("G")
print (out)