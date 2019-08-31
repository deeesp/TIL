# Chapter 4

## Q1. 136. Single Number
https://leetcode.com/problems/single-number/
---

```
class Solution:
    def singleNumber1(self, nums: List[int]) -> int:
        ## XOR
        ##
        Time: O(N)
        Space: O(1)
        ##
        sol = 0
        for num in nums:
            sol ^= num
        return sol
        
    def singleNumber2(self, nums: List[int]) -> int:
```
