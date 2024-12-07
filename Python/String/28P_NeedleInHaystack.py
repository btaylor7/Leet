def needleinhaystack(haystack, needle):
    if len(needle) > len(haystack) or needle == "":
        return -1
    else:
        for i in range(len(haystack) - len(needle) + 1): #Last index where needle can start
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1

#Haystack=sadbutsad, needle=sad
#if haystack[0:3] == needle on first iteration
#i is 0, i + len(needle) = 0 : 0 + 3 (which is 3) so from 0 to but not including 3