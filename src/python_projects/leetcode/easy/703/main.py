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
        if len(self.nums) == 0:
            self.nums.append(newValue)
        else:
            # insert newValue into the right position in nums
            for index, value in enumerate(self.nums):
                if value < newValue:
                    # found the position!
                    self.nums.insert(index, newValue)
                    return index


    def add(self, val):
        """
        :type val: int
        :rtype: int
        """


        if len(self.nums) <= self.k:
            self.insertValueInNums(val)
            return val

        if val < self.nums[-1]:
            return self.nums[-1]

        # place val into the list and drop the last one
        self.insertValueInNums(val)
        self.nums.pop()
        return self.nums[-1]


def testInput(input):
    # [[1,[]],[-3],[-2],[-4],[0],[4]]

    for index, aList in enumerate(input):
        if index == 0:
            initialList = input[0]
            k = initialList[0]
            nums = initialList[1]
            obj = KthLargest(k, nums)
            print("k: ", k)
            print("nums: ", nums)
        else:
            result = obj.add(aList[0])
            obj.printStuff("After adding " + str(aList[0]))
            print("result:", result)

# Your KthLargest object will be instantiated and called as such:
# FAILING AT: [[2,[0]],[-1],[1],[-2],[-4],[3]]
# Expect: [null,-1,1,0,0,1]
input = [[2,[0]],[-1],[1],[-2],[-4],[3]]
testInput(input)
