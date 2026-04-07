class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash =set(nums)
        return not (len(hash) == len(nums))

         