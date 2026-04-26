class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        fw_multiplier, bw_multiplier = 1, 1
        pre_mul_list, suff_mul_list = [], []
        length = len(nums) 
        for n in range(length):
            if n==0:
                pre_mul_list.append(1)
                suff_mul_list.append(1)
                continue
            fw_multiplier *= nums[n-1]
            bw_multiplier *= nums[length-n]
            pre_mul_list.append(fw_multiplier)
            suff_mul_list.append(bw_multiplier)
        
        result = []
        for i in range(length):
            result.append(pre_mul_list[i] * suff_mul_list[length-i-1])
       
        # print(pre_mul_list, suff_mul_list, result)
        return result

        