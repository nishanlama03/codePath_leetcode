"""""
Given a positive integer n, you can apply one of the following operations:

If n is even, replace n with n / 2.
If n is odd, replace n with either n + 1 or n - 1.
Return the minimum number of operations needed for n to become 1.
Tip: Java programmers should treat Integer.MAX_VALUE() as a special case.


Example 1:
Input: n = 8
Output: 3
Explanation: 8 -> 4 -> 2 -> 1
memo[8] = 3
16 -> memo[8

Example 2:
Input: n = 7
Output: 4
Explanation: 7 -> 8 -> 4 -> 2 -> 1
or 7 -> 6 -> 3 -> 2 -> 1

Example 3:
Input: n = 4
Output: 2
'''
"""

"""
Understand
input: integer
output: int
edge cases: input=0

Match
Memoization
Recursion

Plan/Psuedo
-------memo--------
-If even divide by 2
-If odd replace with either n + 1 or n -1

initialize 
memo[0] = 0
memo[1] = 0
memo[2] = 1
memo[3] = 
memo[2] = memo[n-1] + 1
memo[3] = memo[]
main (number):
	# keep memo in local fn scope
	memo = {} -> key = value we run into, val = number of ops it takes to go to 1

	recursion method(number)
		if number is 1 -> ret 0
		if number is 0 -> return 1
		
		if our number is in the memoization table -> return memo[number]

		if number is even
			memo[number] = 1 + recursion(number / 2)
			
		now we know that number's odd
			memo[number] = 1 + min(recursion(n + 1), recursion(n - 1))

		return the value of the number in memoization table
return recursion(number)

Implement


Review


Evaluate


"""
memo = {}
def recursion(num):
    # base cases
    if num == 1:
        return 0
    if num == 0:
        return 1

    if num in memo:
        return memo[num]
    
    if num % 2 == 0: # log n
        memo[num] = 1 + recursion(num / 2)
    else: # log n + log n
        memo[num] = 1 + min(recursion(num+1), recursion(num-1))
	# 12 -> 6 -> 3 -> 4 or 2 -> 1

    return memo[num]

# time complexity: O(log n)
# O(n + n) = O(n)