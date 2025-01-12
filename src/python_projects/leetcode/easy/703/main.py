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

    def insertValueInNums(self, newValue):
        for index, value in enumerate(self.nums):
            if value < newValue:
                # found the position!
                self.nums.insert(index, newValue)
                return index

        self.nums.append(newValue)

    def insertValueInSortedList(self, newValue):
        if len(self.nums) == 0:
            self.nums.append(newValue)


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
            self.insertValueInNums(val)
            return self.nums[-1]

        if val < self.nums[-1]:
            print("checking val ", val, " against the last element")
            return self.nums[-1]

        # place val into the list and drop the last one
        print("inserting into the list and dropping the last item")
        self.insertValueInNums(val)
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
# FAILING AT: [[3,[5,-1]],[2],[1],[-1],[3],[4]]
# Expect: [null,-1,1,1,2,3]
input = [[3,[5,-1]],[2],[1],[-1],[3],[4]]
testInput(input)
