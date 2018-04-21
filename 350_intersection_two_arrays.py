class Solution(object):
    def intersect(self, nums1, nums2):

    	hash = {}
    	s = []

    	for i in range(0,len(nums1)):
    		if nums1[i] not in hash.keys():
    			hash[nums1[i]]=1
    		else:
    			hash[nums1[i]]+=1

    	for i in range(0,len(nums2)):
    		if nums2[i] in hash.keys() and hash[nums2[i]]!=0:
    			hash[nums2[i]]-=1
    			s.append(nums2[i])
    	return s


S = Solution()
nums1 = [1]
nums2 = [1,1]
out = S.intersect(nums1, nums2)
print(out)	