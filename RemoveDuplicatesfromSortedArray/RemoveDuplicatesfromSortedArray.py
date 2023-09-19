def removeDuplicates(nums: list[int]) -> int:
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1
    return j, nums[:j]
    

if __name__ == '__main__':
    a = [1, 1, 2, 2, 3, 3, 4, 4, 5]
    num, nums = removeDuplicates(a)
    print(num)
    print(nums)