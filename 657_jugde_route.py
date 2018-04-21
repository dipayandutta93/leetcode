class Solution(object):
	def judgeCircle(self, moves):

		hash = {"U":0, "D":0, "L":0, "R":0}
		for i in range(0,len(moves)):
			if moves[i] not in hash.keys():
				hash[moves[i]] = 1
			else:
				hash[moves[i]]+=1
			
		if hash["U"] == hash["D"] and hash["L"]==hash["R"]:
			return True
		else:
			return False

S=Solution()
s="LL"
out=S.judgeCircle(s)
print(out)