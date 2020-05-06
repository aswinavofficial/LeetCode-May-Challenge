class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        
        mj = len(nums)//2
        
        if len(nums) == 1:
            return nums[0]
        
        for i in nums:
            if i in d.keys():
                d[i] = d[i] + 1
                if(d[i]) > mj:
                    return i
            else:
                d[i] = 1
        
