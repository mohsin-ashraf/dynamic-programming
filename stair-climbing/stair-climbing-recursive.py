
def stair_climbing_ways(N):
	if N == 1: return 1 # Since there is only stair so only one way is to climb the 1 stair.
	if N == 2: return 2 # Since there are two stairs so there are two ways only to climb these stais
	if N == 3: return 4 # Since there are three stairs so there are four ways of climbing these three stairs.

	# Above are the base cases for this recursive problem.

	# Calling recursively the sub problems.
	return stair_climbing_ways(N-1) + stair_climbing_ways(N-2) + stair_climbing_ways(N-3)


print ("Number of ways to climb 3 stairs: {}".format(stair_climbing_ways(3)))
print ("Number of ways to climb 10 stairs: {}".format(stair_climbing_ways(10)))
print ("Number of ways to climb 15 stairs: {}".format(stair_climbing_ways(15)))

