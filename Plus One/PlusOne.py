def plusOne(digits: list[int]) -> list[int]:
    for i in range(len(digits)-1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] = digits[i] + 1
            return digits
    return [1] + digits
    
   
if __name__ == "__main__": 
    a = [1,2,9]
    b = plusOne(a)
    print(b)