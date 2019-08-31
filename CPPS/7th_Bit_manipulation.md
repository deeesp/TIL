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
        bit = [0]*32
        for num in nums:
            for j in range(32):
                bit[j] += num >> j & 1
        res = 0
        
        for i, val in enumerate(bit):
            if val > len(nums)//2:
                if i == 31:
                    res = -((1<<31)-res)
                else:
                    res |= 1 << i
        return res
        
        
    def majorityElement2(self, nums):
        ```
        Sorting
        Time: O(NlogN)
        Space: O(1)
        ```
        nums.sort()
        return nums[len(nums)//2]
        
```
