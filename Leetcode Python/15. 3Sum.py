class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums) # Reduce calculating length again
        nums.sort() 
        result = [] # Output
        for i in range(len(nums) - 2):
            if (nums[i] > 0):
                break
            if (nums[i] + nums[n - 1] + nums[n - 2] < 0):
                continue
            if i > 0 and nums[i] == nums[i - 1]: # Avoid duplicate elements using i - 1
                continue
            l = i + 1
            r = n - 1
            while l < r:
                temp = nums[i] + nums[l] + nums[r]
                if temp == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    while l + 1 < r and nums[l + 1] == nums[l]:
                        l += 1
                    l += 1
                    while l < r - 1 and nums[r] == nums[r - 1]:
                        r -= 1
                    r -= 1
                elif temp > 0:
                    r -= 1
                else:
                    l += 1

        return result
s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
