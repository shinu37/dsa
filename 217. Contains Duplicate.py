class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)-1):
            nums.sort()
            if nums[i] == nums[i+1]:
                return True
        return False
