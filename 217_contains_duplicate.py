class Solution(object):
    def containsDuplicate(self, nums):

        if len(nums)> len(set(nums)):
            return True
        else:
            return False

S = Solution()
s = [2,4,6]
out = S.containsDuplicate(s)
print(out)
