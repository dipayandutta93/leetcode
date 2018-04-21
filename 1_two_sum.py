class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        indices = []

        for i in range(0,len(nums)):
        	for j in range(i,len(nums)):
        		if nums[i]+nums[j] == target:
        			indices.extend([i,j])
        return indices

class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        indices = []

        dict = {}
        
        if len(nums) <= 1:
        	print "Please enter two numbers as input"

        for i in range(0,len(nums)):
        	if nums[i] in dict:
        		indices.extend([dict[nums[i]],i])
        	else :
        		dict[target - nums[i]] = i
	       

        return indices

S = Solution()
S1 = Solution2()
nums = [2,7,11,15]
target = 9
out = S.twoSum(nums,target)
out2 = S1.twoSum(nums,target)
print (out)
print(out2)