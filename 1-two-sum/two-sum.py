class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen={}  #{value : index}
        for i in range(len(nums)):
            wanted=target-nums[i]

            if wanted in seen:
                return seen[wanted],i
            seen[nums[i]]=i