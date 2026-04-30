class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        '''
        [1,2,1,0,1]
        [1,1,1,1,0]
        '''


        is_reachable = [False] * len(nums)

        def dfs(i: int):

            if i >= len(nums): return
            if is_reachable[i]: return

            is_reachable[i] = True

            for jump_length in range(1, nums[i] + 1):
                dfs(i + jump_length)

        dfs(0)

        return is_reachable[len(nums) - 1]