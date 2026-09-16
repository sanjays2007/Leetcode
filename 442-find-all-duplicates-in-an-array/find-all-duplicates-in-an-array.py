class Solution:
    def findDuplicates(self, nums):
        count = {}
        result = []

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        for num in count:
            if count[num] == 2:
                result.append(num)

        return result
