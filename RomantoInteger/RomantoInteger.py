def romanToInt(s: str) -> int:
    sv = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    ans = 0

    for i in range(len(s)):
        if i < len(s)-1 and sv[s[i]] < sv[s[i+1]]:
            ans -= sv[s[i]]
        else:
            ans += sv[s[i]]

    return ans

if __name__ == "__main__":
    roman = "LVIII"     # 58
    print(romanToInt(roman))
    roman = "MCMXCIV"   # 1994
    print(romanToInt(roman))