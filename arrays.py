
from typing import List


class Solution:


    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            g = sorted(s.lower())
            c = sorted(t.lower())
            print(g,c)
            i = 0 
            while i < len(g):
                if g[i] != c[i]:
                    return False
                i+=1
            else:
                return True
        else:
            return False

            
            

            

    

    # def  print(self, nums):
    #     i = 0
    #     while i < len(nums):
    #         print(nums[i])
    #         i+= 1


    # def containsDuplicate(self, nums):
    #     j = 0
    #     while j < len(nums):
    #         pointer = nums[j]
    #         i = j
    #         while i < len(nums) - 1:
    #             if pointer == nums[i +1]:
    #                 return True
    #             i+=1
    #         j+=1
    #     else:
    #         return False
    # def containsDuplicate(self, nums: List[int]) -> bool: ## reduced time complexity
    #     # seen = set()
    #     # for num in nums:
    #     #     if num in seen:
    #     #         return True
    #     #     seen.add(num)
    #     # return False

    #     set_nums = set(nums)
    #     return len(set_nums) != len(nums)
            


# nums = [10,20,30,223, 45, 65, 300, 50]

sol = Solution()
# sol.print(nums)

# print(sol.containsDuplicate(nums))

print(sol.isAnagram("anagram","nagaram"))

print(sol.isAnagram("cat","tac"))


# print(sol.isAnagram("rat","car"))