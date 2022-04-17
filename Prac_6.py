L = []
diy = {}
t = int(input())      #t=temp
while (t!=0):
    arr = input()
    L.append(arr)
    t-=1
print(len(dict.fromkeys(L)))
for i in range(len(L)):
    diy.update({L[i]:L.count(L[i])})
for L in diy:
    print(diy.get(L))
