# This tests a function that adds a new item to a sorted list
def addValToSortedList(nums, newValue):
    listSize = len(nums)
    if listSize == 0:
        # Just append to the empty list
        nums.append(newValue)
        return nums

    if listSize == 1:
        # Check where to place newValue
        if newValue > nums[0]:
            nums.insert(0, newValue)
        else:
            nums.append(newValue)
        return nums

    if listSize == 2:
        # Place first, new middle or end
        if newValue > nums[0]:
            nums.insert(0, newValue)
        elif newValue > nums[1]:
            nums.insert(1, newValue)
        else:
            nums.append(newValue)
        return nums
    # Now we split the list and decide which part to insert newValue
    # we recurse on the part it belongs in and paste the list returned back together
    leftIndex = 0
    leftValue = nums[leftIndex]
    rightIndex = len(nums) - 1
    rightValue = nums[rightIndex]
    midIndex = (rightIndex - leftIndex) // 2
    midValue = nums[midIndex]
    if newValue > midValue:
        leftNums = nums[leftIndex:midIndex]
        rightNums = nums[midIndex:]
        newNums = addValToSortedList(leftNums, newValue)
        return newNums + rightNums
    else:
        leftNums = nums[leftIndex:midIndex]
        rightNums = nums[midIndex:]
        newNums = addValToSortedList(rightNums, newValue)
        return leftNums + newNums


# test the code
nums = [200, 175, 100, 30, 25]
newValue = 50

result = addValToSortedList(nums, newValue)
print("result: ", result)
