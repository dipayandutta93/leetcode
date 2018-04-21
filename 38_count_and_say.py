class Solution(object):
	def countAndSay(self, n):

		list1 = []
		if n==1:
			return "1"
		if n==2:
			return "11"

		list1.append("1")
		list1.append("11")

		for i in range(2,n):
			count = 1
			l=[]
			l = list1[i-1]
			l = list(l)

			arr = []
			for k in range(0,len(l)):

				if k+1 == len(l):
					s = str(count)+l[k]
					arr.append(s)

				elif l[k] == l[k+1]:
					count +=1
				elif l[k] != l[k+1]:
					s = str(count)+l[k]
					arr.append(s)
					count = 1
			
			arr = "".join(arr)
			list1.append(arr)

		return list1[-1]

S=Solution()
out=S.countAndSay(5)
print(out)