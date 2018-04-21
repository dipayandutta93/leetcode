class Solution(object):
    def isPowerOfThree(self, n):

        while n!=0:
            if n == 1:
                return True
            if n%3!=0:
                return False
            n=n/3
        return False
        #One line solution
        #return n>0 and 1162261467%n==0

S = Solution()
s = -27
out = S.isPowerOfThree(s)
print(out)