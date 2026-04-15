def longest_palindrome(s):
    if not s:
        return""
    start,max_len = 0, 1
    for i in range(len(s)):
        len1 = expand(s,i,i)
        len2 = expand(s,i,i+1)
        curr_max = max(len1,len2)
        if curr_max > max_len:
            start = i - (curr_max - 1) // 2
            max_len = curr_max
    return s[start:start + max_len]

def expand(s,left,right):
    while left >= 0 and right< len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1
print(longest_palindrome("babad"))

