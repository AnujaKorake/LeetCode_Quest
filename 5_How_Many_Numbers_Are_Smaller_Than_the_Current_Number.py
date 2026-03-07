class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j] <  nums[i]:
                    count += 1
            result.append(count)

        return result

#chatgpt solution:


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        rank = {}

        for i, num in enumerate(sorted_nums):
            if num not in rank:
                rank[num] = i

        return [rank[num] for num in nums]