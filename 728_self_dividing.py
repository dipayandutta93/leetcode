class Solution(object):
	def selfDividingNumbers(self, left, right):
		nums = []

		for i in range(left, right+1):
			j = i
			isDividing = False
			while j != 0:

				rem = j%10
				if rem == 0:
					isDividing = False
					break
				
				if i % rem != 0:
					isDividing = False
					break
				else:
					isDividing = True
				j=j/10

			if isDividing == True:
				nums.append(i)

		return nums

S=Solution()
left = 1
right =22
out=S.selfDividingNumbers(left,right)
print(out)