class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        i =1
        j =1
        n = len(nums)

        while i < n:
            if nums[i-1]==nums[i]:
                count+=1
            elif nums[i-1]!= nums[i]:
                count=1
            if count<=2:
                nums[j]=nums[i]
                j+=1
            i+=1
        return j
        