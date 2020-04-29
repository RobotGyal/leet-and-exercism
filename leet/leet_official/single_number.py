"""
Given a non-empty array of integers, every element appears twice except for one.
Find that single one.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

# √ 1. Restate the Problem! 
# √ 2. Ask Clarifying Questions (~3)
# √ 3. State Assumptions
# TODO 4. Think Out Loud (Brainstorming)

### RESTATE ###
# Find the number that only appears once in a list of numbers in pairs


### QUESTIONS ###
# Does every number appear only twice (== or >=)?
# Can we use pre-existing functions (ex. count())
# What type should the output be (int, array, etc.?)


## ASSUMPTIONS ###
# ...could do 'if' statemnt to see in num.count == 2, if not 
# ...could loop through every number and store it's count in another array....
# ...could turn into a dictionary with key as array value and value as count, and return when value is 1


# setup test variables
nums = [2,2, 8, 4, 4, 1, 1, 0, 0]

def singleNumber(nums):
    """
    Returns list consisting of single number answer

    Vars:
    nums: array[n]
    single: array[n]
    item: int
    """

    single = []
    for item in nums:
        if item in single:
            single.remove(item)
        else:
            single.append(item)
    return single



# testing...?
print(singleNumber(nums))