class Solution(object):
    def searchInsert(self, nums, target):
        new_dict = {}
        index = -1
        for i in range(0, len(nums)):
            if target == nums[i]:
                index = i
        if index == -1 and target < nums[len(nums) - 1]:
            for i in range(0, len(nums)):
                if target < nums[i]:
                    index = i
                    break
        elif index == -1 and target > nums[len(nums) - 1]:
            index = len(nums)

        return index