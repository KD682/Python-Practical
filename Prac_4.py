size = int(input())
ru = list(map(int, input().split()))    #ru=runner_ups
print(sorted(list(set(runner_ups)))[-2])
