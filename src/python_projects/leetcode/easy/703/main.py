class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = nums
        self.nums.sort(reverse=True)
        # Only keep the first k elements
        if len(self.nums) > k:
            # remove len-k from the end of the list
            removeCount = len(self.nums) - k
            while removeCount != 0:
                self.nums.pop()
                removeCount -= 1

    def printStuff(self, message):
        print(message)
        print("k: ", self.k)
        print("nums: ", self.nums)
        print("===================")

    def addValToSortedList(self, theList, newValue):
        nums = list(theList)
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
            newNums = self.addValToSortedList(leftNums, newValue)
            return newNums + rightNums
        else:
            leftNums = nums[leftIndex:midIndex]
            rightNums = nums[midIndex:]
            newNums = self.addValToSortedList(rightNums, newValue)
            return leftNums + newNums

    def addNewValueToSortedList2(self, newValue):
        """
        This is a non-recursive algorithm to add an item to a sorted list
        :param nums:
        :param newValue:
        :return:
        """
        print("addNewValueToSortedList nums: ", self.nums)
        print("addNewValueToSortedList newValue: ", newValue)
        listSize = len(self.nums)
        if listSize == 0:
            self.nums.append(newValue)
            return self.nums

        if listSize == 1:
            # Check where to place newValue
            if newValue > self.nums[0]:
                self.nums.insert(0, newValue)
            else:
                self.nums.append(newValue)
            return self.nums

        if listSize == 2:
            # Place first, new middle or end
            if newValue > self.nums[0]:
                self.nums.insert(0, newValue)
            elif newValue > self.nums[1]:
                self.nums.insert(1, newValue)
            else:
                self.nums.append(newValue)
            return self.nums

        if newValue > self.nums[0]:
            self.nums.insert(0, newValue)
            return self.nums

        if newValue < self.nums[-1]:
            self.nums.append(newValue)
            return self.nums

        # We need to find the right position of newValue within the array
        leftIndex = 0
        rightIndex = listSize - 1
        midIndex = leftIndex + (((rightIndex - leftIndex) + 1) // 2)
        newValueAddedFlag = False
        # debugcounter
        debugCounter = 0
        while not newValueAddedFlag:
            print("leftIndex:", leftIndex, "rightIndex:", rightIndex, "midIndex:", midIndex)
            debugCounter += 1
            if debugCounter >= 10:
                print("Exceeded while loop limit")
                break
            if leftIndex == (rightIndex - 1):
                # only two value left
                if newValue > self.nums[leftIndex]:
                    self.nums.insert(leftIndex, newValue)
                elif newValue > self.nums[rightIndex]:
                    self.nums.insert(rightIndex, newValue)
                else:
                    self.nums.insert(rightIndex + 1, newValue)
                newValueAddedFlag = True
            if leftIndex == rightIndex:
                # make decision where newValue falls
                if newValue > self.nums[leftIndex]:
                    self.nums.insert(leftIndex, newValue)
                else:
                    self.nums.insert(leftIndex + 1, newValue)
                newValueAddedFlag = True
            else:
                if newValue < self.nums[midIndex]:
                    leftIndex = midIndex
                else:
                    rightIndex = midIndex
            midIndex = leftIndex + (((rightIndex - leftIndex) + 1) // 2)
        return self.nums

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        # DEBUGGING
        print("adding ", val, "  to ", self.nums)
        if len(self.nums) == 0:
            self.nums.append(val)

        if len(self.nums) < self.k:
            print("just adding val:", val, " to the list")
            self.nums = self.addNewValueToSortedList2(val)
            return self.nums[-1]

        if val < self.nums[-1]:
            print("checking val ", val, " against the last element")
            return self.nums[-1]

        # place val into the list and drop the last one
        print("inserting into the list and dropping the last item")
        self.nums = self.addNewValueToSortedList2(val)
        print("BEFORE POP OF nums: ", self.nums)
        self.nums.pop()
        print("AFTER POP OF nums: ", self.nums)

        return self.nums[-1]


def testInput(input):
    print("testInput processing of: ", input)
    for index, aList in enumerate(input):
        print("index: ", index, " aList: ", aList)
        if index == 0:
            initialList = aList  # holds k and initial nums
            k = initialList[0]
            nums = initialList[1]
            print("initializing KthLargest...")
            obj = KthLargest(k, nums)
            print("k: ", k)
            print("nums: ", nums)
        else:
            result = obj.add(aList[0])
            print("**********")
            obj.printStuff("After adding " + str(aList[0]))
            print("result:", result)



# Your KthLargest object will be instantiated and called as such:
input = [[3,[5,-1]],[2],[1],[-1],[3],[4]]
testInput(input)
