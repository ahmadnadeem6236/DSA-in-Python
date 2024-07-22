# Contains Duplicates

from typing import List

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         seen = set()
#         for num in nums:
#             if num in seen:
#                 return True
#             seen.add(num)
#         return False


# nums = [1, 2, 3, 1]
# sol = Solution()
# print(sol.containsDuplicate(nums))


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            g = sorted(s.lower())
            c = sorted(t.lower())
            print(g, c)
            i = 0
            while i < len(g):
                if g[i] != c[i]:
                    return False
                i += 1
            else:
                return True
        else:
            return False


sol = Solution()
s = "anagram"
t = "nagaram"
print(sol.isAnagram(s, t))
