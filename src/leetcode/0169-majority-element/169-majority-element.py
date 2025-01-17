class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Topics: Array, Hash Table, Divide and Coquer, Sorting, Counting
        """     
        return Counter(nums).most_common(1)[0][0]
