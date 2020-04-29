"""
Given a list of n numbers, determine if it contains any duplicate numbers.
"""

### RESTATE ###
# find the number that appears more than once

### QUESTIONS ###
# what if there are multiple duplicates
# how should the data be output
#
#

## ASSUMPTIONS ###
# there is only 1 duplicate
#


### PSUEDOCODE ###
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