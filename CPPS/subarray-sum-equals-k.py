"""
https://leetcode.com/problems/subarray-sum-equals-k/

p 560. Subarray Sum Equals K

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2

Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""

class Solution:
    '''
    Time: O(N)
    Space: O(N)
    '''
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        연속 부분집합의 합이 k인 부분집합의 개수
        부분집합의 길이가 미정
        길이가 1이어도 되나?
        될거야
        
        [1,3,5,7,8,9]  15
        '''
        count, cur, res = {0: 1}, 0, 0
        for num in nums:
            cur += num
            res += count.get(cur - k, 0)
            count[cur] = count.get(cur, 0) + 1
        return res
