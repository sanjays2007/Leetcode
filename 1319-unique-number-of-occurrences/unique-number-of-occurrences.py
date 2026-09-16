class Solution:
    def uniqueOccurrences(self, arr):
        count = {}

        # Count occurrences
        for num in arr:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        seen = []

        # Check if occurrence counts are unique
        for value in count.values():
            if value in seen:
                return False
            seen.append(value)

        return True