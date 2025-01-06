class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
      # declare a variable that tracks the left side
      # the idea is to move all the non zero vaules to the left 
      l=0

      for i in range(len(nums)):
    #checks to see if nums[i] is 0