class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # Convert to set for O(1) lookups
        num_set = set(nums)
        longest_streak = 0

        for n in num_set:
            # Check if 'n' is the start of a sequence
            # If n-1 exists, 'n' is in the middle of a sequence, so we skip it
            if (n - 1) not in num_set:
                current_num = n
                current_streak = 1

                # Keep looking for the next numbers in the sequence
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak