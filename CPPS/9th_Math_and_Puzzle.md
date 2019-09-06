# Chapter 6 Mathematics and Puzzles

## Q1. 7. Reverse Integer

https://leetcode.com/problems/reverse-integer/

```python
class Solution:

    '''
    Time: O(log10N)
    Space: O(1)
    '''
    def reverse2(self, x: int) -> int:
        sign=-1 if x<0 else 1
        abs_x = x*sign
        answer = 0
        
        while(abs_x):
            abs_x, deno = divmod(abs_x,10)
            answer = answer*10 + deno
        if 2**31<answer: return 0
        
        return sign*answer
        

   '''
   Time: O(N)
   Space: O(1)
   '''
    def reverse1(self, x: int) -> int:
        sign=-1 if x<0 else 1
        abs_rvrsd = int(str(sign*x)[::-1])
        if 2**31<abs_rvrsd: return 0
        return sign*abs_rvrsd
```



## Q2 9. Palindrome Number
https://leetcode.com/problems/palindrome-number/

```python


```



## Q3 29. Divide Two Integers
https://leetcode.com/problems/divide-two-integers/

```python

```



## Q4 202. Happy Number
https://leetcode.com/problems/happy-number

```python

```
