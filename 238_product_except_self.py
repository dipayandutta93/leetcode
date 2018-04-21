class Solution(object):
    def productExceptSelf(self, nums):

    	prod = 1
    	zero_present = 0
    	for i in range(0,len(nums)):
    		if nums[i] == 0:
    			zero_present +=1
    		else:
				prod= prod*nums[i]

    	lst = []
    	for i in range(0,len(nums)):
    		if zero_present == 1:
    			if nums[i] == 0:
    				lst.append(prod)
    			else:
    				lst.append(0)
    		elif zero_present >1:
    			lst.append(0)
    		else:
    			lst.append(prod/nums[i])

    	return lst

S = Solution()
s = [0,2,3,4]
out = S.productExceptSelf(s)
print(out)