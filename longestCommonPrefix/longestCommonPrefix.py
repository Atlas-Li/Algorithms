def longestCommonPrefix(v: list[str]) -> str:
    
    ans = ""
    v = sorted(v)
    
    f = v[0]
    l = v[-1]

    for i in range(min(len(f), len(l))):
        if f[i] == l[i]:
            ans += f[i]
        else:
            break
    
    return ans


if __name__ == "__main__":
    v = ["flower","flow","flight"]
    ans = longestCommonPrefix(v)
    print(ans)
    
    