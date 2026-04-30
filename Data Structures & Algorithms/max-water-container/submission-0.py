class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # Size of a container:
        #. (j - i) * min(heights[i], heights[j])

        # two loops:
        # n^2?
        # n log(n)?

        max_container_size = -1
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                current_container_size = (j - i) * min(heights[i], heights[j])
                max_container_size = max(max_container_size, current_container_size)
        
        return max_container_size