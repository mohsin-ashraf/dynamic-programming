
def stair_climbing_ways(N):
	if N == 1: return 1 # Base case 1
	if N == 2: return 2 # Base case 2
	if N == 3: return 4 # Base case 3

	# Above are the base cases for this recursive problem.

	# Calling recursively the sub problems.
	return stair_climbing_ways(N-1) + stair_climbing_ways(N-2) + stair_climbing_ways(N-3)


print ("Number of ways to climb 3 stairs: {}".format(stair_climbing_ways(3)))
print ("Number of ways to climb 10 stairs: {}".format(stair_climbing_ways(10)))
print ("Number of ways to climb 15 stairs: {}".format(stair_climbing_ways(15)))

