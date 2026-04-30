class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = [None] * len(nums)

        def dfs(i: int) -> int:

            if i >= len(memo):
                return 0

            if memo[i]:
                return memo[i]

            memo[i] = max(dfs(i + 1), nums[i] +  dfs(i + 2))    

            return memo[i]
        
        return dfs(0)
