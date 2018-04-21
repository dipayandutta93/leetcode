class Solution(object):
	def reverseBits(self, n):

		n = bin(n)[2:].zfill(32)
		n1=[]

		for i in range(1,33):
			n1.append(n[-i])

		n1="".join(n1)
		n1= int(n1,2)
			
		return n1

S = Solution()
n = 43261596
out = S.reverseBits(n)
print(out)