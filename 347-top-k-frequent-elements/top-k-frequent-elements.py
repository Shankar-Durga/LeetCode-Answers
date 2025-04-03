class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequencies of each number
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Sort the keys based on frequency in descending order
        sorted_keys = sorted(freq, key=freq.get, reverse=True)
        
        # Return the first k elements
        return sorted_keys[:k]
