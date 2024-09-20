"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

"""
Understand: 
- Input: list of strings
- Task: Find the longest seq of characters that each word has.
- Output: str
- Edge cases: no common prefix -> "", input == [] -> "" 

Match:
-  Finding the longest substring only at the beginning
- use pointers
- for loops

Plan:
- observation: length of common prefix CANT > length of smallest word in the array
# ["hi", "hihi"]

find the smallest length word in the array
initialize pointer var
loop through smallest length word

and using a pointer to check each char is in the smallest length word
		matches w/ each word in the array

Pseudo:
n = len(arr)
prefix = '' -> start off w empty string and add on common letters

for char in the smallest word:
	counter = 0
    for word in arr:
        if word[char] == char:
            counter += 1
		else:
			return prefix
    if counter == n:
        add char to prefix
return prefix

Implement:
def prefix(arr):
    n = len(arr)
    prefix = ''

    for char in min(arr):
        counter = 0
        for word in arr:
            if word[char] == char:
                counter += 1
            else:
                return prefix
        if counter == n:
            prefix += char
    return prefix


Implement:

Review:
- Time
- Space
- Other

Evaluate:
- Test cases

"""
def prefix(arr):
    n = len(arr)
    prefix = ''

    for char in min(arr):
        counter = 0
        for word in arr:
            if word[char] == char:
                counter += 1
            else:
                return prefix
        if counter == n:
            prefix += char
    return prefix