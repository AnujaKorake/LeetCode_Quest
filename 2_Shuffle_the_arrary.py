# My 1st logic

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l = len(nums)
        nums1 = nums[:l//2]
        nums2 = nums[l//2:]
        ans = []
        big = len(nums1) if len(nums1) >= len(nums2) else len(nums2)
        for i in range(big):
            ans.append(nums1[i])
            ans.append(nums2[i])

        return ans
    
# simplest logic

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(n):
            ans.append(nums[i])      # Take x_i
            ans.append(nums[i+n])    # Take y_i
        return ans