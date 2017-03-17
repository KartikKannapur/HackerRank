# #Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# #You may assume that each input would have exactly one solution, and you may not use the same element twice.


TIME TAKEN - 645 ms
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                
                if i != j:
                    if nums[i] + nums[j] == target:
                        return [i,j]

TIME TAKEN - 525 ms
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        dict_result = {}
        for i in range(0, len(nums)):
            if (target - nums[i]) in dict_result.values():
                var = dict_result.keys()[dict_result.values().index((target - nums[i]))]
                if var != i:
                    return [i, var]
            dict_result[i] = nums[i]
 

TIME TAKEN - 516 ms
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        dict_result = {}
        for i in range(0, len(nums)):
            if (target - nums[i]) in dict_result.keys():
                if dict_result[(target - nums[i])] != i:
                    return [dict_result[(target - nums[i])], i]
            dict_result[nums[i]] = i
      
