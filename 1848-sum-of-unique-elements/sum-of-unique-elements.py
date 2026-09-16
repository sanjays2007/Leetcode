class Solution:
    def sumOfUnique(self, nums):
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        total = 0

        for num in count:
            if count[num] == 1:
                total += num

        return total
