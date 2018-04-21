class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        l = 1
        r = x
        mid = x/2

        if x == 0:
        	return 0

        while l <= r:
        	mid = (l+r)/2
        	if mid>x/mid:
        		r = mid-1
        	elif mid<x/mid:
        		l = mid+1
        	else:
        		return mid
        	print mid
        return mid


S = Solution()
x = 8
out = S.mySqrt(x)
print out