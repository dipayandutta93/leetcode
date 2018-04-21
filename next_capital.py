def  strengthen_passwords(passwords):

	new_list = []
	for s in passwords:
		s= list(s)
		
		for i in range(0,len(s)):
			if s[i].lower() == "s":
				s[i] = "5"
		#print s

		if len(s)%2 ==1 and len(s) != 1:
			if s[len(s)/2].isdigit():
				y=int(s[len(s)/2])*2
				x = str(y)
				x=list(x)
				del s[len(s)/2]
				s = s[:len(s)/2] + x + s[len(s)/2:]

		if len(s) % 2 == 0:
			temp = s[0]
			s[0] = s[len(s)-1]
			s[len(s)-1] = temp

			s[0]=s[0].lower() if s[0].isupper() else s[0].upper()
			s[len(s)-1]=s[len(s)-1].lower() if s[len(s)-1].isupper() else s[len(s)-1].upper()

		st=[x.lower() for x in s]
		st="".join(st)
		s=list(s)
		
		if "nextcapital" in st:
			index = st.index("next")

			j=index+3

			while index <= j:
				temp = s[j]
				s[j] = s[index]
				s[index] = temp
				index+=1
				j-=1
		new_list.append(s)
	new_list = ["".join(i) for i in new_list]
	return new_list

l=['GoCardinals', 'Doge', 'nExTcapITalxnextcapital', 'ThreeSThree']
out = strengthen_passwords(l)
print out

#['GoCardinal5', 'Eogd', 'TxEncapITalxnextcapital', 'Ehree10Thret']