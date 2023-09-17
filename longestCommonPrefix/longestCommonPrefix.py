'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string ""
'''

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
    vv = longestCommonPrefix(v)
    print(vv)
    
    