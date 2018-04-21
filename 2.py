def solution(A):

	s=[]
	start=0
	dist_count = 0
	for i in range(0,len(A)):
		if A[i] not in s:
			s.append(A[i])
			dist_count+=1

	print dist_count

	curr_count ={}
	count =0

	for i in range(0,len(A)):
		print i
		print "count"
		print count
		print curr_count
		if A[i] not in curr_count.keys():
			curr_count[A[i]] =1	
		else:
			curr_count[A[i]]+=1

		if curr_count[A[i]]==1:
			count+=1

		if count == dist_count:
			while curr_count[A[start]]>1:
				curr_count[A[start]]-=1
				start+=1
				print "Start"
				print start
				print i
			
			if start >0:
				min_length = i-start+1
			else:
				min_length = i-start

	return min_length


A=[2, 1, 1, 3, 2, 1, 1, 3]
out=solution(A)
print out