def isValid(s: str) -> bool:
    stack = []
    for i in s:
        if i in "([{":
            stack.append(i)
        else:
            if not stack \
                or (i == ')' and stack[-1] != '(') \
                or (i == ']' and stack[-1] != '[') \
                or (i == '}' and stack[-1] != '{'):
                return False
            stack.pop()
        
    return not stack


if __name__ == "__main__":
    print(isValid("()"))        # True
    print(isValid("()[]{}"))    # True
    print(isValid("(]"))        # False
    print(isValid("([)]"))      # False
    print(isValid("{[]}"))      # True
    print(isValid("]"))         # False
    print(isValid("(("))        # False