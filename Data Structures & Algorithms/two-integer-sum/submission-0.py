class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        check = {}

        for index, val in enumerate(nums):

            if val in check:
                return [check[val], index]
            else:
                check[target - val] = index