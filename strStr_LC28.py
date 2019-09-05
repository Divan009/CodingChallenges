def strStr(self, haystack: str, needle: str) -> int:
        
    if len(needle) > len(haystack):
        return -1
    if len(needle) == 0:
        return 0
    
    i = 0
    j = 0
    while i < len(haystack) and j < len(needle):
        if haystack[i] != needle[j]:
            i += 1 - j
            j = 0
        else:
            i += 1
            j += 1
    return i-j if j == len(needle) else -1