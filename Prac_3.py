recurring = int(input())                   
rooms = list(map(int, input().split()))    

for i in range(len(rooms)):
    
    if (rooms.count(i) != recurring and rooms.count(i) != 0):
        print(i)
