class Solution(object):
    def isToeplitzMatrix(self, matrix):

        for i in range(0,len(matrix)-1):
            for j in range(0, len(matrix[0])-1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        return True

        

S = Solution()
nums = [[18],[66]]
out = S.isToeplitzMatrix(nums)
print(out)