class Solution(object):
    def titleToNumber(self, s):
        
        str = list(s)

        c= str.pop()
        sum = ord(c)-64

        i=1
        while len(str) != 0:
            c = str.pop()
            sum = sum + (26**i)*(ord(c)-64)
            i+=1
        return sum

S = Solution()
s = "ZX"
out = S.titleToNumber(s)
print(out)