class Solution(object):
    def calPoints(self, ops):

    	ops = list(ops)

    	score = []
    	ops = ["0","0"]+ ops
    	for op in ops:
    		if self.RepresentsInt(op):
    			
    			score.append(int(op))

    		elif op == "+":
    			score.append(score[-1]+score[-2])
    			
    		elif op == "D":
    			score.append(score[-1]*2)
    			
    		elif op == "C":
    			score.pop()
    			
    				
    	return sum(score)

    def RepresentsInt(self,a):
    	try:
    		int(a)
    		return True
    	except ValueError:
    		return False
        
        

S = Solution()
nums = ["5","2","C","D","+"]
out = S.calPoints(nums)
print(out)