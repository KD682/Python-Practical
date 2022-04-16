ls = []
def l(X,Y):              #l=Lapindrome
    beg = ls[i][:X]
    end = ls[i][Y:]
    rend = end[::-1]
    if beg == end or beg == rend:
        print('YES')
    else:
        print('NO')
t = int(input())
while (t!=0):
    st = input()
    ls.append(st)
    t-=1
for i in range(len(ls)):
    s = len(ls[i])//2
    if len(ls[i])%2 != 0:
        l(s, s+1)
    else:
        l(s, s)
