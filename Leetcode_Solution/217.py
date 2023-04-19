class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count_table = set()
        for num in nums:
            if num not in count_table:
                count_table.add(num)
            elif num in count_table:
                return True
        
        return False