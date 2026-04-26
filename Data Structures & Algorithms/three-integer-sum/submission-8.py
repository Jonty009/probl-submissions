class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        # print('DEBUG: nums sorted:', nums)
        

        res = []

        for i, a in enumerate(nums):
            # print(f"DEBUG: i={i}, a={a}")

            if i>0 and a==nums[i-1]:
                continue

            l = i+1
            r = len(nums) - 1
            while l<r:
                sum = a + nums[l] + nums[r]
                # print(f"DEBUG: i={i}, l={l}, r={r}, sum={sum}")
                if sum<0:
                    l+=1
                elif sum>0:
                    r -= 1
                else:
                    res.append([a, nums[l], nums[r]])
                    # print(f"DEBUG: Found triplet: [{a}, {nums[l]}, {nums[r]}]")
                    l+=1
                    r -= 1
                    #Do duplicate check only after finding triplets and not after every run- very important
                    while nums[l] == nums[l-1] and l<r:
                        # print(f"DEBUG: Skipping duplicate at l={l}, nums[l]={nums[l]}")
                        l+=1
        return res