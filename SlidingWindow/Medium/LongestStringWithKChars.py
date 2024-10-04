
# Longest Substring with K Distinct Characters

# Description: Given a string, find the length of the longest substring in it with no more than K distinct characters.

# This problem uses the same concept of dynamic window length

# Example1: string = "araaci" K = 1 Answer: 2
# Example2: string = "araaci" K = 2 Answer: 4
# 
# we can create a dictionary to keep track of no. of occurences of a character so far
# char_occurences = {
#   "a": 3
#   "r": 1
#   
# }

# function LongestSubstringWithKDistinctChars(string, K)
    # calculate the length of the string
    # window_start = 0
    # max_length = 0
    # char_frequency = {}

    # loop with window_end from 0 till length of the string
        # right_char = str[window_end]
        # if right_char is not in char_frquency
            # we will add the key with the name of right char in char_frequency
        # increment the count of that character in char_frequency

        # loop till our window_size is greater than K
            # left_char = str[window_start]
            # decrement the count of occurence of left_char
            # if occurence is zero than delete the key
            # increment the window_start variable

        # calculate the max_length


def LongestSubstringWithKDistinctChars(string, K):
    n = len(string)
    window_start, max_length = 0, 0
    char_frequency = {}

    for window_end in range(n):
        right_char = string[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0

        char_frequency[right_char] +=1

        while len(char_frequency) > K:
            left_char = string[window_start]
            char_frequency[left_char] -= 1

            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            
            window_start += 1
        
        max_length = max(max_length, window_end - window_start + 1)

    return max_length


print(LongestSubstringWithKDistinctChars("araaci", 1)) # output: 2
print(LongestSubstringWithKDistinctChars("araaci", 2)) # output: 4
print(LongestSubstringWithKDistinctChars("cbbebi", 3)) # output: 5