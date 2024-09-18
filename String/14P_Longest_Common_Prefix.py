class Solution(object):
    #Program that finds longest common prefix out of a list of strings.
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i, char in enumerate(shortest):
            for other in strs: #This will iterate over each string in the list and compare to each char.
                if other[i] != char: #If the character is not the same, return the prefix.
                    return shortest[:i] #[:i] Slice, no start index so default is shortest[0], end is i however i isnt included.
        return shortest

list = ["flower","flow","flight"]
solution = Solution()
print(solution.longestCommonPrefix(list)) #Output: fl