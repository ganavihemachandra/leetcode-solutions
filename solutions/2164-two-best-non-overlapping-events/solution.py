class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        starts = sorted(events, key = lambda i:i[0])
        ends = sorted(events, key = lambda i:i[1])

        max_val = 0
        res = 0
        end_idx = 0

        for i in range(len(starts)):
            while end_idx < len(ends) and ends[end_idx][1] < starts[i][0]:
                max_val = max(ends[end_idx][2], max_val)
                end_idx += 1
            
            res = max(res, max_val + starts[i][2])
        return res
        
