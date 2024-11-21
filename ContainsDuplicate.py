class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i, n in enumerate(nums):
            for m in nums[i+1:]:
                if n == m:
                    return True 
                    
        return False