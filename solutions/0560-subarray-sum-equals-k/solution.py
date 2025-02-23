class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        counter = 0
        dict = {}

        for n in nums:
            total += n

            if total == k:
                counter += 1
            
            if (total - k) in dict:
                counter += dict[total-k]
            
            if total in dict:
                dict[total] += 1
            else:
                dict[total] = 1
        return counter
        
