'''
https://leetcode.com/problems/group-anagrams/

p 49. Group Anagrams

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        """
        아나그램 집합! input의 문자가 중복이 될수도 있지 않을까?
        # 중요한 아이디어
        # dictionary key에 tuple 이 들어갈 수 있는 것
        # value 에 list가 들어갈 수 있고 append도 가능하다는 것        
        
        Time: O(NMlogM)
        Space: O(NM)
        
        """
        
        answer = {}
        
        for s in strs:
            key = tuple(sorted(s))
            if key not in answer:
                answer[key] = [s]
            else:
                answer[key].append(s)
        return answer.values()
            
