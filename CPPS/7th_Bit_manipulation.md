# Chapter 4

## Q2. 136. Single Number
https://leetcode.com/problems/single-number/
---

```
class Solution:
    def singleNumber1(self, nums: List[int]) -> int:
        ## XOR
        ## Time: O(N)
        ## Space: O(1)
        sol = 0
        for num in nums:
            sol ^= num
        return sol
```


## Q4. 169. Majority Element
https://leetcode.com/problems/majority-element/
---

```
class Solution:
    def majorityElement1(self, nums):
        ```
        Bit Manipulation
        Time: 
        Space: 
        ```
        
        
    def majorityElement2(self, nums):
        ```
        Sorting
        Time: O(NlogN)
        Space: O(1)
        ```
        nums.sort()
        return nums[len(nums)//2]
        
```
