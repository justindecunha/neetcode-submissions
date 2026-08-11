class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        ans = set()

        for i in range(len(nums)):

            left = i + 1
            right = len(nums) - 1

            while left < right:
            
                candidate = nums[i] + nums[left] + nums[right]
                if candidate == 0:
                    ans.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1

                elif candidate > 0:
                    right -= 1
                else:
                    left += 1
        
        return list(ans)