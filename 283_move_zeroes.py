class Solution(object):
    def moveZeroes(self, nums):
        
        for i in range(0, len(nums)-1):
            if nums[i] == 0:
                for j in range(i+1,len(nums)):
                    if nums[j]!=0:
                        temp = nums[j]
                        nums[j] = nums[i]
                        nums[i] = temp
                        break
        print nums

        '''
        def moveZeroes(self, nums):
        zero = 0  # records the position of "0"
        for i in xrange(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
            print nums
        '''

S = Solution()
nums = [0, 1, 0, 3, 12]
out = S.moveZeroes(nums)
print(out)