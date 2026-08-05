class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        queued_temps = []
        result = [0] * len(temperatures)

        for i, t in enumerate(temperatures):

            while queued_temps and queued_temps[-1][0] < t:
                qt, qi = queued_temps.pop()
                result[qi] = i - qi
            
            queued_temps.append((t, i))
        
        return result