def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)

    return ()

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums, target))