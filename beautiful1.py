def  max_florists(path_length, florist_intervals):
	#print florist_intervals

	k = 0
	count =0
	acc = 1
	print florist_intervals[k]
	for i in range(1, len(florist_intervals)):
		print count 
		if count>3:
			break
		if florist_intervals[k][1] < florist_intervals[i][1] and florist_intervals[k][1] > florist_intervals[i][0]:

			count+=1
		elif florist_intervals[k][1] == florist_intervals[i][1] and florist_intervals[k][1] == florist_intervals[i][0]:
			count+=1
		
		else:
			acc+=1

	
		k+=1	
		# if count <= 3:
		# 	print acc
		# else:
		# 	print count
	print acc
	

	#l = []

	#for i in florist_intervals:
		#print i
		#l.append(range(i[0],i[1]+1))
	#print l

	#intersect = l[0]
	#print len(l)

	#counter
	count = 1
	cl = 0
	t_temp = []
	c = 1

	'''
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
	'''

out = max_florists(5, [[0, 5], [0, 5], [0, 5], [0, 5], [0, 5], [5, 6], [6, 7]])
print out