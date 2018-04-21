class Solution(object):
    def majorityElement(self, nums):

    	hash = {}
    	for i in range(0,len(nums)):
    		if nums[i] not in hash.keys():
    			hash[nums[i]]=1
    		else:
    			hash[nums[i]]+=1

    	for key,values in hash.iteritems():
    		if values >len(nums)/2:
				return key

S = Solution()
s = [4,2,2,2]
out = S.majorityElement(s)
print(out)
