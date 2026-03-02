# Q1. Concatenation of Array
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums[:]
        ans.extend(nums)
        return ans
    
# Another Solution
        # return nums * nums
        # return nums * 2