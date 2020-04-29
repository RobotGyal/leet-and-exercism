### RESTATE ###
# In a list, return the fifth largest problem

### QUESTIONS ###
# Is the list sorted
# do we count duplicates

### ASSUMPTIONS ###
# whole = int

## SOLVE ### 
# sort list
# find last index value
# reurn value at index - 5


nums = [2, 3, 76, 1, 34, 98, 45, 2, 8]

def fifthLargest(nums):
    """
    Returns the fifth largest number in a array of n numbers
    """
    nums.sort()
    return nums[-5]

fifthLargest(nums)