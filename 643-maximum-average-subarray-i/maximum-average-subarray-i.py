class Solution(object):
    def findMaxAverage(self, nums, k):
        # First window sum
        s = sum(nums[:k])
        maxi = s

        # Slide the window
        for i in range(k, len(nums)):
            s = s - nums[i-k] + nums[i]
            maxi = max(maxi, s)

        return maxi / float(k)