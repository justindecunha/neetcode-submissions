class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
	Interview flow:
	1. Clarify: restate problem, constraints, ambiguities. Ensure you fully understand the problem.
	2. Example: walk through a simple example.
	3. Brute force: explain approach + complexity.
	4. Optimal: explain insight, algorithm, data structures + complexity BEFORE coding.
	5. Code: narrate key decisions; don't code silently.
	6. Dry run: manually trace the code.
	7. Test: walk through normal + relevant edge cases.
	8. Complexity: ALWAYS state time/space complexity and why.

    i, j | i < j | max(price[j] - price[i])

    prices = [10,1,5,0,7,1]
               ^ ^
'''
        max_profit = 0
        i = 0

        for j in range(1, len(prices)):

            if prices[j] < prices[i]:
                i = j
            else:
                max_profit = max(max_profit, prices[j] - prices[i])

        return max_profit



    