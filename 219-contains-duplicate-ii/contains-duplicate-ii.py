class Solution:
    def containsNearbyDuplicate(self, nums, k):
        pos = {}

        for i in range(len(nums)):
            if nums[i] in pos:
                if i - pos[nums[i]] <= k:
                    return True

            pos[nums[i]] = i

        return False