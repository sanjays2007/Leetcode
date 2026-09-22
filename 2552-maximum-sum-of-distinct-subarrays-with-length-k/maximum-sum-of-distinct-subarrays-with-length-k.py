class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        freq = {}
        window_sum = 0
        max_sum = 0

        for i in range(len(nums)):
            # Add current element
            window_sum += nums[i]
            freq[nums[i]] = freq.get(nums[i], 0) + 1

            # Remove element if window becomes larger than k
            if i >= k:
                left = nums[i - k]
                window_sum -= left

                freq[left] -= 1

                if freq[left] == 0:
                    del freq[left]

            if i >= k - 1 and len(freq) == k:
                max_sum = max(max_sum, window_sum)

        return max_sum