class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums] #terminate recursion
        answer = [] #declare answer
        for i, num in enumerate(nums): #fix pivots
            n = nums[:i] + nums[i+1:]
            for y in self.permute(n):
                answer.append([num] + y)
        return answer
