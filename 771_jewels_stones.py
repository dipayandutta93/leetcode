class Solution(object):
	def numJewelsInStones(self, J, S):
		count =0
		for i in range(0,len(S)):
			if S[i] in J:
				count+=1
		return count
		

S=Solution()
St = "z"
J = "ZZ"
out=S.numJewelsInStones(St,J)
print(out)