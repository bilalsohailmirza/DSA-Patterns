# Problem: Fruits in A Basket

# Description: 
# Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.

# You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

# Write a function to return the maximum number of fruits in both the baskets.

# input : "ssfrdsfj"
# output : 5 
# input2: a a b c b b a d

# calculate the length of string
# window start
# total fruit
# fruit_frequency ={}

#loop with windowend from 0 till end of string
    #right_fruit = str[window_end]
    # if right_fruit is not in fruit_frequency
        #add right_fruit
    # if right_fruit is in fruit_frequency increment

    #while fruit_frequency is greater than 2 
        #left_fruit  = str[window_start]
        #decrement the left fruit 
        #remove if zero
        #slide window_start right
    
def FruitBasket(string):
    n = len(string)
    window_start, total_fruit = 0,0
    fruit_frequency = {}

    for window_end in range(n):
        right_fruit = string[window_end]
        if right_fruit not in fruit_frequency:
            fruit_frequency[right_fruit] = 0

        fruit_frequency[right_fruit] +=1

        while len (fruit_frequency) >2 :
            left_fruit = string[window_start]
            fruit_frequency[left_fruit] -=1
            
            if fruit_frequency[left_fruit] == 0:
                del fruit_frequency[left_fruit]

            window_start += 1
        total_fruit = max(total_fruit, window_end -window_start +1)
    
    return total_fruit
    

print(FruitBasket("121")) #output: 3
print(FruitBasket("0122")) # output: 3
print(FruitBasket("12322")) # output: 4