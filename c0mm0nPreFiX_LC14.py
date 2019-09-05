# Solution 1
# We use all() and startswith() fn. It first finds the shortest word 
# in the I/P array, then iterates each character of the shortest word
# to find out whether the char is common to the rest of words.
# O(S) time where S is the total number of characters for all the words
# in the array, O(1) space.

def longestCommonPrefix(strs):
	longest_pre = ""
	if not strs:
		return longest_pre
	shortest_str = min(strs, key=len)
	# we want to compare prefix with the shortest word
	for i in range(len(shortest_str)):
		# checking if the first letter of all words are same
		if all([x.startswith(shortest_str[:i+1]) for x in strs]):
			#if above is True, then add to longest_pre
			longest_pre = shortest_str[:i+1]
		else:
			break
	return longest_pre

#Runtime: 28 ms, faster than 20.10% of Python online submissions for Longest Common Prefix.
#Memory Usage: 11.7 MB, less than 98.75% of Python online submissions for Longest Common Prefix.


# Solution 2:
def longestCommonPrefix(strs):
	if not strs:
		return ""
	shortest_str = min(strs, key=len)
	for i, char in enumerate(shortest_str):
		for other in strs:
			if other[i] != char:
				return shortest_str[:i]
	return shortest_str

# Runtime: 16 ms, faster than 91.52% of Python online submissions for Longest Common Prefix.
# Memory Usage: 11.9 MB, less than 78.75% of Python online submissions for Longest Common Prefix.

#Solution 3:
def LongestCommonPrefix(strs):
    letter_g, longest_pre = zip(*strs), ""
    print(letter_g, longest_pre)
    for letter in letter_g:
        if len(set(letter)) > 1:
            break
        longest_pre += letter[0]
    return longest_pre

# Runtime: 32 ms, faster than 11.25% of Python online submissions for Longest Common Prefix.
# Memory Usage: 11.9 MB, less than 78.75% of Python online submissions for Longest Common Prefix.