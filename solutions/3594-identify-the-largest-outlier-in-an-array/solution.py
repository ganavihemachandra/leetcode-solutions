class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        outlier = float('-inf')
        total_sum = sum(nums)
        counts = Counter(nums)
        res = 0

        for n in nums:
            total_sum -= n
            counts[n] -= 1
            if total_sum % 2 == 0 and counts[total_sum // 2] > 0:
                outlier = max(outlier, n)
            total_sum +=n
            counts[n] +=1
        return outlier
        
