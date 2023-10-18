class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        list1 = []
        for i in nums:
            list1.append(i**2)
            list1.sort()
        return list1
