class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        '''
            seen = {} (0, 3)
            [3,4,5,6], target = 7
             ^
            seen {
                4 -> 0
            }

            [3,4,5,6], target = 7
               ^
            seen {
                4 -> 0
            }
        '''

        for i, num in enumerate(nums):
            k = target - num
            if num in seen:
                return [seen[num], i]
            else:
                seen[k] = i

        return []