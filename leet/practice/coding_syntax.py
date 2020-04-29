### QUESTION 1 ###
## Given a list of n numbers, determine if it contains any duplicate numbers. ##


# go through list
# if that item in in the list, print true
# else keep looking until it is true
# if it’s all false, return none

# setup test variables
nums = [1, 23, 4, 52, 12, 4, 0, 5]

# write function
def duplicates(nums):
    """
    # description
    Vars: {nums: list}
    """
    for i in range(len(nums)):
        if nums.count(nums[i]) > 1:
            print("The duplicate is:" , nums[i])
            return nums[i]


# Testing...
duplicates(nums)

# ---------------------------------------------------------------------------------------------------------------- #

### QUESTION 2 ###

## Find the middle item in a singly linked list, or two middle items if it contains an even number of nodes.# #

# make linked list
# traverse it until we get to tail 
# while transversing keep track of location =count
# get the half of the count and go to that index 
# if odd, return the value at index of half the length
# if even, return the value at the inde of half the length and length + 1
# Return middle_node.data, middle_node.next.data

