# Probelem: No-Repeat Problem

# Description: 
# Given a string, find the length of the longest substring which has no repeating characters.

# Example: string = "aabccbb" Output: 3
# Example2: string = "abbbb" Output: 2
# Example3: string = "sbrebypwbcsdwabxnerypansg"

# Algorithm:

# calculate the length
# set the window start 0
# max length 
# empty dict 

# loop through the window end in range length
#   right char = str[window_end]
#   if right_char is not in char_dict
        # we will add the key with its position
#   if (char_dict[right_char] < str[window_end])
        # window_start will be set to to char_dict[right_char] +1 
#   max length = max length, window-end - window_start +1 
#return max length


def NoRepeatString(string):
    n = len(string)
    window_start, max_length = 0,0
    char_position = {}

    for window_end in range(n):
        right_char = string[window_end]
        
        if right_char in char_position:
            window_start = max(window_start, char_position[right_char] + 1)
            
        char_position[right_char] = window_end

        max_length = max(max_length, window_end - window_start + 1)

    return max_length

print(NoRepeatString("sbrebypwbcsdwabxnerypansg"))

print(NoRepeatString("aabccbb"))

