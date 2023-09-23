def searchInsert(nums: list[int], target: int) -> int:
    n = len(nums)
    start, end = 0, n - 1
    
    while start <= end:
        mid = start + (end - start) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start
    
    
if __name__ == "__main__":
    nums = [1,3,5,6]
    target = 7
    
    print(searchInsert(nums, target))