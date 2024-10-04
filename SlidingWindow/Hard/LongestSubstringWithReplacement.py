# Problem: Longest Substring with Same Letters after Replacement

# Problem Statement: 
# Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

# Example: aabbqcbb, K=2
#  window_end - window_start + 1 - max_count > K:
# stuff to find out:
# 1. Which letter has most occurences
# 2. We need to know that when in our execution we can have the longest substring
def LongestSubstringAfterReplacement(s, k):

    # calculate the length
    n = len(s)
    window_start = 0 
    max_letter_count = 0 
    char_frequency = {}
    max_substring = 0

    # char_frequency = {
    #     "a": 2,
    #     "b":1
    # }
    # max_letter_count = 2 

    #loop with window_end for length 
    for window_end in range(n):
        right_char = s[window_end]
    
        if right_char not in char_frequency:
            # add key
            char_frequency[right_char] = 0

        #increment count in char_frequency
        char_frequency[right_char] += 1

        #calculate the max char occurence within this window
        max_letter_count = max(max_letter_count, char_frequency[right_char])

        #check if window_end - window_start + 1 - max_count > K
        if window_end - window_start + 1 - max_letter_count > k:
            # shrink the window
            left_char = s[window_start]
            char_frequency[left_char] -=1
            # shift window
            window_start +=1
                
    #update the max_substring 
        max_substring = max(max_substring, window_end - window_start +1)

    return max_substring

string = "aabbqcbb"
result = LongestSubstringAfterReplacement(string, 2)
print(result)