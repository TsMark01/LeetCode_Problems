class Solution(object):
    def twoSum(self, nums, target):
        num_dict = {}
        for i, num in enumerate(nums):

            x = target - num


            if x in num_dict:

                return [num_dict[x], i]


            num_dict[num] = i

        return None