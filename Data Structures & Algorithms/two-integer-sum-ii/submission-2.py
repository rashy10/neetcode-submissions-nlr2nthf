class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1

        while left < right:
            total = numbers[left] + numbers[right]
            if target == total:
                return [left+1,right+1]
            if target < total:
                right -= 1
                while numbers[right-1] == numbers[right]:
                    right -= 1
            else:
                left += 1
                while numbers[left+1] == numbers[left]:
                    left += 1
        