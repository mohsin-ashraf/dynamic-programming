def stair_climbing_ways(N):
	ways = [0] * (N+1)
	ways[1] = 1 # Base case 1
	ways[2] = 2 # Base case 2
	ways[3] = 4 # Base case 3
	for i in range(4,N+1):
		ways[i] = ways[i-1] + ways[i-2] + ways[i-3]
	return ways[N]

print ("Number of ways to climb 3 stairs: {}".format(stair_climbing_ways(3)))
print ("Number of ways to climb 10 stairs: {}".format(stair_climbing_ways(10)))
print ("Number of ways to climb 15 stairs: {}".format(stair_climbing_ways(15)))

