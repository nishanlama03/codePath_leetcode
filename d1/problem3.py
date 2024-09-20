'''
Given two binary strings a and b, return their sum as a binary string.


Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

Understand
- Input: two strings representing binary numbers
- Output: a string representing the sum of the binary numbers
- Edge case: what if numbers are not binary (prob dont have to worry about)
    strings of different length

Match
- adding base 10 numbers
- looping backwards over string
- add leading zeros to shorter string
- 

Plan/Pseudo 
# Adjust input strings so that they're the same length
if len(a) > len(b):
    max_input = a
    min_input = b
else:
    max_input = b
    min_input = a

#Add leading zeros
for i in range(len(max_input) - len(min_input)):
    min_input = "0" + min_input

#reverse adding
remainder = 0
output = ''
for i in range(len(max_input):: - 1): ? does this go in reservse?
    summing = max_input[i] + min_input[i] + remainder
    if summing > 1:
        remainder = 1
        output = '0' + output
    else:
        output = '1' + output

if remainder == 1:
    output = '1' + output
return output


Implement


Review

Evaluate



'''

