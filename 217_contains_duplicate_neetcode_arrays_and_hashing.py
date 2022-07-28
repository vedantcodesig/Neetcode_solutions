class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        prevMap={}
        for i,n in enumerate(nums):
            if n in prevMap:
                return True
            prevMap[n]=i
        return False