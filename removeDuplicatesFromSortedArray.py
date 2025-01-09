class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        u = []
        for i in nums:
            if i not in u:
                u.append(i)
    
        nums[:] = u 
        return len(u)  