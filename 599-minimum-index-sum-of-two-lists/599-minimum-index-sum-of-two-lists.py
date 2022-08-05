class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = []
        min_idx = 2 * 10**3
        for menu in set(list1).intersection(set(list2)):
            idx_sum = list1.index(menu) + list2.index(menu)
            if min_idx > idx_sum:
                min_idx = idx_sum
                ans = [menu]
            elif min_idx == idx_sum:
                ans.append(menu)
        return ans
                