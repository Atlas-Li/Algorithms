def lengthOfLastWord(s: str) -> int:
        parts = s.split()
        return len(parts[-1])
    
    
if __name__ == "__main__":
    s = "Hello World "
    print(lengthOfLastWord(s))