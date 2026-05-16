class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        nums1 = nums[::-1]
        nums.extend(nums1)
        return nums

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna