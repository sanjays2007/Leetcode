class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        seen={}
        for i in range(len(numbers)):
            needed=target-numbers[i]
            if needed in seen:
                return seen[needed]+1,i+1
            seen[numbers[i]]=i