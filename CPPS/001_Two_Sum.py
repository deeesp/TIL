'''
https://leetcode.com/problems/two-sum/

1.  Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''



class Solution:
    
    '''
    1. Brute-Force
    Time: O(N^2)
    Space: O(1)
    '''
    def twoSum1(self, nums: List[int], target: int) -> List[int]:    
        for idx in range(len(nums)):
            for i in range(idx+1,len(nums)):
                if nums[idx] + nums[i] == target:
                    return [idx, i]
        return []
    
    '''
    2. One-Pass Hash Table
    Time: O(N)
    Space: O(N)
    '''
    def twoSum2(self, nums, target):
        d = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in d:
                return [d[diff], idx]
            else:
                d[num] = idx # {key <-> value switch}
        return []
