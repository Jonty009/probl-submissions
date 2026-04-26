class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums= sorted(nums)
        # print(nums)
        longest_seq,  current_seq = 1, 1
        if len(nums) in [0,1]:
            return(len(nums))
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
            elif nums[i] + 1 == nums[i+1]:
                current_seq += 1
            else:
                current_seq = 1
            if current_seq > longest_seq:
                    longest_seq = current_seq
            print(longest_seq, current_seq)
        return longest_seq

        