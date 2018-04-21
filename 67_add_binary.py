class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        a=list(a)
        b=list(b)
        a = map(int, a)
        b = map(int, b)
        

        
        arr_len = max(len(a),len(b))+1
        k = arr_len -1

        if len(a)>len(b):
            for i in range(0,len(a)-len(b)+1):
                b = [0] + b
            a = [0] + a
        elif len(b)>len(a):
            for i in range(0,len(b)-len(a)+1):
                a = [0] + a
            b=[0]+b
        else:
            a=[0]+a
            b=[0]+b
        i = len(a)-1
        j = len(b)-1

        carry_out=0
        c = [0]*arr_len
        
        while k>=0:
            
            a_dig = a[i]
            b_dig = b[j]
            
            carry_in = carry_out
            c[k] = (int(a_dig+b_dig+carry_in))%2
            
            if(a_dig+b_dig+carry_in)>1:
                carry_out = 1
            else:
                carry_out = 0
            
            if i !=0:
                i=i-1
            if j !=0:
                j=j-1
            k-=1
        if c[0] == 0:
            del c[0]
        c = "".join(str(item) for item in c) 
        
S = Solution()
a = "11"
b = "1"
out = S.addBinary(a,b)
print out