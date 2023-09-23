Given a string ```s``` consisting of words and spaces, return the length of the __last__ word in the string.

A __word__ is a maximal substring consisting of non-space characters only.

## Example 1:
```bash
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
```

## Example 2:
```bash
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
```

## Example 3:
```bash
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
```

## Constraints:
* ```1 <= s.length <= 10^4```
* ```s``` consists of only English letters and spaces ```' '```.
* There will be at least one word in ```s```.