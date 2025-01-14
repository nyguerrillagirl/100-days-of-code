def addNewValueToSortedList(nums, newValue):
    """
    This is a non-recursive algorithm to add an item to a sorted list
    :param nums:
    :param newValue:
    :return:
    """
    print("addNewValueToSortedList nums: ", nums)
    print("addNewValueToSortedList newValue: ", newValue)
    listSize = len(nums)
    if listSize == 0:
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

    if newValue > nums[0]:
        nums.insert(0, newValue)
        return nums

    if newValue < nums[-1]:
        nums.append(newValue)
        return nums

    # We need to find the right position of newValue within the array
    leftIndex = 0
    rightIndex = listSize - 1
    midIndex = leftIndex +(((rightIndex - leftIndex) + 1) // 2)
    newValueAddedFlag = False
    # debugcounter
    debugCounter = 0
    while not newValueAddedFlag:
        print("leftIndex:", leftIndex, "rightIndex:", rightIndex, "midIndex:", midIndex)
        debugCounter += 1
        if debugCounter >= 10:
            print("Exceeded while loop limit")
            break
        if leftIndex == (rightIndex-1):
            # only two value left
            if newValue > nums[leftIndex]:
                nums.insert(leftIndex, newValue)
            elif newValue > nums[rightIndex]:
                nums.insert(rightIndex, newValue)
            else:
                nums.insert(rightIndex+1, newValue)
            newValueAddedFlag = True
        if leftIndex == rightIndex:
            # make decision where newValue falls
            if newValue > nums[leftIndex]:
                nums.insert(leftIndex, newValue)
            else:
                nums.insert(leftIndex+1, newValue)
            newValueAddedFlag = True
        else:
            if newValue < nums[midIndex]:
                leftIndex = midIndex
            else:
                rightIndex = midIndex
        midIndex = leftIndex + (((rightIndex - leftIndex) + 1) // 2)
    return nums
# test the code
nums = [200, 175, 100, 30, 25]

newValue = 50

result = addNewValueToSortedList(nums, newValue)
print("result: ", result)