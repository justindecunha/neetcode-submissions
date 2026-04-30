class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
    
        solution = []
        def dfs(prefix=[], remaining=set(nums)):

            nonlocal solution

            if not remaining:
                solution.append(prefix)
                return
            
            for i in remaining:
                dfs(prefix + [i], remaining - {i})

        dfs()

        return solution
        


