'''
Problem 1: Substring

Write a function that takes in two strings and returns True if the second string is a substring of the first, and False otherwise.

NOTE: You may not use the in operator (Python) or call a library function that tests for substrings, such as substring() or indexOf() (Java).

Example 1:
Input: laboratory, rat
Output: true

Example 2:
Input: cat, meow
Output: false 

Understand:
- Check if the second string is a substring of the first
- What is the time and space complexity? O(n)?
- Edge case: Empty string for either 
- Edge case: the length of the substring is greater than the string

Match
- Pointers: Iterate through the string and compare with a pointer pointing at the substrin
- sliding window
- for loops

Plan
brute force O(n^2) - nested for loops
pointer soln O(n)

Pseudocode
pointer = track substring index 
edge cases -> which edge case checks and how?
for each char in string
    check if i == substring we are pointing ar
        if 
    

# strings = anteater
# substring ant
def subString(strings, substring):
    pointer = 0
    if len(strings) < len(substring):
        return False
    for char in strings:
        if char == substring[pointer]:
            pointer += 1 
		    if len(substring) == pointer:
			    return True
		else:
			pointer = 0
    return False
	



Implement


Review
- 

Evaluate
'''

# strings = anteater
# substring ant
'''
def subString(strings, substring):
    pointer = 0
    if len(strings) < len(substring):
        return False
    for char in strings:
        if char == substring[pointer]:
            pointer += 1 
		    if len(substring) == pointer:
			    return True
		else:
			pointer = 0
    return False
	
'''
