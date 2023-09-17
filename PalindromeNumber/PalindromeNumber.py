def isPalindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]

if __name__ == "__main__":
    print(isPalindrome(121))
    print(isPalindrome(-121))
    print(isPalindrome(10))
    print(isPalindrome(-101))
    print(isPalindrome(0))
    print(isPalindrome(11))
    