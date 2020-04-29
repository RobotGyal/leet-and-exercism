"""
Given an array of strings, group anagrams together.

All inputs will be in lowercase.
The order of your output does not matter.

EXAMPLE:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""

# √ 1. Restate the Problem! 
# TODO 2. Ask Clarifying Questions (~3)
# TODO 3. State Assumptions
# TODO 4. Think Out Loud (Brainstorming)

### RESTATE ###
# Create unique arrays that hold all words that are anagrams of each other in each array


### QUESTIONS ###
# will all strings be the same length
# can the strings contain spaces, multiple data types, etc


## ASSUMPTIONS ###
# The number of arrays created does not matter
# anagram also means the same size word


# setup test variables
vars = ["eat", "tea", "tan", "ate", "nat", "bat"]

import collections

def groupAnagrams(input):
    # ...could look at if the size is the same first
    ans = collections.defaultdict(list)
    for s in input:
        ans[tuple(sorted(s))].append(s)
    
    return ans.values()
    


# testing...?
print(groupAnagrams(vars))
