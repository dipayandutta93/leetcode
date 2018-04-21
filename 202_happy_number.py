class Solution(object):
    def isHappy(self, nums):

    	s = []
        while nums!=1:
        	sum =0


        	while nums!=0:
        		xdigit =nums%10
        		sum = sum + xdigit**2
        		nums=nums/10
        	if sum not in s:
        		s.append(sum)
        	else:
        		return False
        	print s

        	nums=sum

        return True

S = Solution()
s = 2
out = S.isHappy(s)
print(out)