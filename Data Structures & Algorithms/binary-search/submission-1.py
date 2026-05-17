class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (right - left) // 2 + left #to establish the middle of nums
            if target == nums[middle]:
                return middle 
            elif target > nums[middle]: # the target is on the right hand side of middle, therefore we can get rid of left side values
                left = middle + 1 
            else:
                right = middle - 1 # target is on the left side, so rid of right side
        return -1