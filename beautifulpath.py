#	9, [[1, 10], [1, 6], [2, 8], [3, 5]])

def  max_florists(path_length, florist_intervals):
	#print florist_intervals

	l = []

	for i in florist_intervals:
		#print i
		l.append(range(i[0],i[1])+1)
	print l

	intersect = l[0]
	#print len(l)

	#counter
	count = 1
	cl = 0
	t_temp = []
	c = 1
	for j in range(1,len(l)):

		
		temp = []
		for i in set(l[0]).intersection(set(l[j])):
			temp.append(i)
		print temp
		t_temp.append(temp)
		print t_temp
		if temp in t_temp:
			cl+=1

		print cl
		if cl >=3:
			return c

		if temp and temp not in t_temp:
			count+=1

		c+=1
		if count >=3:
			return c
	return c

out = max_florists(5, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]])
print out