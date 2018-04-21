class Solution(object):
    def topKFrequent(self, nums, k):

        hash = {}
        for i in range(0,len(nums)):
            if nums[i] not in hash:
                hash[nums[i]] = 1
            else:
                hash[nums[i]] +=1


        lst = []
        lst = sorted(hash.items(), key=lambda kv: kv[1], reverse=True)

        print hash
        i = 0
        l = []
        for elem in lst:

            if i < k:
                l.append(elem[0]) 

            i+=1   
        return l

S = Solution()
s = [4,1,-1,2,-1,2,3]
out = S.topKFrequent(s,2)
print(out)