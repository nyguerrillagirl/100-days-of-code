# Given an integer array nums, return true if any value appears at least
# twice in the array, and return false if every element is distinct.

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        uniqueMap = {}
        foundDuplicate = False
        for item in nums:
            # if found in uniqueMap - exit with answer
            if item in uniqueMap:
                foundDuplicate = True
                break
            else:
                uniqueMap[item] = item
        return foundDuplicate


solution = Solution()
nums = [1,1,1,3,3,4,3,2,4,2]
result = solution.containsDuplicate(nums)
print("result: ", result)