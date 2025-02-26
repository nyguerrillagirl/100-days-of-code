# This program compares the Fisher-Yates shuffle with a naive shuffle


def run_shuffle_good(n):
    pass

def permute(nums):
    def backtrack(start=0):
        if start == len(nums):
            result.append(nums[:])
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    result = []
    backtrack()
    return result



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1, 2, 3]
    permutations = permute(nums)
    print(permutations)


