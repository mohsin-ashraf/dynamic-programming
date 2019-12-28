# Problem Statement

Given that you can climb 1, 2 or 3 stairs with one step.
How many different ways can you climb N stairs. Where N can be any number

## Before moving to solution try to do it yourself.

## Recursive Solution.
We can solve the above problem recursively in few lines of code. First of all we have to consider the base cases of this problem, so there are three base cases for this problem.
1. When we only have to climb 1 stair given the conditions mentioned in the problem there is only one way to climb.
2. When we have to climb 2 stairs given the conditions mentioned in the problem there are two ways to do so which are given below.
* climb one stair at a time.
* climb two stairs at a time.
3. When we have to climb 3 stairs given the above conditions mentioned in the problem there are four ways to do so which are given below.
* climb on stair at a time.
* climb two stairs at first and then one stair afterword.
* climb one stair at first and then two stairs afterword.
* climb three stairs at once.

Now these base cases are right in place lets talk about the recursive step. Since we know for 1, 2 and 3 stairs how many ways are there to climb these stairs. We can find number of ways to climb stairs for any number *N* if we know how we can climb the *N - 3* stairs, *N - 2* and *N - 1* stairs. Eventually by reducing the *N* we will reach to the base cases and then we will move back up to the number *N*. Lets have a look at the following sudo code.

```
def function(N):
	if N == 1: return 1
	if N == 2: return 2
	if N == 3: return 4
	return function(N-1) + function(N-2) + function(N-3)
```

## Dynamic Programming Solution.
To solve the proble dynamically we have to consider base cases as we have discussed in recursive solution, and instead of making trees with recursive calls we can simply use 
an array to solve it. Have a look at the following sudo code for more information.
```
def function(N):
	ways = [0] * (N+1)
	ways[1] = 1 # Base case 1
	ways[2] = 2 # Base case 2
	ways[3] = 4 # Base case 3
	for i in range(4,N+1):
		ways[i] = ways[i-1] + ways[i-2] + ways[i-3]
	return ways[N]
```
