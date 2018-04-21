class Solution(object):
    def fizzBuzz(self, n):
        l = []
        for i in range(1,n+1):
            if i%3 == 0 and i%5 == 0:
                l.append("FizzBuzz")
            elif i%3 == 0 and i%5 != 0:
                l.append("Fizz")
            elif i%5 == 0 and i%3 !=0:
                l.append("Buzz")
            else:
                l.append("%d"%i)

        return l

S = Solution()
nums = 1
out = S.fizzBuzz(nums)
print(out)