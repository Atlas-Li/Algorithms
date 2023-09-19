def removeElement(nums: list[int], val: int) -> int:
    if len(nums) == 0:
        return 0

    count = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[count] = nums[i]
            count += 1

    return count, nums[:count]

if __name__ == "__main__":
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    
    print(removeElement(nums, val)[1])