def solution(A):
	strokes=0
	l=0
	for i in range(0,len(A)):
		if A[i] > l:
			strokes += A[i]-l
			l = A[i]
		elif A[i]<l:
			l=A[i]
		if strokes > 1000000000:
			return -1
	return strokes

l=[5,8]
out=solution(l)
print out